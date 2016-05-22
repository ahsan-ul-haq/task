from django.conf.urls import include, patterns, url


urlpatterns = patterns('',
                       url(r'^v1/', include('backend.api.v1.urls')),
                       )
