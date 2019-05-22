from django.shortcuts import render
from django.http import HttpResponse
from main import models
import logging
# Create your views here.

def homepage(request):
    return render(request=request,
                  template_name="main/home.html",
                  context={"projects": models.Project.objects.all,
                           "skills": models.Skill.objects.all,
                           "resume_educations": models.Resume_Education.objects.all,
                           "resume_jobs": models.Resume_Job.objects.all})