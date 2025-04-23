from aiogram import Bot, Dispatcher, types
from aiogram.types import BotCommand
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from aiogram.types.web_app_info import WebAppInfo
from aiogram.filters import Command
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="ℹ️ Info")],
            [KeyboardButton(text="❓ Help")]
        ],
        resize_keyboard=True
    )
    # Просто надсилаємо клавіатуру, без тексту
    await message.answer(text="Виберіть опцію нижче:", reply_markup=markup)

@dp.message()
async def handle_buttons(message: types.Message):
    if message.text == "ℹ️ Info":
        await message.answer("Це бот для демонстрації меню.")
    elif message.text == "❓ Help":
        await message.answer("Натисніть кнопку, щоб дізнатися більше.")
    else:
        await message.answer("Будь ласка, використовуйте кнопки меню.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())