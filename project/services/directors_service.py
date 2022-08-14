from typing import Optional

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Director


class DirectorsService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Director:
        """
        Сервис получения одного режиссера
        :param pk:
        :return:
        """
        if director := self.dao.get_by_id(pk):
            return director
        raise ItemNotFound(f'Genre with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[Director]:
        """
        Сервис получения списка всех режиссеров
        :param page:
        :return:
        """
        return self.dao.get_all(page=page)
