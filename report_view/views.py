# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response

from report_view.models import Bug, Report, Jira
from django.shortcuts import render
from django_tables2 import RequestConfig
from report_view.tables import Report_Table

# def bug_row(request):
#     render(request, "index.html", {"bugs": Bug.objects.all()})

# def index(request):
#     # Obtain the context from the HTTP request.
#     context = RequestContext(request)
#
#     all_bugs = Report_Table(Bug.objects.all())
#     RequestConfig(request).configure(all_bugs)
#
#     return render(request, "report_view/index.html", {'all_bugs': all_bugs})

def index(request, report_name_url):

    report_name = report_name_url.replace('_', ' ')

    try:
        report = Report.objects.get(name=report_name)
        jira_connector = Jira.objects.get(report=report)
        report_table = Report_Table(Bug.objects.filter(jira_connect=jira_connector))
        RequestConfig(request).configure(report_table)
    except Report.DoesNotExist:
        pass

    # Go render the response and return it to the client.
    return render(request, "report_view/index.html", {'report_table': report_table, 'report_name': report_name,
                                                      'reports': Report.objects.all()})