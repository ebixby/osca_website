from django.db import models

class Position(models.Model):
    title = models.CharField(length=100)
    credit = models.DecimalField()
    stipend = models.IntegerField()
    semesters = ManyToManyField(membership.Semester)
    is_employee = models.BooleanField()
    supported_by = models.ManyToManyField(Position)
    reports_to = models.ManyToManyField(Position)
    time = models.IntegerField()
    appointments = models.ManyToManyField(Position)
    general_respons = models.TextField()
    specific_respons = models.TextField()
    timeline = models.TextField()
    need_to_know = models.TextField()
    relationships = models.TextField()
    permissions = models.ManyToManyField(Permission)
    committees = models.ManyToManyField(Committee, through CommitteeMember)

class Committee(models.Model):
    is_open = models.BooleanField()
    meeting_time = models.DateTimeField()

class CommitteeMember(models.Model):
    comittee = models.ForeignKey(Committee)
    position = models.ForeignKey(Position)
    is_chair = models.BooleanField()
