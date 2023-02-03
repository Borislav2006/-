from random import choice


def open_quiz_solution(lesson_name, material_name):
    """ Функция, прочитывающая решение питоновской викторины """
    with open(f"Materials_PYTHON\\Quiz Solutions\\{lesson_name}\\{material_name}", encoding="utf-8") as file:
        text_in_file = file.read()
    return text_in_file


def open_function_text(function_number):
    """ Функция, прочитывающая решение питоновской викторины """
    with open(f"Functions_PYTHON\\Functions Text\\{function_number}", encoding="utf-8") as file:
        text_in_file = file.read()
    return text_in_file


def read_text_file(file):
    """ Функция, возвращающая содержимое текстового файла """
    with open(file, encoding="utf-8") as file:
        text_in_file = file.read()
    return text_in_file


def open_photo(lesson_name, material_name):
    """ Функция, возвращающая питоновскую фотографию """
    return open(f"Materials_PYTHON\\Theory Pictures\\{lesson_name}\\{material_name}.png", mode="rb")


def send_theory_photo(lesson_name, material_name):
    """ Функция, возвращающая питоновскую фотографию (теорию) """
    return f"Materials_PYTHON\\Theory Pictures\\{lesson_name}\\{material_name}.png"
