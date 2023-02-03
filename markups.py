from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup

# --- Кнопки главного меню ---

info_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

btn_list = KeyboardButton("Тренироваться 🥸")

info_menu.add(btn_list)

# Виды викторины

quiz_menu = InlineKeyboardMarkup(row_width=1)

btn_quiz_option_1 = InlineKeyboardMarkup(text="1)", callback_data="btn_quiz_option_1")
btn_quiz_option_2 = InlineKeyboardMarkup(text="2)", callback_data="btn_quiz_option_2")
btn_main_back = InlineKeyboardMarkup(text="🔙 Назад", callback_data="btn_main_back")

quiz_menu.insert(btn_quiz_option_1)
quiz_menu.insert(btn_quiz_option_2)
quiz_menu.insert(btn_main_back)

# Виды викторины

# --- Python меню ---

main_menu = InlineKeyboardMarkup(row_width=7)

btn_number_1 = InlineKeyboardMarkup(text="№1", callback_data="btn_number_1")
btn_number_2 = InlineKeyboardMarkup(text="№2", callback_data="btn_number_2")
btn_number_3 = InlineKeyboardMarkup(text="№3", callback_data="btn_number_3")
btn_number_4 = InlineKeyboardMarkup(text="№4", callback_data="btn_number_4")
btn_number_5 = InlineKeyboardMarkup(text="№5", callback_data="btn_number_5")
btn_number_6 = InlineKeyboardMarkup(text="№6", callback_data="btn_number_6")
btn_number_7 = InlineKeyboardMarkup(text="№7", callback_data="btn_number_7")
btn_number_8 = InlineKeyboardMarkup(text="№8", callback_data="btn_number_8")
btn_number_9 = InlineKeyboardMarkup(text="№9", callback_data="btn_number_9")
btn_number_10 = InlineKeyboardMarkup(text="№10", callback_data="btn_number_10")
btn_number_11 = InlineKeyboardMarkup(text="№11", callback_data="btn_number_11")
btn_number_12 = InlineKeyboardMarkup(text="№12", callback_data="btn_number_12")
btn_number_13 = InlineKeyboardMarkup(text="№13", callback_data="btn_number_13")
btn_number_14 = InlineKeyboardMarkup(text="№14", callback_data="btn_number_14")
btn_number_15 = InlineKeyboardMarkup(text="№15", callback_data="btn_number_15")
btn_number_16 = InlineKeyboardMarkup(text="№16", callback_data="btn_number_16")
btn_number_17 = InlineKeyboardMarkup(text="№17", callback_data="btn_number_17")
btn_number_18 = InlineKeyboardMarkup(text="№18", callback_data="btn_number_18")
btn_number_19 = InlineKeyboardMarkup(text="№19", callback_data="btn_number_19")
btn_number_20 = InlineKeyboardMarkup(text="№20", callback_data="btn_number_20")
btn_number_21 = InlineKeyboardMarkup(text="№21", callback_data="btn_number_21")
btn_number_22 = InlineKeyboardMarkup(text="№22", callback_data="btn_number_22")
btn_number_23 = InlineKeyboardMarkup(text="№23", callback_data="btn_number_23")
btn_number_24 = InlineKeyboardMarkup(text="№24", callback_data="btn_number_24")
btn_number_25 = InlineKeyboardMarkup(text="№25", callback_data="btn_number_25")
btn_number_26 = InlineKeyboardMarkup(text="№26", callback_data="btn_number_26")

main_menu.insert(btn_number_1)
main_menu.insert(btn_number_2)
main_menu.insert(btn_number_3)
main_menu.insert(btn_number_4)
main_menu.insert(btn_number_5)
main_menu.insert(btn_number_6)
main_menu.insert(btn_number_7)
main_menu.insert(btn_number_8)
main_menu.insert(btn_number_9)
main_menu.insert(btn_number_10)
main_menu.insert(btn_number_11)
main_menu.insert(btn_number_12)
main_menu.insert(btn_number_13)
main_menu.insert(btn_number_14)
main_menu.insert(btn_number_15)
main_menu.insert(btn_number_16)
main_menu.insert(btn_number_17)
main_menu.insert(btn_number_18)
main_menu.insert(btn_number_19)
main_menu.insert(btn_number_20)
main_menu.insert(btn_number_21)
main_menu.insert(btn_number_22)
main_menu.insert(btn_number_23)
main_menu.insert(btn_number_24)
main_menu.insert(btn_number_25)
main_menu.insert(btn_number_26)

