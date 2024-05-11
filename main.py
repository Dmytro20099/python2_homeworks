def longest_string(first_str: str, second_str: str) -> str:
    """LONGEST_STRING return the longest text,
    example: longest_string('yy', 'yyy') -> 'yyy'"""

    result = ""
    if len(first_str) > len(second_str):
        result += first_str
    elif len(second_str) > len(first_str):
        result += second_str
    else:
        result += "first_str = second_str"
    return result


def digit_list(user_list: list) -> bool:
    """DIGIT_LIST return True if your text has only digits, else: False,
    example1: digit_list([3, 5, 7, 2, 13, 7]) -> True
    example2: digit_list([6, 5, 't', 'df', 7, 8, 3]) -> False"""

    result = True
    for symbol in user_list:
        if str(symbol).isdigit():
            result = True
        else:
            result = False
            break
    return result


print(digit_list([6, 5, 't', 'df', 7, 8, 3]))


def random_symbols():
    """PRINT_SYMBOLS print '/' % 50"""

    print("'/' % 50")
