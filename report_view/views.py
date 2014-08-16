# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response

from report_view.models import Bug
from django.shortcuts import render
from django_tables2 import RequestConfig
from report_view.tables import Report_Table

# def bug_row(request):
#     render(request, "index.html", {"bugs": Bug.objects.all()})

def index(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    all_bugs = Report_Table(Bug.objects.all())
    RequestConfig(request).configure(all_bugs)

    return render(request, "report_view/index.html", {'all_bugs': all_bugs})

