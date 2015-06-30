import json

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, View
from django.http import HttpResponse


urlpatterns = patterns('',
    url(r'^error/$', TemplateView.as_view(template_name='none.html'), name='test-error'),
)
