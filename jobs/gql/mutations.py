import graphene
from .types import JobType, CreateJobInputType
from jobs.models import Jobs, Applications
from graphql_jwt.decorators import login_required

class CreateJob(graphene.Mutation):
    class Arguments:
        input = CreateJobInputType(required=True)

    job = graphene.Field(JobType)

    @login_required
    def mutate(self, info, input):
        user = info.context.user
        job = Jobs.objects.create(user=user, title=input.title, description=input.description)
        return CreateJob(job=job)

class ApplyJob(graphene.Mutation):
    success = graphene.Boolean(default_value=False)
    class Arguments:
        job_id = graphene.Int(required=True)

    @login_required
    def mutate(self, info, job_id):
        user = info.context.user
        job = Jobs.objects.get(id=job_id)
        Applications.objects.create(user=user, job=job)
        return ApplyJob(success=True)

class Mutation(graphene.ObjectType):
    create_job = CreateJob.Field()
    apply_job = ApplyJob.Field()