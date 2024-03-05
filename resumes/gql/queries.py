from resumes.models import Resume
import graphene
from .types import ResumeType
from graphql_jwt.decorators import login_required

class Query(graphene.ObjectType):
    resumes = graphene.List(ResumeType)

    @login_required
    def resolve_resumes(self, info):
        return Resume.objects.filter(user=info.context.user.id)
