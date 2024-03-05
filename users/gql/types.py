from graphene_django.types import DjangoObjectType
import graphene
from users.models import CustomUser

class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'name', 'type']

class CreateUserInputType(graphene.InputObjectType):
    email = graphene.String(required=True)
    name = graphene.String(required=True)
    type = graphene.String(required=True)
    password = graphene.String(required=True)