from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^_ah/warmup$', 'djangoappengine.views.warmup'),
    (r'^_ah/mail/(?P<address>.*)$', 'services.views.email_handler'),
    (r'^admin/', include(admin.site.urls)),
    (r'^version$', 'views.version'),
    (r'^locationrandom$', 'views.locationrandom'),
    (r'^$', 'django.views.generic.simple.direct_to_template',
        {'template': 'index.html'}),
    (r'^page.html', 'django.views.generic.simple.direct_to_template',
        {'template': 'page.html'}),
    (r'^examples.html', 'django.views.generic.simple.direct_to_template',
        {'template': 'examples.html'}),
    (r'^hello.html', 'django.views.generic.simple.direct_to_template',
        {'template': 'hello.html'}),
)

