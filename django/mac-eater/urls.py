from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'index.html'}),
    ('^page.html', 'django.views.generic.simple.direct_to_template',
     {'template': 'page.html'}),
    ('^examples.html', 'django.views.generic.simple.direct_to_template',
     {'template': 'examples.html'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^version$', 'views.version'),
    (r'^locationrandom$', 'views.locationrandom'),
)

