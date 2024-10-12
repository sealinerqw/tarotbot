from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu_button = InlineKeyboardButton(text="〰️В главное меню", callback_data="menu")
back_button = InlineKeyboardButton(text="🔙Назад", callback_data="back")

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [menu_button],
    [back_button]
])


def build():
    return keyboard
