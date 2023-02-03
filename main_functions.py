import logging
import asyncio
import json
import markups as nav
from contextlib import suppress
from aiogram import Dispatcher, Bot, types
from aiogram.utils.exceptions import MessageCantBeDeleted, MessageToDeleteNotFound
from config import *
from other_functions import *

# Инициализируем бота
bot = Bot(token=BOT_TOKEN)  # Объект класса Bot
dp = Dispatcher(bot)  # Создали объект класса Dispatcher (нужен для хэндлеров)

# Включаем логирование, чтобы не пропустить важные сообщения красного цвета
logging.basicConfig(level=logging.INFO)


with open('tasks.json', encoding='utf-8') as json_file:
    WHOLE_THEORY = json.loads(json_file.read())  # Переменная, в которой хранится вся теория курса в формате JSON


class Message:
    """
     Класс работает с сообщениями:
     1) способен удалять сообщения
     2) способен печатать информацию, теорию, викторины и т.п. """

    answered_the_quiz = []

    @staticmethod
    async def delete_messages(message: types.Message, sleep_time: int = 0):
        """ Метод, способный удалять большие объекты: картинки, викторины и другое """
        await asyncio.sleep(sleep_time)  # Можно настроить время удаления
        with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
            await message.delete()

    @staticmethod
    async def del_last_message(human_id):
        """ Метод, удаляющий предыдущее сообщение """
        await bot.delete_message(human_id.from_user.id, human_id.message.message_id)

    async def del_output_text(self, text, human_id, menu=None):
        """ Метод, удаляющий предыдущее сообщение и печатающий текст с меню/без меню """
        await self.del_last_message(human_id)  # Удаляем предыдущее сообщение
        if menu is None:  # Если меню нет
            await bot.send_message(human_id.from_user.id, text, parse_mode="HTML")  # То выводим текст
        else:  # Иначе выводим текст с меню
            await bot.send_message(human_id.from_user.id, text, reply_markup=eval(f"nav.{menu}"), parse_mode="HTML")

    @staticmethod
    async def output_text(text, human_id, menu=None):
        """ Метод, печатающий текст с меню/без меню """
        if menu is None:  # Если меню нет
            await bot.send_message(human_id.from_user.id, text, parse_mode="HTML", disable_web_page_preview=True)  # То выводим текст
        else:  # Иначе выводим текст с меню
            await bot.send_message(human_id.from_user.id, text, reply_markup=eval(f"nav.{menu}"), parse_mode="HTML")


ms = Message()  # Экземпляр класса Message

"""

<b> ... </b> - Жирный текст

<i> ... </i> - Курсивный текст

<u> ... </u> - Подчеркнутый текст

<del> ... </del> - Зачеркнутый текст

<code> ... </code> - моно-шрифт

&lt;html&gt;Вопрос&lt;/html&gt; -> <html>Вопрос</html> ->

<a href='https://www.python.org/'>здесь</a>    -> ссылка

Чтобы вставить HTML код в сообщение блога, чтобы он не интерпретировался 
как команды HTML, нужно все символы < заменить на &lt;, а символы > на &gt;

"""
