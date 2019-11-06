import graphene
from graphene_django.types import DjangoObjectType
from . import models

class SkillType(DjangoObjectType):
    class Meta:
        model = models.Skill

class Resume_EducationType(DjangoObjectType):
    class Meta:
        model = models.Resume_Education

class Resume_JobType(DjangoObjectType):
    class Meta:
        model = models.Resume_Job

class Query(graphene.AbstractType):
    all_skills = graphene.List(SkillType)
    all_resume_educations = graphene.List(Resume_EducationType)
    all_resume_jobs = graphene.List(Resume_JobType)

    def resolve_all_skills(self, context, **kwargs):
        return models.Skill.objects.all()

    def resolve_all_resume_educations(self, context, **kwargs):
        return models.Resume_Education.objects.all()

    def resolve_all_resume_jobs(self, context, **kwargs):
        return models.Resume_Job.objects.all()