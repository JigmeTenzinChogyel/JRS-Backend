from .mutations import Mutation
from .queries import Query
import graphene

schema = graphene.Schema(query=Query, mutation=Mutation)