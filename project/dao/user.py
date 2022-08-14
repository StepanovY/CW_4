from project.models import User
from project.tools.security import generate_password_hash


class UserDAO:
    """
    Класс с методами доступа к данным
    """

    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        """
        Метод получения одного пользователя User
        """
        return self.session.query(User).get(uid)

    def get_by_email(self, email):
        """
        Метод поиска пользователя User по его логину (email)
        """
        return self.session.query(User).filter(User.email == email).first()

    def get_all(self):
        """
        Метод получения всех пользователей Users
        """
        return self.session.query(User).all()

    def create(self, user_d):
        """
        Метод создания пользователя User
        :param user_d:
        :return:
        """
        user = User(**user_d)
        self.session.add(user)
        self.session.commit()
        return user

    def delete(self, uid):
        """
        Метод удаления User
        """
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_d):
        """
        Метод обновления данных о пользователе User
        """
        user = self.get_one(user_d.get("id"))
        if user_d.get("email"):
            user.email = user_d.get("email")
        if user_d.get("password"):
            user.password = user_d.get("password")
        if user_d.get("name"):
            user.name = user_d.get("name")
        if user_d.get("surname"):
            user.surname = user_d.get("surname")
        if user_d.get("favourite_genre"):
            user.favourite_genre = user_d.get("favourite_genre")

        self.session.add(user)
        self.session.commit()

    def update_password(self, email, new_password):
        """
        Метод обновления пароля пользователя
        :param email:
        :param new_password:
        :return:
        """
        user = self.get_by_email(email)
        user.password = generate_password_hash(new_password)

        self.session.add(user)
        self.session.commit()

