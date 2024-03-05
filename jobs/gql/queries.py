from jobs.models import Jobs, Applications
import graphene
from .types import JobType
from graphql_jwt.decorators import login_required

class Query(graphene.ObjectType):
    jobs = graphene.List(JobType)
    applications = graphene.List(JobType)

    @login_required
    def resolve_jobs(self, info):
        return Jobs.objects.filter(user=info.context.user.id)
    
    @login_required
    def resolve_applications(self, info):
        applied_jobs = Applications.objects.filter(user=info.context.user.id)
        jobs = []
        for job in applied_jobs:
            jobs.append(job.job)
        return jobs
