from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
import settings

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'db_stud.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api/', include('db.urls')),
                       url(r'^$', TemplateView.as_view(template_name="index.html"), name="home"),
                       # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}),

)

urlpatterns += patterns('',
                        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)