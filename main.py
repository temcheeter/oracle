from aiogram import Dispatcher, Bot, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import *
import keyboard as kb
import asyncio
from callback import rt as call_rt

bot = Bot(token)
dp = Dispatcher()
dp.include_routers(call_rt)

@dp.message(CommandStart())
async def start(msg: Message):
    await msg.answer('А ты подписан на наш канал🤨?', reply_markup=kb.check_sub_kb)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
