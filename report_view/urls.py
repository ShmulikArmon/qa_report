from django.conf.urls import patterns, url
from report_view import views

urlpatterns = patterns('',
        url(r'^(?P<report_name_url>\w+)/$', views.index, name='report_name'),
        )