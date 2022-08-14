from flask import request, abort
from flask_restx import Namespace, Resource

from project.container import user_service
from project.helpers.decorators import auth_required
from project.setup.api.models import user
from project.tools.security import get_email_by_token

api = Namespace('user')


@api.route('/')
class UserView(Resource):
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    @auth_required  # декоратор аутентификации пользователя
    def get(self):
        """
        Получение информации о пользователе
        return:
        """
        email = get_email_by_token(request.headers)
        return user_service.get_by_email(email), 200

    @api.marshal_with(user, as_list=True, code=200, description='OK')
    @auth_required  # декоратор аутентификации пользователя
    def patch(self):
        """
        Изменение информации о пользователе
        return:
        """
        req_json = request.json
        email = get_email_by_token(request.headers)
        if "email" not in req_json:
            req_json["email"] = email
        user_service.update(req_json)
        return "", 204

    @auth_required  # декоратор аутентификации пользователя
    def delete(self, user_id):
        """
        Удаление пользователя
        :param user_id:
        :return:
        """
        user_service.delete(user_id)
        return "", 204


@api.route('/password/')
class UserPasswordView(Resource):
    @auth_required
    def put(self):
        """
        Обновление пароля пользователя
        return:
        """
        req_json = request.json
        psw_1 = req_json.get('old_password')
        psw_2 = req_json.get('new_password')
        email = get_email_by_token(request.headers)
        if None in [psw_1, psw_2]:
            abort(400)
        if not email:
            abort(401)
        user_service.update_password(email, psw_2)
        return "", 204
