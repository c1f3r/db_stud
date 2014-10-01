from django.conf.urls import patterns, include, url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from db import views

api_router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = patterns('',
                       url(r'^groups$', views.GroupList.as_view(), name='group-list'),
                       url(r'^tagtest$', views.ForTagTest.as_view(), name='group-test-list'),
                       # url(r'^\?id=(?P<pk>[0-9]+)/$', views.GroupDetail.as_view(), name='group-detail'),
                       url(r'^groups/(?P<pk>[0-9]+)$', views.GroupDetail.as_view(), name='group-detail'),
                       url(r'^students$', views.StudentList.as_view(), name='student-list'),
                       url(r'^students/(?P<pk>[0-9]+)$', views.StudentDetail.as_view(), name='student-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)