from typing import Any, Type, cast

from planar.task_local import TaskLocal

data: TaskLocal[Any] = TaskLocal()


def set_state(ctx: Any):
    return data.set(ctx)


def get_state[T](_: Type[T]) -> T:
    return cast(T, data.get())


def delete_state():
    return data.clear()