# Основы (База) Введение

Menu_BASE_1_lesson = InlineKeyboardMarkup(row_width=4)

btn_BASE_1_lesson_1_theory = InlineKeyboardMarkup(text="1)", callback_data="btn_BASE_1_lesson_1_theory")
btn_BASE_1_lesson_2_theory = InlineKeyboardMarkup(text="2)", callback_data="btn_BASE_1_lesson_2_theory")
btn_BASE_1_lesson_3_theory = InlineKeyboardMarkup(text="3)", callback_data="btn_BASE_1_lesson_3_theory")
btn_BASE_1_lesson_4_theory = InlineKeyboardMarkup(text="4)", callback_data="btn_BASE_1_lesson_4_theory")
btn_BASE_1_lesson_5_theory = InlineKeyboardMarkup(text="5)", callback_data="btn_BASE_1_lesson_5_theory")
btn_BASE_1_lesson_6_theory = InlineKeyboardMarkup(text="6)", callback_data="btn_BASE_1_lesson_6_theory")
btn_BASE_1_lesson_7_theory = InlineKeyboardMarkup(text="7)", callback_data="btn_BASE_1_lesson_7_theory")
btn_BASE_1_lesson_8_theory = InlineKeyboardMarkup(text="8)", callback_data="btn_BASE_1_lesson_8_theory")
btn_BASE_1_lesson_9_theory = InlineKeyboardMarkup(text="9)", callback_data="btn_BASE_1_lesson_9_theory")
btn_BASE_1_lesson_10_theory = InlineKeyboardMarkup(text="10", callback_data="btn_BASE_1_lesson_10_theory")
btn_BASE_1_lesson_11_theory = InlineKeyboardMarkup(text="11)", callback_data="btn_BASE_1_lesson_11_theory")
btn_BASE_1_lesson_12_theory = InlineKeyboardMarkup(text="12)", callback_data="btn_BASE_1_lesson_12_theory")
btn_BASE_1_lesson_13_theory = InlineKeyboardMarkup(text="13)", callback_data="btn_BASE_1_lesson_13_theory")
btn_BASE_1_lesson_14_theory = InlineKeyboardMarkup(text="14)", callback_data="btn_BASE_1_lesson_14_theory")
btn_BASE_1_lesson_15_theory = InlineKeyboardMarkup(text="15)", callback_data="btn_BASE_1_lesson_15_theory")
btn_BASE_1_lesson_16_theory = InlineKeyboardMarkup(text="16)", callback_data="btn_BASE_1_lesson_16_theory")
btn_BASE_1_lesson_17_theory = InlineKeyboardMarkup(text="🔙 Назад", callback_data="btn_BASE_1_lesson_17_theory")


Menu_BASE_1_lesson.insert(btn_BASE_1_lesson_1_theory)
Menu_BASE_1_lesson.insert(btn_BASE_1_lesson_2_theory)
Menu_BASE_1_lesson.insert(btn_BASE_1_lesson_3_theory)
Menu_BASE_1_lesson.insert(btn_BASE_1_lesson_4_theory)
Menu_BASE_1_lesson.insert(btn_BASE_1_lesson_5_theory)
Menu_BASE_1_lesson.insert(btn_BASE_1_lesson_6_theory)
Menu_BASE_1_lesson.insert(btn_BASE_1_lesson_7_theory)
Menu_BASE_1_lesson.insert(btn_BASE_1_lesson_8_theory)
Menu_BASE_1_lesson.insert(btn_BASE_1_lesson_9_theory)
Menu_BASE_1_lesson.insert(btn_BASE_1_lesson_10_theory)
Menu_BASE_1_lesson.insert(btn_BASE_1_lesson_11_theory)
Menu_BASE_1_lesson.insert(btn_BASE_1_lesson_12_theory)
Menu_BASE_1_lesson.insert(btn_BASE_1_lesson_13_theory)
Menu_BASE_1_lesson.insert(btn_BASE_1_lesson_14_theory)
Menu_BASE_1_lesson.insert(btn_BASE_1_lesson_15_theory)
Menu_BASE_1_lesson.insert(btn_BASE_1_lesson_16_theory)
Menu_BASE_1_lesson.insert(btn_BASE_1_lesson_17_theory)

