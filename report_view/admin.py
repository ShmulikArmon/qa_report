from django.contrib import admin
from report_view.models import Jira, Bug, Testrail, Report

admin.site.register(Jira)
admin.site.register(Bug)
admin.site.register(Testrail)
admin.site.register(Report)