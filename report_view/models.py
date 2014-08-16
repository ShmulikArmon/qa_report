from django.db import models


class Testrail(models.Model):
    plan_id = models.IntegerField(help_text="The number at the end on the main URL")
    link = models.URLField()


    def __unicode__(self):
        return self.plan_id


class Jira(models.Model):
    service = models.CharField(max_length=30)
    component_id = models.CharField(max_length=20)
    tag_id = models.CharField(max_length=20)
    epic_link = models.CharField(max_length=20)
    jql = models.CharField(max_length=200)

    def __unicode__(self):
        return self.component_id


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