from jira.client import JIRA
from jira import exceptions as jira_exceptions

jira = JIRA(options={'server': 'https://tabtale.atlassian.net'},
            basic_auth=('shmulika', 'cECxWccn16'))


def generate_list(jql):
    try:
        return jira.search_issues(jql)
    except jira_exceptions as e:
        print "something went wrong with the jira search: "
        print jira_exceptions.get_error_list(e)
