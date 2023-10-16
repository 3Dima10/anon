import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

################################
#--------------Log-------------#
################################
API_TOKEN = str(input("Ведите токен бота: "))
USER_ID = input("Ведите ID собеседника: ")
IM_ID = input("Ведите свой ID: ")


#######################################
#--------------Config Bot-------------#
#######################################

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.chat.id, "start run")

@dp.message_handler(content_types=['text'])
async def text(message):
    user = message.from_user.id
    if int(user) == int(IM_ID):
        await bot.send_message(USER_ID, message.text)
    else:
        await bot.send_message(IM_ID, message.text)



# Запуск бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
