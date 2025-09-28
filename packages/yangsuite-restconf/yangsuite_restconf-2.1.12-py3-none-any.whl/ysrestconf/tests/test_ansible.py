import os
import unittest
import json
import yaml

from yangsuite.paths import set_base_path
from ysrestconf.ansible import create_playbook


class TestAnsiblePlaybook(unittest.TestCase):
    """Test AnsiblePlaybook class for generating URL, body, and content"""
    @classmethod
    def setUpClass(cls):
        cls.testdir = os.path.join(os.path.dirname(__file__), 'data')
        cls.openapi_dir = os.path.join(cls.testdir, 'openapi')
        cls.playbooks_dir = os.path.join(cls.testdir, 'playbooks')
        cls.user = 'testrest'
        cls.proxyhost = 'localhost:8480'
        cls.devicename = 'CSR1K-7'

        set_base_path(cls.testdir)
        cls.filename = 'testscript.yaml'
        cls.task_name = 'testtask'
        cls.msg_name = 'testmsg'
        cls.xpath_value = 15
        cls.openapi_doc = {}

    def test_get_nested_leaf(self):
        """Test playbook of GET nested leaf"""
        file = open(os.path.join(self.openapi_dir, 'test-leaf.json'))
        openapi_doc = json.load(file)
        file.close()
        # Nested leaf with one key in parent container
        xpath = '/native/user-name/privilege'
        method = 'GET'

        playbook_obj = create_playbook(
            self.filename, self.task_name, self.msg_name, xpath,
            method, openapi_doc,
            content_type='application/yang-data+json',
        )
        content, params_map = playbook_obj.gen_playbook_content()
        content = yaml.safe_load(content)

        expected_content = [{
            'name': 'testmsg',
            'hosts': 'HOST_NAME_HERE',
            'gather_facts': False,
            'tasks': [
                {
                    'name': 'testtask',
                    'ansible.netcommon.restconf_get': {
                        'output': 'json',
                        'path': (
                            'Cisco-IOS-XE-native:native'
                            '/user-name={user-name-name}'
                            '/privilege'
                        )
                    },
                }
            ],
        }]
        expected_params_map = {'user-name': 'user-name-name'}

        self.assertEqual(content, expected_content)
        self.assertEqual(params_map, expected_params_map)

    def test_patch_nested_leaf(self):
        """Test playbook of PATCH nested leaf"""
        file = open(os.path.join(self.openapi_dir, 'test-leaf.json'))
        openapi_doc = json.load(file)
        file.close()
        # Nested leaf with one key in parent container
        xpath = '/native/user-name/privilege'
        xpath_value = 15
        method = 'PATCH'

        playbook_obj = create_playbook(
            self.filename, self.task_name, self.msg_name, xpath,
            method, openapi_doc, xpath_value=xpath_value,
            content_type='application/yang-data+json',
        )
        content, params_map = playbook_obj.gen_playbook_content()
        content = yaml.safe_load(content)

        expected_content = [{
            'name': 'testmsg',
            'hosts': 'HOST_NAME_HERE',
            'gather_facts': False,
            'tasks': [{
                    'name': 'testtask',
                    'ansible.netcommon.restconf_config': {
                        'method': 'patch',
                        'format': 'json',
                        'path': (
                            'Cisco-IOS-XE-native:native'
                            '/user-name={user-name-name}/privilege'
                        ),
                        'content': '{"privilege": 15}',
                    },
            }],
        }]
        expected_params_map = {'user-name': 'user-name-name'}

        self.assertEqual(content, expected_content)
        self.assertEqual(params_map, expected_params_map)

    def test_delete_nested_leaf(self):
        """Test playbook of DELETE nested leaf"""
        file = open(os.path.join(self.openapi_dir, 'test-leaf.json'))
        openapi_doc = json.load(file)
        file.close()
        # Nested leaf with one key in parent container
        xpath = '/native/user-name/privilege'
        method = 'DELETE'

        playbook_obj = create_playbook(
            self.filename, self.task_name, self.msg_name, xpath,
            method, openapi_doc, xpath_value=xpath,
            content_type='application/yang-data+json',
        )
        content, params_map = playbook_obj.gen_playbook_content()
        content = yaml.safe_load(content)

        expected_content = [{
            'name': 'testmsg',
            'hosts': 'HOST_NAME_HERE',
            'gather_facts': False,
            'tasks': [
                {
                    'name': 'testtask',
                    'ansible.netcommon.restconf_config': {
                        'format': 'json',
                        'method': 'delete',
                        'path': (
                            'Cisco-IOS-XE-native:native'
                            '/user-name={user-name-name}/privilege'
                        )
                    },
                }
            ],
        }]
        expected_params_map = {'user-name': 'user-name-name'}

        self.assertEqual(content, expected_content)
        self.assertEqual(params_map, expected_params_map)

    def test_get_container(self):
        """Test GET container playbook"""
        file = open(os.path.join(self.openapi_dir, 'test-container.json'))
        openapi_doc = json.load(file)
        file.close()
        xpath = '/top-level-container'
        method = 'GET'

        playbook_obj = create_playbook(
            self.filename, self.task_name, self.msg_name,
            xpath, method, openapi_doc,
            content_type='application/yang-data+json',
        )
        content, params_map = playbook_obj.gen_playbook_content()
        content = yaml.safe_load(content)

        expected_content = [{
            'name': 'testmsg',
            'hosts': 'HOST_NAME_HERE',
            'gather_facts': False,
            'tasks': [
                {
                    'name': 'testtask',
                    'ansible.netcommon.restconf_get': {
                        'output': 'json',
                        'path': 'test-container:top-level-container',
                    },
                }
            ],
        }]
        expected_params_map = {}

        self.assertEqual(content, expected_content)
        # No parameters expected
        self.assertEqual(params_map, expected_params_map)

    def test_patch_container(self):
        """Test PATCH container playbook"""
        file = open(os.path.join(self.openapi_dir, 'test-container.json'))
        openapi_doc = json.load(file)
        file.close()
        xpath = '/top-level-container'
        xpath_value = []
        method = 'PATCH'

        playbook_obj = create_playbook(
            self.filename, self.task_name, self.msg_name, xpath,
            method, openapi_doc, xpath_value=xpath_value,
            content_type='application/yang-data+json',
        )
        content, params_map = playbook_obj.gen_playbook_content()
        content = yaml.safe_load(content)

        expected_content = [{
            'name': 'testmsg',
            'hosts': 'HOST_NAME_HERE',
            'gather_facts': False,
            'tasks': [{
                'name': 'testtask',
                'ansible.netcommon.restconf_config': {
                    'method': 'patch',
                    'format': 'json',
                    'path': 'test-container:top-level-container',
                    'content': (
                        '{"top-level-container": {"test-leaf-list": []}}'
                    )
                },
            }],
        }]
        expected_params_map = {}

        self.assertEqual(content, expected_content)
        # No parameters should be captured
        self.assertEqual(params_map, expected_params_map)

    def test_delete_container(self):
        """Test DELETE container playbook"""
        file = open(os.path.join(self.openapi_dir, 'test-container.json'))
        openapi_doc = json.load(file)
        file.close()
        xpath = '/top-level-container'
        method = 'DELETE'

        playbook_obj = create_playbook(
            self.filename, self.task_name, self.msg_name, xpath,
            method, openapi_doc, xpath_value=xpath,
            content_type='application/yang-data+json',
        )
        content, params_map = playbook_obj.gen_playbook_content()
        content = yaml.safe_load(content)

        expected_content = [{
            "name": "testmsg",
            "hosts": "HOST_NAME_HERE",
            "gather_facts": False,
            "tasks": [{
                "name": "testtask",
                "ansible.netcommon.restconf_config": {
                    "method": "delete",
                    "format": "json",
                    "path": "test-container:top-level-container"
                }
            }]
        }]
        expected_params_map = {}

        self.assertEqual(content, expected_content)
        # No parameters should be captured
        self.assertEqual(params_map, expected_params_map)

    def test_get_list(self):
        """Test playbook content for GET of nested list"""
        file = open(os.path.join(self.openapi_dir, 'test-nested-list.json'))
        openapi_doc = json.load(file)
        file.close()
        xpath = '/top-level-list-top-level-key'
        method = 'GET'

        playbook_obj = create_playbook(
            self.filename, self.task_name, self.msg_name, xpath,
            method, openapi_doc,
            content_type='application/yang-data+json',
        )

        content, params_map = playbook_obj.gen_playbook_content()
        content = yaml.safe_load(content)
        expected_content = [{
            'name': 'testmsg',
            'hosts': 'HOST_NAME_HERE',
            'gather_facts': False,
            'tasks': [{
                'name': 'testtask',
                'ansible.netcommon.restconf_get': {
                    'output': 'json',
                    'path': (
                        'test-nested-list:top-level-list='
                        '{test-nested-list:top-level-list'
                        '-top-level-key}'
                    )
                },
            }],
        }]
        expected_params_map = {
            'test-nested-list:top-level-list': (
                'test-nested-list:top-level-list-top-level-key'
            )
        }

        self.assertEqual(content, expected_content)
        # No parameters should be captured
        self.assertEqual(params_map, expected_params_map)

    def test_patch_list(self):
        """Test PATCH of a list by modifying one nested leaf"""
        file = open(os.path.join(self.openapi_dir, 'test-list.json'))
        openapi_doc = json.load(file)
        file.close()
        xpath = 'test-list:top-level-list/first-leaf'
        method = 'PATCH'

        playbook_obj = create_playbook(
            self.filename, self.task_name, self.msg_name, xpath,
            method, openapi_doc, xpath_value='testvalue',
            content_type='application/yang-data+json',
        )

        content, params_map = playbook_obj.gen_playbook_content()
        content = yaml.safe_load(content)

        # Add this line to see the full diff
        self.maxDiff = None

        expected_content = [{
            "name": "testmsg",
            "hosts": "HOST_NAME_HERE",
            "gather_facts": False,
            "tasks": [{
                "name": "testtask",
                "ansible.netcommon.restconf_config": {
                    "method": "patch",
                    "format": "json",
                    "path": "test-list:top-level-list="
                        + "{test-list:top-level-list-first-key},"
                        + "{test-list:top-level-list-second-key}/first-leaf",
                    "content": "{\"first-leaf\": \"testvalue\"}"
                }
            }]
        }]
        expected_params_map = {
            'test-list:top-level-list': 'test-list:top-level-list-first-key,'
                                        + 'test-list:top-level-list-second-key'
        }

        self.assertEqual(content, expected_content)
        # No parameters should be captured
        self.assertEqual(params_map, expected_params_map)

    def test_delete_nested_list(self):
        """Test playbook content for DELETE of nested list"""
        file = open(os.path.join(self.openapi_dir, 'test-nested-list.json'))
        openapi_doc = json.load(file)
        file.close()
        xpath = (
            '/top-level-list-top-level-key'
            '/level-2-list/level-3-container'
            '/level-4-list/level-5-list'
        )
        method = 'DELETE'

        playbook_obj = create_playbook(
            self.filename, self.task_name, self.msg_name, xpath,
            method, openapi_doc,
            content_type='application/yang-data+json',
        )

        content, params_map = playbook_obj.gen_playbook_content()
        content = yaml.safe_load(content)
        expected_content = [{
            "name": "testmsg",
            "hosts": "HOST_NAME_HERE",
            "gather_facts": False,
            "tasks": [
                {
                    "name": "testtask",
                    "ansible.netcommon.restconf_config": {
                        "method": "delete",
                        "format": "json",
                        "path": "test-nested-list:top-level-list"
                                + "={test-nested-list:top-level-list-top-level-key}"
                                + "/level-2-list={level-2-list-level-2-key}/"
                                + "level-3-container/level-4-list="
                                + "{level-4-list-level-4-first-key},{level-4-list-"
                                + "level-4-second-key}/level-5-list"
                    }
                }
            ]
        }]
        expected_params_map = {
            'test-nested-list:top-level-list': 'test-nested-list:top-level-list-top-level-key',
            'level-2-list': 'level-2-list-level-2-key',
            'level-4-list': 'level-4-list-level-4-first-key,level-4-list-level-4-second-key'
        }

        self.assertEqual(content, expected_content)
        # No parameters should be captured
        self.assertEqual(params_map, expected_params_map)
