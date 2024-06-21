from strawberry import ID
from . import schemas
from typing import List


class QueryResolver:
    @staticmethod
    def get_tasks(pagination: any) -> List[schemas.Task]:
        # TODO: update the pagination type
        # TODO: Connect to the data layer
        pass

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
