# Create your views here.

from report_view.models import Bug, Report, Jira, Testrail
from report_view.forms import ReportForm
from django.shortcuts import render
from django_tables2 import RequestConfig
from report_view.tables import Report_Table
from graphs import pie_chart
from tasks import locked_populate

def index(request, report_name_url, posted=False):


    report_name = report_name_url.replace('_', ' ')
    if request.method == 'POST' and not posted:
        report_form = ReportForm(request.POST)
        if report_form.is_valid():
            report_form.save(commit=True)
            return index(request, report_name_url, posted=True)
        else:
            print report_form.errors
    else:
        report_form = ReportForm()
    locked_populate()
    try:
        report = Report.objects.get(name=report_name)
        jira_connector = Jira.objects.get(report=report)
        report_table = Report_Table(Bug.objects.filter(jira_connect=jira_connector))
        RequestConfig(request).configure(report_table)
        chart = pie_chart(report)
    except Report.DoesNotExist:
        pass



    context_dict = dict({'report_table': report_table, 'report_name': report_name,
                         'reports': Report.objects.all(), 'report_form': report_form}.items()
                          + chart.items())
    print(context_dict)
    return render(request, "report_view/index.html", context_dict)
                                                      # 'chart': chart})