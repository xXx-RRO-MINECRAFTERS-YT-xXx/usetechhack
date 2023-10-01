# -*- coding: utf-8 -*-

import graphene
from pizda.services.jwt import generate_jwt_token

class GenerateTokenMutation(graphene.Mutation):
    class Arguments:
        access = graphene.String(required=True)

    token = graphene.String()

    def mutate(self, info, access):
        # Получите пользователя, для которого вы хотите сгенерировать токен
        user = info.context.user

        # Проверьте, что пользователь аутентифицирован, если это необходимо

        token = generate_jwt_token(user.id, access)

        return GenerateTokenMutation(token=token)

class Mutation(graphene.ObjectType):
    generate_token = GenerateTokenMutation.Field()
