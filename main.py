from aiogram import executor
from main_functions import *


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await ms.output_text(f'Здравствуйте, {message.from_user.first_name})\nЯ бот-платочек. Ты можешь писать, '
                         f'все что хочешь. Я обязательно выслушаю тебя. Также я могу поделится с тобой полезными статьями. '
                         f'Для информации введите /info.', message)


@dp.message_handler(commands=['write'])
async def write(message: types.Message):
    await ms.output_text(f'Пиши, для остановки напиши /stop', message)


@dp.message_handler(commands=['stop'])
async def stop(message: types.Message):
    await ms.output_text(f'Спасибо, что поделился со мной удачи) /link - обязательно прочитай материалы, тебе точно '
                         f'понравится', message)


@dp.message_handler(commands=['info'])
async def info(message: types.Message):
    await ms.output_text(f'Напиши /write и пиши, что душе угодно. Если хочешь получить материалы пиши /link\n/info - '
                         f'вернет тебя назад в будущем.', message)


@dp.message_handler(commands=['link'])
async def link(message: types.Message):
    await ms.output_text("<a href='https://youtu.be/Pqd9eM_cqi8'>про выгорание</a>\n"
                         "<a href='https://youtu.be/2QSN2KmE7Wk'>как быстро справится со стресом</a>\n"
                         "Желаю всего Вам хорошего!", message)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
