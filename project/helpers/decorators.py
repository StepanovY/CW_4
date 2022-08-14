# Создание декоратора ограничения доступа

import jwt
from flask import request, current_app
from flask_restx import abort


def auth_required(func):
    """
    Декоратор аутентификации пользователя по имени и паролю
    """

    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]

        try:
            jwt.decode(token, key=current_app.config['SECRET_KEY'], algorithms=current_app.config['JWT_ALGORITHM'])
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

        return func(*args, **kwargs)

    return wrapper
