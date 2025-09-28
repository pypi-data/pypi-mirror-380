# Copyright 2016 to 2021, Cisco Systems, Inc., all rights reserved.
import json
import re
import yaml
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from djproxy.views import HttpProxy
from requests.utils import unquote

from yangsuite import get_logger
from ysdevices import YSDeviceProfile
from ysfilemanager import YSYangSet
from ysrestconf.restconf import (
    DEFAULT_CONTENT_TYPES,
    generate_swagger,
    get_parse_status,
    get_header,
    ParseRestconfError,
    MAX_DEPTH,
    REST_METHODS,
)
from ysrestconf.ansible import create_playbook

log = get_logger(__name__)


@login_required
def render_main_page(request):
    """Return the main restconf.html page."""
    return render(request, 'ysrestconf/index.html')


@login_required
def get_devices(request):
    devices = YSDeviceProfile.list(require_feature="restconf")

    return JsonResponse({'devices': devices})


@login_required
def get_yang_sets(request):
    owner = request.user.username
    yang_sets = YSYangSet.user_yangsets(owner)

    return JsonResponse({
        'yangSets': yang_sets,
        'owner': owner,
    })


@login_required
def get_max_depth(request):
    return JsonResponse({
        'maxDepth': MAX_DEPTH,
    })


@login_required
def get_yang_modules(request):
    owner = request.user.username
    set_name = request.GET.get('yangset')

    if set_name is not None:
        yang_set = YSYangSet.load(owner, set_name)
        modules = yang_set._modules
        return JsonResponse({'yangModules': modules})
    elif set_name is None:
        msg = 'Set name cannot be empty'
        return JsonResponse({}, status=500, reason=msg)


@login_required
def get_rc_yang(request, yangset=None, modulenames=None):
    """Render the base netconf page, with optional selections.

    Args:
      request (django.http.HttpRequest): HTTP GET request

        -  devices (list): Device profiles that have been configured.
        -  yangset (str): YANG set slug 'owner+setname' to auto-select.
        -  modulenames (str): module name(s) to auto-select from this yangset,
           as comma-separated list of the form "module-1,module-2,module-3"
    Returns:
      django.http.HttpResponse: page to display
    """
    devices = YSDeviceProfile.list(require_feature="restconf")

    return render(request, 'ysrestconf/restconf.html', {
        'devices': devices,
        'yangset': yangset or '',
        'modulenames': modulenames or '',
    })


def get_media_types(request):
    """Get the default media content types"""
    return JsonResponse({
        'types': DEFAULT_CONTENT_TYPES
    })


@login_required
def gen_swag(request):
    """Generate swagger object."""
    req = {}
    swagobj = {}
    req['yangset'] = request.GET.get('yangset')
    req['user'] = request.user.username
    req['models'] = request.GET.getlist('models')
    req['nodes'] = []
    req['proxyhost'] = request.GET.get('host')
    req['depthlimit'] = request.GET.get('depthlimit', 'No limit')
    req['custommediatypes'] = request.GET.get('custommediatypes', None)

    if 'depthlimit' in req and isinstance(req['depthlimit'], str) and req['depthlimit'].isdigit():
        req['depthlimit'] = int(req['depthlimit'])
    else:
        req['depthlimit'] = None

    if 'custommediatypes' in req and req['custommediatypes']:
        mediaTypes = req['custommediatypes'].split(',')
        req['custommediatypes'] = [unquote(mt) for mt in mediaTypes]

    nodes = request.GET.getlist('nodes')
    device = request.GET.get('device')

    for node in nodes:
        try:
            req['nodes'].append(json.loads(node))
        except Exception:
            return JsonResponse(
                {},
                status=500,
                reason='Unable to parse node with data: {}'.format(node)
            )

    dev_profile = YSDeviceProfile.get(device)

    if not dev_profile:
        msg = '{0} does not have a profile'.format(dev_profile)
        return JsonResponse({}, status=500, reason=msg)
    if not dev_profile.restconf.enabled:
        msg = '{0} is not RESTCONF enabled'.format(dev_profile)
        return JsonResponse({}, status=500, reason=msg)

    req['host'] = dev_profile

    try:
        swagobj = generate_swagger(req)
    except ParseRestconfError as e:
        return JsonResponse({}, status=404, reason=str(e))

    return JsonResponse({'swagobj': swagobj}, status=200)


@login_required
def download_yaml(request):
    """
    Download the OpenAPI YAML file.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: The response object containing the YAML data string
        and the filename.
    """
    data = json.loads(request.body.decode('utf-8'))
    openapi_doc = data['openapiDoc']
    yang_model = data['yangModel']
    node_name = data['nodeName']

    # Delete unwanted properties
    if 'pageCount' in openapi_doc:
        del openapi_doc['pageCount']
    if 'pagination' in openapi_doc:
        del openapi_doc['pagination']

    filename = f'{yang_model}_{node_name}.yaml'
    data = yaml.dump(
        openapi_doc,
        default_flow_style=False,
        allow_unicode=True
    )

    return JsonResponse({
        'data': data,
        'filename': filename
    })


