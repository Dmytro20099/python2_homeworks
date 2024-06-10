from functools import wraps
from typing import Callable, Any


def do_base_template_decorator(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) == list:
            for value in result:
                if type(value) == str:
                    result.remove(value)
        return f'Your new message >>> {result}'
    return wrapper


@do_base_template_decorator
def input_message(message: Any):
    result = message
    return result


print(input_message([55, 'll', 99, 'kk']))


