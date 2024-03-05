from graphene_django.types import DjangoObjectType
import graphene
from jobs.models import Jobs

class JobType(DjangoObjectType):
    class Meta:
        model = Jobs
        fields = '__all__'

class CreateJobInputType(graphene.InputObjectType):
    title = graphene.String()
    description = graphene.String()