@login_required
def download_json(request):
    """
    Download the OpenAPI JSON file.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: Object containing the JSON data string and the filename.
    """
    data = json.loads(request.body.decode('utf-8'))
    openapi_doc = data['openapiDoc']
    yang_model = data['yangModel']
    node_name = data['nodeName']

    # Delete unwanted properties
    if 'pageCount' in openapi_doc:
        del openapi_doc['pageCount']
    if 'pagination' in openapi_doc:
        del openapi_doc['pagination']

    filename = f'{yang_model}_{node_name}.json'
    data = json.dumps(openapi_doc, indent=2)

    return JsonResponse({
        'data': data,
        'filename': filename
    })


@login_required
def get_status(request):
    """Get the status of the users swagger generator."""
    status = get_parse_status(request.user.username)
    return JsonResponse({'value': 10000, 'max': 10001, 'info': status})


@login_required
def get_chunk(request):
    """Get OpenAPI object."""
    return JsonResponse({'swagobj': get_header(request)}, status=200)


@login_required
def download_ansible(request):
    data = json.loads(request.body)
    openapi_doc = data['openapiDoc']
    yang_modules = data['yangModules']
    depth_limit = data['depthLimit']
    yang_set = data['yangSet']
    filename = data['scriptFileName']
    task_name = data['ansibleTaskName']
    msg_name = data['restMessageName']
    xpath = data['xpath']
    xpath_value = data['xpathValue'] or ''
    method = data['selectedRestMethod']
    host = data['host']
    nodes = data['nodes']
    device = data['device']
    content_type = data['mediaType'] or ''
    user_custom_content = data['customContent'] or ''
    openapi_exists_in_req = False

    # Generate new OpenAPI doc if frontend did not have it yet
    if not openapi_doc:
        req = {}
        req['yangset'] = yang_set
        req['user'] = request.user.username
        req['models'] = yang_modules
        req['nodes'] = []
        req['proxyhost'] = host
        req['depthlimit'] = depth_limit
        req['custommediatypes'] = [content_type]
        if hasattr(
            req['depthlimit'], 'isdigit'
        ) and req['depthlimit'].isdigit():
            req['depthlimit'] = int(req['depthlimit'])
        else:
            req['depthlimit'] = None
        req['nodes'] = [nodes]

        dev_profile = YSDeviceProfile.get(device)
        if not dev_profile:
            msg = '{0} does not have a profile'.format(dev_profile)
            return JsonResponse({}, status=500, reason=msg)
        if not dev_profile.restconf.enabled:
            msg = '{0} is not RESTCONF enabled'.format(dev_profile)
            return JsonResponse({}, status=500, reason=msg)
        req['host'] = dev_profile

        try:
            openapi_doc = generate_swagger(req)
        except ParseRestconfError as e:
            return JsonResponse({}, status=404, reason=str(e))
    else:
        # Set var to not send back OpenAPI doc in response
        openapi_exists_in_req = True

    try:
        # Generate playbook content
        playbook = create_playbook(
            filename, task_name, msg_name, xpath, method, openapi_doc,
            xpath_value=xpath_value, content_type=content_type,
            user_custom_content=user_custom_content,
        )
        content, params_map = playbook.gen_playbook_content()
        response = {
            'content': content,
            'paramsMap': params_map,
            'filename': playbook.filename,
            'openapiDoc': openapi_doc if not openapi_exists_in_req else None
        }
    except ValueError as e:
        return JsonResponse({}, status=404, reason=str(e))

    return JsonResponse(response)


@login_required
def get_rest_methods(request):
    """Get the valid methods that this YS plugin supports"""
    return JsonResponse({'methods': REST_METHODS})


class RestProxyView(HttpProxy):
    """Proxy RESTCONF request to avoid CSRF violations."""

    base_url = 'https://restconf/data/'
    verify_ssl = False
    ignored_request_headers = []  # Overwriting HttpProxy.ignored_request_headers

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        # TODO: slashes in key values do not get escaped
        url = kwargs.get('url', '')
        match = re.findall(
            r'(ethernet=\d+/\d+/\d+|ethernet=\d+/\d+)',
            url,
            flags=re.IGNORECASE
        )
        slashes = []
        for m in match:
            slashes.append((m, m.replace('/', '%2f')))
        for m, s in slashes:
            url = url.replace(m, s)
        # TODO: NGINX removes second slash when passing URL
        if 'https://' not in url:
            url = url.replace('https:/', 'https://')
        kwargs['url'] = url
        return super().dispatch(request, *args, **kwargs)
