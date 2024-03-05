import graphene
from users.gql import schema as users_schema
from resumes.gql import schema as resumes_schema
from jobs.gql import schema as jobs_schema
from files.gql import schema as files_schema

class Query(users_schema.Query, resumes_schema.Query, jobs_schema.Query, files_schema.Query, graphene.ObjectType):
    pass

class Mutation(users_schema.Mutation, resumes_schema.Mutation, jobs_schema.Mutation, files_schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)