"""2 ступень. "Base" Углубление"""

Menu_UGLUBLENIE = InlineKeyboardMarkup(row_width=1)

btn_UGLUBLENIE_1_part = InlineKeyboardMarkup(text="Углубление часть 1 (Функции)", callback_data="btn_UGLUBLENIE_1_part")
btn_UGLUBLENIE_2_part = InlineKeyboardMarkup(text="Углубление часть 2 (Рекурсия, декораторы +)", callback_data="btn_UGLUBLENIE_2_part")
btn_UGLUBLENIE_3_part = InlineKeyboardMarkup(text="Углубление часть 3 (Библиотеки)", callback_data="btn_UGLUBLENIE_3_part")
btn_UGLUBLENIE_4_part = InlineKeyboardMarkup(text="Углубление часть 4 (ООП)", callback_data="btn_UGLUBLENIE_4_part")

Menu_UGLUBLENIE.insert(btn_UGLUBLENIE_1_part)
Menu_UGLUBLENIE.insert(btn_UGLUBLENIE_2_part)
Menu_UGLUBLENIE.insert(btn_UGLUBLENIE_3_part)
Menu_UGLUBLENIE.insert(btn_UGLUBLENIE_4_part)

# 2.1 ступень. Base часть 1

Menu_UGLUBLENIE_1_part = InlineKeyboardMarkup(row_width=1)

btn_UGLUBLENIE_1_part_1_lesson = InlineKeyboardMarkup(text="Функции. Введение", callback_data="btn_UGLUBLENIE_1_part_1_lesson")
btn_UGLUBLENIE_1_part_2_lesson = InlineKeyboardMarkup(text="Возвращение значений из функций", callback_data="btn_UGLUBLENIE_1_part_2_lesson")
btn_UGLUBLENIE_1_part_3_lesson = InlineKeyboardMarkup(text="Функции: Области видимости переменных", callback_data="btn_UGLUBLENIE_1_part_3_lesson")
btn_UGLUBLENIE_1_part_4_lesson = InlineKeyboardMarkup(text="Функции: Передача аргументов", callback_data="btn_UGLUBLENIE_1_part_4_lesson")
btn_UGLUBLENIE_1_part_5_lesson = InlineKeyboardMarkup(text="Функции с переменным числом аргументов", callback_data="btn_UGLUBLENIE_1_part_5_lesson")
btn_UGLUBLENIE_1_part_6_lesson = InlineKeyboardMarkup(text="Вложенные функции", callback_data="btn_UGLUBLENIE_1_part_6_lesson")
btn_UGLUBLENIE_1_part_7_lesson = InlineKeyboardMarkup(text="Лямбда-функции, filter, map, all, any, zip", callback_data="btn_UGLUBLENIE_1_part_7_lesson")

Menu_UGLUBLENIE_1_part.insert(btn_UGLUBLENIE_1_part_1_lesson)
Menu_UGLUBLENIE_1_part.insert(btn_UGLUBLENIE_1_part_2_lesson)
Menu_UGLUBLENIE_1_part.insert(btn_UGLUBLENIE_1_part_3_lesson)
Menu_UGLUBLENIE_1_part.insert(btn_UGLUBLENIE_1_part_4_lesson)
Menu_UGLUBLENIE_1_part.insert(btn_UGLUBLENIE_1_part_6_lesson)
Menu_UGLUBLENIE_1_part.insert(btn_UGLUBLENIE_1_part_7_lesson)

# 2.2 ступень. Base часть 2

