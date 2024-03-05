from users.models import CustomUser
import graphene
from .types import UserType

class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return CustomUser.objects.all()
