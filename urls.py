from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
        url(r'^$', 'dev.views.hello_page'),
        url(r'^dev/', include('dev.urls', namespace='dev')),
)
urlpatterns += staticfiles_urlpatterns()
