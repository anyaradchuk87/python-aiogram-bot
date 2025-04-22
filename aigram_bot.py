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
        keyboard=[[KeyboardButton(text="Open web", web_app=WebAppInfo(url="https://anyaradchuk87.github.io/game_telegram/"))]],
        resize_keyboard=True
    )
    await message.answer("hello my friend", reply_markup=markup)

@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer("Це бот з кнопкою для відкриття гри у веб-застосунку.")

async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Запустити бота"),
        BotCommand(command="help", description="Допомога та опис"),
    ]
    await bot.set_my_commands(commands)

async def main():
    await set_bot_commands(bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())