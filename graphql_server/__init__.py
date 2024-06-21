from typing import List
import strawberry

from .schemas import Task
from .resolvers import QueryResolver, MutationResolver


@strawberry.type
class Query:
    tasks: List[Task] = strawberry.field(resolver=QueryResolver.get_tasks)
    task: (Task | None) = strawberry.field(resolver=QueryResolver.get_task)


@strawberry.type
class Mutation:
    add_task: Task = strawberry.field(resolver=MutationResolver.add_task)
    update_task: (Task | None) = strawberry.field(
        resolver=MutationResolver.update_task)
    delete_task = strawberry.field(resolver=MutationResolver.delete_task)
