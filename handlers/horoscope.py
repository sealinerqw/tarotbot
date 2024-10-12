from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards import horoscope_get_sign, answer_keyboard
from helpers import parser


router = Router()


@router.callback_query(F.data == "horoscope")
async def call_horoscope(callback: CallbackQuery):
    await callback.message.answer(text="Выберите ваш знак зодиака: ", reply_markup=horoscope_get_sign.build())
    await callback.answer()


@router.callback_query(F.data == "general_horoscope")
async def send_general_horoscope(callback: CallbackQuery):
    await callback.message.answer(f"Гороскоп для всех:\n"
                                  f"{parser.parse_general_horoscope()}")
    await callback.answer()


@router.callback_query(F.data.startswith("sign_"))
async def send_sign_horoscope(callback: CallbackQuery):
    user_sign = str(callback.data).split("_")[1]
    await callback.message.answer(f"Гороскоп для {user_sign}:\n"
                                  f"{parser.parse_sign_horoscope(user_sign)}",
                                  reply_markup=answer_keyboard.build())
    await callback.answer()
