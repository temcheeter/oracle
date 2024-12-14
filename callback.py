from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery
import keyboard as kb
from config import channel


rt = Router()


@rt.callback_query(F.data == 'check_sub')
async def first_check_sub(call: CallbackQuery, bot: Bot):
    user_channel_status = await bot.get_chat_member(chat_id=channel, user_id=call.from_user.id)
    if user_channel_status.status != 'left':
        await call.answer('Спасибо за подписку!')
        await call.message.answer('Поехали💥?', reply_markup=kb.go_kb)
    else:
        await call.answer('Для начала подпишись на наш канал')


@rt.callback_query(F.data == 'go')
async def first_prediction(call: CallbackQuery):
    await prediction.predict(call.from_user.id)
