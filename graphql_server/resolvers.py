from strawberry import ID
from . import schemas
from typing import List

from model import models
from model.database import DBSession


class QueryResolver:

    @staticmethod
    def get_tasks(pagination: (schemas.PaginationInput | None) = None) -> List[schemas.Task]:
        db = DBSession()
        try:
            query = db.query(models.Task)
            if pagination is not None:
                query = query \
                    .offset(pagination.offset) \
                    .limit(pagination.limit)

            tasks = query.all()
        finally:
            db.close()
        return tasks


@staticmethod
def get_task(task_id: ID) -> (schemas.Task | None):
    # TODO: Connect to the data layer
    pass


class MutationResolver:
    @staticmethod
    def add_task(task_content: str) -> schemas.Task:
        # TODO: Connect to the data layer
        pass

    @staticmethod
    def update_task(task_id: ID, task: any) -> (schemas.Task | None):
        # TODO: update the task type
        # TODO: Connect to the data layer
        pass

    @staticmethod
    def delete_task(task_id: ID) -> None:
        # TODO: Connect to the data layer
        pass
