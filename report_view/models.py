from django.db import models


class Report(models.Model):
    name = models.CharField(max_length=64, unique=True)
    jira_jql = models.CharField(max_length=300)
    testrail_plan_id = models.IntegerField()

    def __unicode__(self):
        return self.name


class Testrail(models.Model):
    report = models.OneToOneField('Report')
    tc_untested = models.CharField(max_length=10)
    tc_passed = models.CharField(max_length=10)
    tc_failed = models.CharField(max_length=10)
    tc_retest = models.CharField(max_length=10)
    tc_NA = models.CharField(max_length=10)

    def __unicode__(self):
        return self.report.name


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