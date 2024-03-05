import graphene
from .types import UserType, CreateUserInputType
from users.models import CustomUser
import graphql_jwt

class CreateUser(graphene.Mutation):
    # 1. Declare the mutations result field
    user = graphene.Field(UserType)

    # 2. Declare arguments for the mutation
    class Arguments:
        input = CreateUserInputType(required=True)

    # 3. Create new user model
    def mutate(self, info, input):
        user = CustomUser(
            email=input.email,
            name=input.name,
            type=input.type,
        )
        user.set_password(input.password)
        user.save()

        return CreateUser(user=user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
