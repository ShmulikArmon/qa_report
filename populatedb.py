
import urllib2, urllib, os
from jira.client import JIRA

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qa_report_2.settings')
from report_view.models import Jira, Bug

jira = JIRA(options={'server': 'https://tabtale.atlassian.net'}, basic_auth=('shmulika', 'cECxWccn16'))


def URLRequest(url, params, method="GET"):
    if method == "POST":
        return urllib2.Request(url, data=urllib.urlencode(params))
    else:
        return urllib2.Request(url + "?" + urllib.urlencode(params))


def create_jira_connect(srv, cmp, tag, epc):
    j = Jira.objects.get_or_create(service=srv, component_id=cmp, tag_id=tag, epic_link=epc)[0]
    return j


def create_bug(id, des, pr, st, fv, ass):
    b = Bug.objects.get_or_create(bug_id=id, description=des, priority=pr, status=st,
                                  fix_version=fv, assignee=ass)[0]
    return b


def populate():
    result = jira.search_issues('component="PSDK Server"')
    i = 0
    for item in result:
        id = result[i].key
        des = result[i].fields.summary
        pr = result[i].fields.priority.name
        st = result[i].fields.status.name
        fv = ""
        if len(result[i].fields.fixVersions) != 0:
            fv = result[i].fields.fixVersions[0]
        ass = result[i].fields.assignee.displayName
        create_bug(id, des, pr, st, fv, ass)
        i += 1


def populate_call():
    print "Starting Population of DB..."
    populate()

if __name__ == '__main__':
    print "Starting Population of DB..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qa_report_2.settings')
    from report_view.models import Jira, Bug
    populate()