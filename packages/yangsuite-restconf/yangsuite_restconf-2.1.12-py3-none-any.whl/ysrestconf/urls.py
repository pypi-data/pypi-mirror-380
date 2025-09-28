# Copyright 2016 to 2021, Cisco Systems, Inc., all rights reserved.
from django.conf.urls import url
from . import views

app_name = 'restconf'
urlpatterns = [
    url(r'^$', views.render_main_page, name="rendermainpage"),
    url(r'^getdevices/', views.get_devices, name="getdevices"),
    url(r'^getyangsets/', views.get_yang_sets, name="getyangsets"),
    url(r'^getmaxdepth/', views.get_max_depth, name="getmaxdepth"),
    url(r'^getyangmodules/', views.get_yang_modules, name="getyangmodules"),
    url(r'^getrcyang/', views.get_rc_yang, name="getrcyang"),
    url(r'^genswag/', views.gen_swag, name="genswag"),
    url(r'^getchunk/', views.get_chunk, name="getchunk"),
    url(r'^genstatus/', views.get_status, name="genstatus"),
    url(r'^getrestmethods/', views.get_rest_methods, name="getrestmethods"),
    url(r'^downloadansible/', views.download_ansible, name="downloadansible"),
    url(r'^getmediatypes/', views.get_media_types, name="getmediatypes"),
    url(r'^downloadjson/', views.download_json, name="downloadjson"),
    url(r'^downloadyaml/', views.download_yaml, name="downloadyaml"),
    url(r'^proxy/(?P<url>.*)$', views.RestProxyView.as_view(), name="rcproxy"),
]
