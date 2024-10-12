from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

general_button = InlineKeyboardButton(text="🪄 Для всех знаков", callback_data="general_horoscope")
aries_button = InlineKeyboardButton(text="♈ Овен", callback_data="sign_aries")
taurus_button = InlineKeyboardButton(text="♉ Телец", callback_data="sign_taurus")
gemini_button = InlineKeyboardButton(text="♊ Близнецы", callback_data="sign_gemini")
cancer_button = InlineKeyboardButton(text="♋ Рак", callback_data="sign_cancer")
leo_button = InlineKeyboardButton(text="♌ Лев", callback_data="sign_leo")
virgo_button = InlineKeyboardButton(text="♍ Дева", callback_data="sign_virgo")
libra_button = InlineKeyboardButton(text="♎ Весы", callback_data="sign_libra")
scorpio_button = InlineKeyboardButton(text="♏ Скорпион", callback_data="sign_scorpio")
sagittarius_button = InlineKeyboardButton(text="♐ Стрелец", callback_data="sign_sagittarius")
capricorn_button = InlineKeyboardButton(text="♑ Козерог", callback_data="sign_capricorn")
aquarius_button = InlineKeyboardButton(text="♒ Водолей", callback_data="sign_aquarius")
pisces_button = InlineKeyboardButton(text="♓ Рыбы", callback_data="sign_pisces")
back_button = InlineKeyboardButton(text="🔙Назад", callback_data="back")

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [general_button],
    [aries_button, taurus_button, gemini_button],
    [cancer_button, leo_button, virgo_button],
    [libra_button, scorpio_button, sagittarius_button],
    [capricorn_button, aquarius_button, pisces_button],
    [back_button]
])


def build():
    return keyboard
