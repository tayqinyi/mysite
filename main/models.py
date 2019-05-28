from django.db import models
import datetime

# Create your models here.
class BaseObject(models.Model):

    name = models.CharField(max_length = 200);
    description = models.TextField(null=True, blank=True);
    imagepath = models.TextField(null=True, blank=True);
    classes = models.TextField(null=True, blank=True);

    def __str__(self):
        return self.name;

    class Meta:
        abstract = True;
        ordering = ('id',)

class BaseResume(BaseObject):
    institute = models.CharField(max_length = 200);
    start = models.DateField("Start Date", null=True, blank=True)
    end = models.DateField("End Date", null=True, blank=True)

    class Meta:
        abstract = True;

class Skill(BaseObject):
    displayname = models.TextField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True);

class Project(BaseObject):
    moreinfo = models.TextField(null=True, blank=True)
    skills = models.ManyToManyField(Skill);

class Resume_Education(BaseResume):
    pass;

class Resume_Job(BaseResume):
    pass;

