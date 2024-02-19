def uppercase_string(input_string):
    """принимает на вход строку и возвращает ее со всеми заглавными буквами"""
    return input_string.upper()


def capitalize_words(input_str):
    """Делает заглавными первые буквы каждого слова в строке поступившей на вход"""
    return ' '.join(word.capitalize()
                    for word in input_str.split())

