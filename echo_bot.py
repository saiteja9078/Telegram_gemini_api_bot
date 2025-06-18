from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
import asyncio
import google.generativeai as genai
import os
from dotenv import load_dotenv
from aiogram.client.default import DefaultBotProperties


load_dotenv()
TOKEN = os.getenv("TELEBOT_BOT_TOKEN")
# TOKEN = "7663115421:AAEhVK9XnqY2yBHT7ytDZNDXNa005qlNbuM"

# Initialize Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello! I am Shanks , AI powered pirate.")
@dp.message()
async def gemini_reply(message: Message):
    user_input = message.text
    try:
        response = model.generate_content(f"You are Shanks an ai powered pirate act like him,just respond to that prompt as if you are shanks and this is prompt:{user_input}")
        answer = response.text
    except Exception as e:
        answer = f"❌ Gemini API error: {e}"
    await message.answer(answer)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
