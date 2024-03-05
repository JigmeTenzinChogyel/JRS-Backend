from graphene_django.types import DjangoObjectType
import graphene
from files.models import Files

class FileType(DjangoObjectType):
    class Meta:
        model = Files
        fields = '__all__'
        

class UploadFileInputType(graphene.InputObjectType):
    file = graphene.String(required=True)
    filename = graphene.String(required=True)
    mimetype = graphene.String(required=True)
    job_id = graphene.Int(required=False)
