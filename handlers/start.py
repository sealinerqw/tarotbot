from aiogram import Router, F, dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from tarotbot.keyboards import start_select_options
router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Здравствуйте!\nЯ - ТароБот!\nВыберите услугу:", reply_markup=start_select_options.build())


@router.callback_query(F.data == "menu")
async def callback_back(callback: CallbackQuery):
    await callback.message.answer("Выберите услугу:", reply_markup=start_select_options.build())
    await callback.answer()


