from aiogram import F
from random import randint
from aiogram.types import Message
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardRemove
from key_boards import start_keyboard as sk, accept_keyboard as ak
from users_data import users, show_stat as ss

from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

game_cases = ['Камень', 'Ножницы', 'Бумага']
game_win_con = {
    'Камень': 'Ножницы',
    'Ножницы': 'Бумага',
    'Бумага': 'Камень',
}


@dp.message(Command(commands=['start']))
@dp.message(F.text == 'start')
async def start_cmd(message: Message):
    if not users.get(message.from_user.id, False):
        users[message.from_user.id] = {
            'wins': 0,
            'tries': 0,
            'loses': 0,
            'draws': 0,
            'game_state': False,
        }
    if not users[message.from_user.id]['game_state']:
        await message.answer(text=os.getenv('INFO_TEMP'), reply_markup=sk)
    else:
        await message.answer("Подожди пока доиграем!")


@dp.message(F.text == "/help")
@dp.message(F.text == 'help')
async def help_cmd(message: Message):
    if not users[message.from_user.id]['game_state']:
        await message.answer(text=os.getenv('HELP_TEMP'), reply_markup=sk)
    else:
        await message.answer("Подожди пока доиграем!")


@dp.message(F.text == "Не хочу!")
async def refuse_case(message: Message):
    if not users[message.from_user.id]['game_state']:
        await message.answer(text=os.getenv('REFUSE_TEMP'), reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer("Вообще-то мы уже играем...")


@dp.message(F.text == "Давай!")
async def lets_go_case(message: Message):
    if not users[message.from_user.id]['game_state']:
        users[message.from_user.id]['game_state'] = True
        await message.answer(text=os.getenv('ACCEPT_TEMP'), reply_markup=ak)
    else:
        await message.answer("Да мы уже в игре...")


@dp.message(F.text == "stat")
@dp.message(F.text == "/stat")
async def show_stat(message: Message):
    if not users[message.from_user.id]['game_state']:
        stat = ss(message.from_user.id)
        await message.answer(text=stat)
    else:
        await message.answer("Подожди пока доиграем!")


@dp.message(F.text == "Камень")
@dp.message(F.text == "Ножницы")
@dp.message(F.text == "Бумага")
async def game_case(message: Message):
    if users[message.from_user.id]['game_state']:
        new_indx = randint(0, 2)
        if game_win_con[message.text] == game_cases[new_indx]:
            users[message.from_user.id]['game_state'] = False
            users[message.from_user.id]['wins'] += 1
            users[message.from_user.id]['tries'] += 1
            await message.reply("Вы победили!")
        elif message.text == game_cases[new_indx]:
            users[message.from_user.id]['game_state'] = False
            users[message.from_user.id]['draws'] += 1
            users[message.from_user.id]['tries'] += 1
            await message.reply("Похоже, что у нас ничья!")
        else:
            users[message.from_user.id]['game_state'] = False
            users[message.from_user.id]['loses'] += 1
            users[message.from_user.id]['tries'] += 1
            await message.reply("К сожалению, проигрыш!")
        await message.answer("Хотите сыграть еще?", reply_markup=sk)
    else:
        await message.answer("Не торопитесь! Мы ведь не начали!")


@dp.message()
async def casual_talk(message: Message):
    await message.reply("Я не понимаю... \_[Х]_[Х]__/")


dp.run_polling(bot)
