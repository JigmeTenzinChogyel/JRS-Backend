import graphene
from .types import ResumeType, CreateResumeInputType
from users.models import CustomUser
from resumes.models import Resume
from graphql_jwt.decorators import login_required


class CreateResume(graphene.Mutation):
    resume = graphene.Field(ResumeType)

    class Arguments:
        input = CreateResumeInputType(required=True)

    @staticmethod
    @login_required
    def mutate(root, info, input):
        user = CustomUser.objects.get(id=info.context.user.id)
        resume = Resume(
            user_id=user,
            title=input.title,
            description=input.description
        )
        resume.save()
        return CreateResume(resume=resume)

class Mutation(graphene.ObjectType):
    create_resume = CreateResume.Field()