from django.db import models


class Report(models.Model):
    name = models.CharField(max_length=64)
    jira_jql = models.CharField(max_length=300)
    testrail_plan_id = models.IntegerField()

    def __unicode__(self):
        return self.name



class Testrail(models.Model):
    report = models.ManyToOneRel('Report', 'testrail_plan_id')
    link = models.URLField(max_length=30)


    def __unicode__(self):
        return self.plan_id


class Jira(models.Model):
    report = models.OneToOneField('Report')

    def __unicode__(self):
        return self.report.name


class Bug(models.Model):
    jira_connect = models.ForeignKey('Jira')
    bug_id = models.CharField(max_length=10)
    description = models.CharField(max_length=300)
    priority = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    fix_version = models.CharField(max_length=20)
    assignee = models.CharField(max_length=20)


    def __unicode__(self):
        return self.bug_id