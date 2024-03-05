from graphene_django.types import DjangoObjectType
import graphene
from resumes.models import Resume

class ResumeType(DjangoObjectType):
    class Meta:
        model = Resume
        fields = '__all__'

class CreateResumeInputType(graphene.InputObjectType):
    title = graphene.String(required=True)
    description = graphene.String(required=True)