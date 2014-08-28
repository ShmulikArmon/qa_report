from testrail import *

tr_client = APIClient('https://tabtale.testrail.com/')
tr_client.user = 'shmulika@tabtale.com'
tr_client.password = 'QWEqwe00'


def make_request(api, id):
    tr_request = '/'.join([api, id])
    try:
        return tr_client.send_get(tr_request)
    except APIError as e:
        print "something went wrong with testrail"
        print e

def get_plan(plan_id):
    return make_request('get_plan',str(plan_id))

def get_run(run_id):
    return make_request('get_run',str(run_id))