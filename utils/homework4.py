def get_text_without_step(text: str) -> str:
    result = ""
    for letter in text:
        if letter != " ":
            result += letter
    return result
