from django.db import models
import datetime

# Create your models here.
class BaseObject(models.Model):

    name = models.CharField(max_length = 200);
    description = models.TextField(blank=True);
    imagepath = models.TextField(blank=True);
    classes = models.TextField(blank=True);

    def __str__(self):
        return self.name;

    class Meta:
        abstract = True;
        ordering = ('id',)

class BaseResume(BaseObject):
    institute = models.CharField(max_length = 200);
    start = models.DateTimeField("Start Date", blank=True)
    end = models.DateTimeField("End Date", blank=True)

    class Meta:
        abstract = True;

class Skill(BaseObject):
    displayname = models.TextField(blank=True)
    level = models.IntegerField(blank=True);

class Project(BaseObject):
    moreinfo = models.TextField(blank=True)
    skills = models.ManyToManyField(Skill);

class Resume_Education(BaseObject):
    pass;

class Resume_Job(BaseResume):
    jobtitle = models.CharField(max_length = 200);

