from django_tables2 import tables
from report_view.models import Bug
from django.shortcuts import render
from report_view.models import Bug

class Report_Table(tables.Table):
    bug_id = tables.columns.TemplateColumn('<a href="https://tabtale.atlassian.net/browse/{{ record.bug_id }}">{{ record.bug_id }}</a>')
    description = tables.columns.Column()
    priority = tables.columns.TemplateColumn('{% if record.priority == "Blocker" or record.priority == "Critical" %}<font color="red">{{ record.priority }}</font>{% else %}{{ record.priority }}{% endif %}')
    status = tables.columns.Column()
    fix_version = tables.columns.Column()
    assignee = tables.columns.Column()

    class Meta:
        model = Bug
        attrs = {'class': 'table'}
        exclude = ('id',)
        # www.attrs = {'a' : "http://facebook.com"}