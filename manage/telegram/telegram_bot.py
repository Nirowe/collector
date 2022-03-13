from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher

from config import settings
from states import ChannelStates

bot = Bot(token=settings.telegram.bot_token)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(state='*', commands=['add'])
async def process_setstate_command(message: types.Message):
    """ Выставляет режим ADD при команде /add """
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(ChannelStates.all()[0])
    await bot.send_message(message.from_user.id, text='Пиши по одному каналы, которые хочешь добавить')


@dp.message_handler(state='*', commands=['delete'])
async def process_setstate_command(message: types.Message):
    """ Выставляет режим DELETE при команде /delete """
    state = dp.current_state(user=message.from_user.id)
    await state.set_state(ChannelStates.all()[1])
    await bot.send_message(message.from_user.id, text='Пиши по одному каналы, которые хочешь удалить')


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, text="Привет! Это бот для того, чтобы ты мог собрать новости из нескольких каналов в одном месте")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await bot.send_message(message.from_user.id, text="TODO")


@dp.message_handler(state=ChannelStates.ADD[0])
async def add_state_case_met(message: types.Message):
    """ Добавление каналов """
    await message.reply(f"add {message.text}", reply=False)


@dp.message_handler(state=ChannelStates.DELETE[0])
async def delete_state_case_met(message: types.Message):
    """ Удаление каналов """
    await message.reply(f"delete {message.text}", reply=False)


@dp.message_handler()
async def echo_message(message: types.Message):
    """ Работает, если не выбран режим работы с каналами """
    await bot.send_message(message.from_user.id, text="Напиши /add или /delete чтобы добавлять или удалять каналы")



