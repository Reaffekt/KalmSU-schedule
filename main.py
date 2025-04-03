import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command
from aiogram.types.web_app_info import WebAppInfo

TOKEN = "7293964428:AAEAzmo9lgcA8yXAPdIjNxfKUDhUaQyPJ-Y"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    web_app_button = KeyboardButton(text="Открыть мини-приложение", web_app=WebAppInfo(url="https://your-web-app-url.com"))

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(web_app_button)

    await message.answer("Привет! Нажми на кнопку, чтобы открыть мини-приложение.", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
