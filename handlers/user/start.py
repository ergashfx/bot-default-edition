from loader import dp
from aiogram.types import Message


@dp.message_handler(commands="start")
async def send(message: Message):
    await message.answer("*Salom*",
                         parse_mode="markdown")

