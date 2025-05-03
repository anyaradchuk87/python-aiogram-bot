from aiogram import Bot, Dispatcher, types
from aiogram.types import BotCommand
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from aiogram.types.web_app_info import WebAppInfo
from aiogram.filters import Command, Text
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
# TOKEN="7875509094:AAEv-d5n-s8_mtRFVcmb2PhHzz4-c-WMI7c"

bot = Bot(token=TOKEN)
dp = Dispatcher()

game_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎮 Почати гру")],
        [KeyboardButton(text="🔄 Перезапустити гру")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("👋 Привіт! Обери опцію:", reply_markup=game_menu)

@dp.message(Text("🎮 Почати гру"))
async def start_game(message: types.Message):
    await message.answer("🎯 Гру розпочато!")

@dp.message(Text("🔄 Перезапустити гру"))
async def restart_game(message: types.Message):
    await message.answer("♻️ Гру перезапущено!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())