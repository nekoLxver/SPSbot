from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

lets_go_btn = KeyboardButton(text="Давай!")
refuse_btn = KeyboardButton(text="Не хочу!")

stone_case = KeyboardButton(text='Камень')
paper_case = KeyboardButton(text='Ножницы')
scissors_case = KeyboardButton(text='Бумага')

accept_keyboard = ReplyKeyboardBuilder().row(stone_case, paper_case, scissors_case, width=3).as_markup(resize_keyboard=True)
start_keyboard = ReplyKeyboardBuilder().row(lets_go_btn, refuse_btn, width=2).as_markup(resize_keyboard=True)
