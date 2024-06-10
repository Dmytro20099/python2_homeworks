from typing import Callable
import datetime


db = {"login": "admin", "password": "123"}


def add_two_numbers(number_1: float | int, number_2: float | int) -> float | int:
    result = number_1 + number_2
    return result


def simple_decorator(func: Callable):
    def wrapper(*args, **kwargs):
        data1, data2, *other = args
        print(*args)
        print(kwargs)
        login = input("Enter login: ")
        password = input("Enter password: ")
        if login == db["login"] and password == db["password"]:
            result = func(*args, **kwargs)
    return result




add_two_numbers = simple_decorator(func=add_two_numbers)



print(add_two_numbers())




