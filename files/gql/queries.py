import graphene
from files.models import Files
from .types import FileType
from graphql_jwt.decorators import login_required

class Query(graphene.ObjectType):
    files = graphene.List(FileType)

    @login_required
    def resolve_files(self, info):
        return Files.objects.filter(user=info.context.user.id)