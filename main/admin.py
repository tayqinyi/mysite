from django.contrib import admin
from main import models
from tinymce.widgets import TinyMCE
from django.db import models as dbmodels
from django import forms
# Register your models here.

class BaseAdminForm(forms.ModelForm):
  class Meta:
    model = models.BaseObject;
    widgets = {
      'description': TinyMCE(),
    }
    fields = '__all__'

class BaseAdmin(admin.ModelAdmin):
    form = BaseAdminForm

allModels = [models.Skill, models.Project, models.Resume_Education, models.Resume_Job]

admin.site.register(allModels, BaseAdmin)
