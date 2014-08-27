
def remove_entries(entries, dic):
    for key in entries:
        if key in dic:
            del dic[key]


def clean_testrail_dic(dic):
    for key in dic.keys():
        if dic[key] == '0':
            del dic[key]


def create_color_list(keys):
    color_list = []
    for key in keys:
        if key == 'tc_untested':
            color_list.append('#4D4D4D')
        if key == 'tc_passed':
            color_list.append('#60BD68')
        if key == 'tc_retest':
            color_list.append('#B2912F')
        if key == 'tc_failed':
            color_list.append('#F15854')
        if key == 'tc_NA':
            color_list.append('#DECF3F')
    return color_list


def replace_at_index(l, val, new_val):
    i = l.index(val)
    l.remove(val)
    l.insert(i,new_val)


def replace_to_human_names(list):
    for item in list:
        if item == 'tc_untested':
            replace_at_index(list,item,"Untested")
        if item == 'tc_passed':
            replace_at_index(list,item,"Passed")
        if item == 'tc_retest':
            replace_at_index(list,item,"Retest")
        if item == 'tc_failed':
            replace_at_index(list,item,"Failed")
        if item == 'tc_NA':
            replace_at_index(list,item,"Not Available")