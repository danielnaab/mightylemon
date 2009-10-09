from django.conf.urls.defaults import *

import views

urlpatterns = patterns('',
    (r'^contact/$', views.contact, {'template_name': 'natty/contact.html'}),
    (r'^projects/$', views.contact, {'template_name': 'natty/projects.html'}),
)
