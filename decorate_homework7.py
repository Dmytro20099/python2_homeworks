from typing import Callable


types = [int, str, float]

def input_message(message):
    result =  f'Your new message >>>> {message}'
    return result


def create_new_message(func: Callable, arg, delete_type) -> None:
    if type(arg) == list:
        result = []
        for value in arg:
            result.append(value)
            if type(value) == delete_type:
                result.remove(value)
        new_message = func(result)
        return new_message
    else:
        new_message = func(arg)
        return new_message


result_message = create_new_message(func=input_message, arg=['6666', 99], delete_type=int)
print(result_message)
