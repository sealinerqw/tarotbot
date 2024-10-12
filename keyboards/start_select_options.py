from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

horoscopeButton = InlineKeyboardButton(text="✨Гороскоп", callback_data="horoscope")
tarotButton = InlineKeyboardButton(text="🔮Расклад Таро (Премиум)", callback_data="tarot")
tarotDailyButton = InlineKeyboardButton(text="Карта дня", callback_data="tarotDaily")
premiumButton = InlineKeyboardButton(text="Купить премиум подписку", callback_data="premium")

keyboard = InlineKeyboardMarkup(inline_keyboard=[[horoscopeButton],
                                 [tarotButton],
                                 [tarotDailyButton],
                                 [premiumButton]
])


def build():
    return keyboard