Menu_UGLUBLENIE_2_part = InlineKeyboardMarkup(row_width=1)

btn_UGLUBLENIE_2_part_1_lesson = InlineKeyboardMarkup(text="Рекурсия", callback_data="btn_UGLUBLENIE_2_part_1_lesson")
btn_UGLUBLENIE_2_part_2_lesson = InlineKeyboardMarkup(text="Рекурсивный обход файлов", callback_data="btn_UGLUBLENIE_2_part_2_lesson")
btn_UGLUBLENIE_2_part_3_lesson = InlineKeyboardMarkup(text='Строка документирования "Docstring"', callback_data="btn_UGLUBLENIE_2_part_3_lesson")
btn_UGLUBLENIE_2_part_4_lesson = InlineKeyboardMarkup(text="Аннотации", callback_data="btn_UGLUBLENIE_2_part_4_lesson")
btn_UGLUBLENIE_2_part_5_lesson = InlineKeyboardMarkup(text="Замыкания", callback_data="btn_UGLUBLENIE_2_part_5_lesson")
btn_UGLUBLENIE_2_part_6_lesson = InlineKeyboardMarkup(text="Декораторы", callback_data="btn_UGLUBLENIE_2_part_6_lesson")

Menu_UGLUBLENIE_2_part.insert(btn_UGLUBLENIE_2_part_1_lesson)
Menu_UGLUBLENIE_2_part.insert(btn_UGLUBLENIE_2_part_2_lesson)
Menu_UGLUBLENIE_2_part.insert(btn_UGLUBLENIE_2_part_3_lesson)
Menu_UGLUBLENIE_2_part.insert(btn_UGLUBLENIE_2_part_4_lesson)
Menu_UGLUBLENIE_2_part.insert(btn_UGLUBLENIE_2_part_5_lesson)
Menu_UGLUBLENIE_2_part.insert(btn_UGLUBLENIE_2_part_6_lesson)

# 2.3 ступень. Base часть 3

Menu_UGLUBLENIE_3_part = InlineKeyboardMarkup(row_width=1)

btn_UGLUBLENIE_3_part_1_lesson = InlineKeyboardMarkup(text="Потоковый ввод sys.stdin", callback_data="btn_UGLUBLENIE_3_part_1_lesson")
btn_UGLUBLENIE_3_part_2_lesson = InlineKeyboardMarkup(text="Встроенные модули", callback_data="btn_UGLUBLENIE_3_part_2_lesson")
btn_UGLUBLENIE_3_part_3_lesson = InlineKeyboardMarkup(text="Модуль collections", callback_data="btn_UGLUBLENIE_3_part_3_lesson")
btn_UGLUBLENIE_3_part_4_lesson = InlineKeyboardMarkup(text="Библиотека PIL (Python Image Library)", callback_data="btn_UGLUBLENIE_3_part_4_lesson")

Menu_UGLUBLENIE_3_part.insert(btn_UGLUBLENIE_3_part_1_lesson)
Menu_UGLUBLENIE_3_part.insert(btn_UGLUBLENIE_3_part_2_lesson)
Menu_UGLUBLENIE_3_part.insert(btn_UGLUBLENIE_3_part_3_lesson)
Menu_UGLUBLENIE_3_part.insert(btn_UGLUBLENIE_3_part_4_lesson)

# 2.4 ступень. Base часть 4

Menu_UGLUBLENIE_4_part = InlineKeyboardMarkup(row_width=1)

btn_UGLUBLENIE_4_part_1_lesson = InlineKeyboardMarkup(text="Введение в ООП", callback_data="btn_UGLUBLENIE_4_part_1_lesson")
btn_UGLUBLENIE_4_part_2_lesson = InlineKeyboardMarkup(text="ООП: Полиморфизм", callback_data="btn_UGLUBLENIE_4_part_2_lesson")
btn_UGLUBLENIE_4_part_3_lesson = InlineKeyboardMarkup(text="ООП: Определение операторов", callback_data="btn_UGLUBLENIE_4_part_3_lesson")
btn_UGLUBLENIE_4_part_4_lesson = InlineKeyboardMarkup(text="ООП: Наследование", callback_data="btn_UGLUBLENIE_4_part_4_lesson")

