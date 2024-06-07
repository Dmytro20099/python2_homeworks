from typing import Callable


types = [int, str, float]

def input_message(message):
    result =  f'Your new message >>>> {message}'
    print(result)
    return result


def create_new_message(func: Callable, arg, delete_type) -> None:
    if type(arg) == list:
        result = []
        for value in arg:
            result.append(value)
            if type(value) == delete_type:
                result.remove(value)
    else:
        result = arg
    return result



resul = create_new_message(func=input_message, arg=['5, 6, 8', 9], delete_type=str)
print(resul)
