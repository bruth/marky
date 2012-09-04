from django.conf.urls import patterns, url


urlpatterns = patterns('marky.views',
    url(r'^$', 'preview', name='marky-preview'),
    url(r'^api/$', 'api', name='marky-api'),
)
