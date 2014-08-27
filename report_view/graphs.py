
from report_view.models import Testrail
from misc import remove_entries, clean_testrail_dic, create_color_list,replace_to_human_names


def pie_chart(report):
    raw_data = Testrail.objects.filter(report=report).values()
    data = raw_data[0]
    remove_entries(['id','report_id'],data)
    clean_testrail_dic(data)
    xdata = data.keys()
    ydata = data.values()

    color_list = create_color_list(xdata)
    replace_to_human_names(xdata)

    extra_serie = {"color_list": color_list}
    chartdata = {'x': xdata,'y1': ydata, 'extra1': extra_serie, 'chartAttr': False}
    charttype = "pieChart"
    chartcontainer = 'piechart_container'

    chart = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'show_legend': False,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False

        }
    }
    return chart
