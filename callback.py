from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
import keyboard as kb
from config import channel
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from prediction import predict


rt = Router()


@rt.callback_query(F.data == 'check_sub')
async def first_check_sub(call: CallbackQuery, bot: Bot):
    user_channel_status = await bot.get_chat_member(chat_id=channel, user_id=call.from_user.id)
    if user_channel_status.status != 'left':
        await call.answer('Спасибо за подписку!')
        await call.message.answer('Поехали💥?', reply_markup=kb.go_kb)
    else:
        await call.answer('Для начала подпишись на наш канал')


class Form(StatesGroup):
    date = State()


@rt.callback_query(F.data == 'go')
async def first_prediction(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Ты можешь ввести дату в виде число-буквенного значения (например 17 октября), а '
                              'я тебе отправлю предсказание связаное с этой датой')
    await call.message.answer('Напиши дату:')
    await state.set_state(Form.date)


@rt.message(Form.date)
async def date(msg: Message, state: FSMContext):
    try:
        if msg.text == '777':
            await predict(msg.text)
            await msg.answer(
                '```AVTO268``` ', parse_mode='MARKDOWN')
        elif msg.text == '1 апреля':
            await predict(msg.text)
            await msg.answer('```750at```', parse_mode='MARKDOWN')
        else:
            day, month = msg.text.split(' ')[0], msg.text.split(' ')[1]
            if month == 'января' and 0 < int(day) < 32:
                await predict(msg.text)
            else:
                await msg.answer('Тебе пока что доступен только январь😢')
                await state.clear()
    except:
        await msg.answer('Что-то пошло не так')
