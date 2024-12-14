from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery
from config import channel


rt = Router()


@rt.callback_query(F.data == 'check_sub')
async def check_sub(call: CallbackQuery, bot: Bot):
    user_channel_status = await bot.get_chat_member(chat_id=channel, user_id=call.from_user.id)
    if user_channel_status.status != 'left':
        await call.answer('Спасибо за подписку!')
    else:
        await call.answer('Для начала подпишись на наш канал')