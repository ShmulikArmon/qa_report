
import urllib2, urllib, os
from jira.client import JIRA
from jira import exceptions
import testrail, json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qa_report_2.settings')
from report_view.models import Jira, Bug, Report, Testrail

jira = JIRA(options={'server': 'https://tabtale.atlassian.net'}, basic_auth=('shmulika', 'cECxWccn16'))
tr_client = testrail.APIClient('https://tabtale.testrail.com/')
tr_client.user = 'shmulika@tabtale.com'
tr_client.password = 'QWEqwe00'

def URLRequest(url, params, method="GET"):
    if method == "POST":
        return urllib2.Request(url, data=urllib.urlencode(params))
    else:
        return urllib2.Request(url + "?" + urllib.urlencode(params))


def create_report(name, jql, testrail):
    r = Report.objects.get_or_create(name=name, jira_jql=jql, testrail_plan_id=testrail)[0]
    return r


def create_jira_connector(report):
    j = Jira.objects.get_or_create(report=report)[0]
    return j


def create_bug(jc, id, des, pr, st, fv, ass):
    b = Bug.objects.get_or_create(jira_connect=jc, bug_id=id, description=des, priority=pr, status=st,
                                  fix_version=fv, assignee=ass)[0]
    return b


def create_testrail(report, tc_u, tc_p, tc_f, tc_r, tc_n):
    t = Testrail.objects.get_or_create(report=report, tc_untested=tc_u, tc_passed=tc_p, tc_failed=tc_f,
                                       tc_retest=tc_r, tc_NA=tc_n)[0]
    return t


def populate_testrail(report):
    get_plan_api = 'get_plan'
    plan_id = (str(report.testrail_plan_id))
    tr_request = '/'.join([get_plan_api,plan_id])
    data = tr_client.send_get(tr_request)
    create_testrail(report, data["untested_count"], data["passed_count"], data["failed_count"],
                    data["retest_count"], data["custom_status1_count"])



def populate():
    create_report("Publishing", 'component="PSDK Server"', 6342)
    populate_existing_reports()


def populate_existing_reports():
    reports = Report.objects.all()
    for report in reports:
        jql = report.jira_jql
        jir = create_jira_connector(report)
        try:
            jira_list = jira.search_issues(jql)
            i = 0
            for item in jira_list:
                id = jira_list[i].key
                des = jira_list[i].fields.summary
                pr = jira_list[i].fields.priority.name
                st = jira_list[i].fields.status.name
                fv = ""
                if len(jira_list[i].fields.fixVersions) != 0:
                    fv = jira_list[i].fields.fixVersions[0]
                ass = jira_list[i].fields.assignee.displayName
                create_bug(jir, id, des, pr, st, fv, ass)
                i += 1
        except exceptions.JIRAError as r:
            print "something went wrong with the jira search: "
            print exceptions.get_error_list(r)
        try:
            populate_testrail(report)
        except testrail.APIError as e:
            print "something went wrong with testrail"
            print e



def populate_call():
    print "Starting Population of DB..."
    populate()

if __name__ == '__main__':
    print "Starting Population of DB..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qa_report_2.settings')
    from report_view.models import Jira, Bug, Report
    populate()
