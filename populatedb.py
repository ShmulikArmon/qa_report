
import os
from misc import create_json_file
from testrail_handler import get_plan
from jira_handler import generate_list
from django.core import exceptions as django_exceptions

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qa_report_2.settings')

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
    data = get_plan(report.testrail_plan_id)
    create_json_file('tr_test.json', data)
    create_testrail(report, data["untested_count"], data["passed_count"], data["failed_count"],
                    data["retest_count"], data["custom_status1_count"])


def populate_bugs(jira_list, jira_connector):
    for item in jira_list:
        id = item.key
        des = item.fields.summary
        pr = item.fields.priority.name
        st = item.fields.status.name
        fv = ""
        if len(item.fields.fixVersions) != 0:
            fv = item.fields.fixVersions[0]
        ass = item.fields.assignee.displayName
        create_bug(jira_connector, id, des, pr, st, fv, ass)


def populate():
    create_report("Publishing Server", 'component="PSDK Server"', 6342)
    populate_existing_reports()


def populate_existing_reports():
    reports = Report.objects.all()
    for report in reports:
        jql = report.jira_jql
        jir = create_jira_connector(report)
        try:
            jira_list = generate_list(jql)
            populate_bugs(jira_list,jir)
        except django_exceptions as e:
            print "something went wrong with the jira population: "
            print e
        try:
            populate_testrail(report)
        except django_exceptions as e:
            print "something went wrong with testrail population: "
            print e



def populate_call():
    print "Starting Population of DB..."
    populate()

if __name__ == '__main__':
    print "Starting Population of DB..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qa_report_2.settings')
    from report_view.models import Jira, Bug, Report, Testrail
    populate()
