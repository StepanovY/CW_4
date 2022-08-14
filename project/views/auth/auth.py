from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service, auth_service
from project.setup.api.models import user
from project.setup.api.parsers import page_parser

api = Namespace('auth')


@api.route('/register/')  # регистрация (создание) пользователя в БД
class AuthView(Resource):
    def post(self):
        req_json = request.json
        user = user_service.create(req_json)
        return "OK", 201, {"location": f"/users/{user.id}"}


@api.route('/login/')  # вход пользователя в систему
class AuthView(Resource):
    def post(self):
        """
        Аутентификация пользователя
        :return:
        """
        data = request.json

        email = data.get('email', None)
        password = data.get('password', None)

        if None in [email, password]:
            return '', 400

        tokens = auth_service.generate_token(email, password)

        return tokens, 201

    def put(self):  # создание новой пары токенов
        """
        Создание новой пары токенов
        :return:
        """
        data = request.json
        token = data.get('refresh_token')

        tokens = auth_service.approve_refresh_token(token)

        return tokens, 201