Menu_UGLUBLENIE_4_part.insert(btn_UGLUBLENIE_4_part_1_lesson)
Menu_UGLUBLENIE_4_part.insert(btn_UGLUBLENIE_4_part_2_lesson)
Menu_UGLUBLENIE_4_part.insert(btn_UGLUBLENIE_4_part_3_lesson)
Menu_UGLUBLENIE_4_part.insert(btn_UGLUBLENIE_4_part_4_lesson)

""" Секции теорий в уроках """

# Base; урок: Введение; 9-ая теория

Menu_BASE_1_lesson_9_theory = InlineKeyboardMarkup(row_width=5)

btn_BASE_1_lesson_9_theory_1_section = InlineKeyboardMarkup(text="1)", callback_data="btn_BASE_1_lesson_9_theory_1_section")
btn_BASE_1_lesson_9_theory_2_section = InlineKeyboardMarkup(text="2)", callback_data="btn_BASE_1_lesson_9_theory_2_section")
btn_BASE_1_lesson_9_theory_3_section = InlineKeyboardMarkup(text="3)", callback_data="btn_BASE_1_lesson_9_theory_3_section")
btn_BASE_1_lesson_9_theory_4_section = InlineKeyboardMarkup(text="4)", callback_data="btn_BASE_1_lesson_9_theory_4_section")
btn_BASE_1_lesson_9_theory_5_section = InlineKeyboardMarkup(text="5)", callback_data="btn_BASE_1_lesson_9_theory_5_section")
btn_BASE_1_lesson_9_theory_6_section = InlineKeyboardMarkup(text="🔙 Назад", callback_data="btn_BASE_1_lesson_9_theory_6_section")

Menu_BASE_1_lesson_9_theory.insert(btn_BASE_1_lesson_9_theory_1_section)
Menu_BASE_1_lesson_9_theory.insert(btn_BASE_1_lesson_9_theory_2_section)
Menu_BASE_1_lesson_9_theory.insert(btn_BASE_1_lesson_9_theory_3_section)
Menu_BASE_1_lesson_9_theory.insert(btn_BASE_1_lesson_9_theory_4_section)
Menu_BASE_1_lesson_9_theory.insert(btn_BASE_1_lesson_9_theory_5_section)
Menu_BASE_1_lesson_9_theory.insert(btn_BASE_1_lesson_9_theory_6_section)

# Base; урок: Введение; 13-ая теория

Menu_BASE_1_lesson_13_theory = InlineKeyboardMarkup(row_width=2)

btn_BASE_1_lesson_13_theory_1_section = InlineKeyboardMarkup(text="1)", callback_data="btn_BASE_1_lesson_13_theory_1_section")
btn_BASE_1_lesson_13_theory_2_section = InlineKeyboardMarkup(text="2)", callback_data="btn_BASE_1_lesson_13_theory_2_section")
btn_BASE_1_lesson_13_theory_3_section = InlineKeyboardMarkup(text="3)", callback_data="btn_BASE_1_lesson_13_theory_3_section")
btn_BASE_1_lesson_13_theory_4_section = InlineKeyboardMarkup(text="4)", callback_data="btn_BASE_1_lesson_13_theory_4_section")
btn_BASE_1_lesson_13_theory_5_section = InlineKeyboardMarkup(text="🔙 Назад", callback_data="btn_BASE_1_lesson_13_theory_5_section")

Menu_BASE_1_lesson_13_theory.insert(btn_BASE_1_lesson_13_theory_1_section)
Menu_BASE_1_lesson_13_theory.insert(btn_BASE_1_lesson_13_theory_2_section)
Menu_BASE_1_lesson_13_theory.insert(btn_BASE_1_lesson_13_theory_3_section)
Menu_BASE_1_lesson_13_theory.insert(btn_BASE_1_lesson_13_theory_4_section)
Menu_BASE_1_lesson_13_theory.insert(btn_BASE_1_lesson_13_theory_5_section)
