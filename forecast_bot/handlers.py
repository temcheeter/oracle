from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from aiogram.types.input_file import BufferedInputFile
from aiogram.enums import ChatAction
import keyboard as kb
from config import channel
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from prediction import predict


rt = Router()


class Form(StatesGroup):
    go = State()


@rt.callback_query(F.data == 'check_sub')
async def first_check_sub(call: CallbackQuery, bot: Bot):
    response = await sub_checker(call.message, bot)
    if response:
        await call.answer('Спасибо за подписку!')
        await call.message.answer('Поехали?', reply_markup=kb.go_kb)
    else:
        await call.message.answer('Тебе всё ещё нет у нас на канале😢')


async def sub_checker(msg:Message, bot: Bot):
    user_channel_status = await bot.get_chat_member(chat_id=channel, user_id=msg.from_user.id)
    if user_channel_status.status == 'left':
        return False, 'Для начала подпишись на наш канал'
    else:
        return True


@rt.callback_query(F.data == 'go')
async def first_prediction(call: CallbackQuery, state: FSMContext):
    await call.message.answer('Ты можешь ввести дату в виде число-буквенного значения (например 17 октября), а '
                              'я тебе отправлю предсказание связаное с этой датой🤗')
    await call.message.answer('Напиши дату:')
    await state.set_state(Form.go)


@rt.message(Form.go)
async def forecast(msg: Message, bot: Bot, state: FSMContext):
    response = await sub_checker(msg, bot)
    if response:
        txt = msg.text
        try:
            if txt == '777':
                await msg.bot.send_chat_action(msg.from_user.id, action=ChatAction.UPLOAD_PHOTO)
                await msg.answer_photo(
                    BufferedInputFile(
                        await predict(txt),
                        'forecast.png'
                    )
                )
                await msg.answer(
                    '```AVTO268``` ', parse_mode='MARKDOWN', reply_markup=kb.main_kb)
            elif txt == '1 апреля':
                await msg.bot.send_chat_action(msg.from_user.id, action=ChatAction.UPLOAD_PHOTO)
                await msg.answer_photo(
                    BufferedInputFile(
                        await predict(txt),
                        'forecast.png'
                    )
                )
                await msg.answer('```750at```', parse_mode='MARKDOWN', reply_markup=kb.main_kb)
            else:
                day, month = txt.split(' ')[0], txt.split(' ')[1]
                if month == 'января' and 0 < int(day) < 32:
                    await msg.bot.send_chat_action(msg.from_user.id, action=ChatAction.UPLOAD_PHOTO)
                    await msg.answer_photo(
                        BufferedInputFile(
                            await predict(txt),
                            'forecast.png'
                        ),
                        reply_markup=kb.main_kb
                    )
                else:
                    await msg.answer('Тебе пока что доступен только январь😢', reply_markup=kb.main_kb)
            await state.clear()
        except:
            await msg.answer('Что-то пошло не так, попробуй ещё раз', reply_markup=ReplyKeyboardRemove())
            await state.set_state(Form.go)
    else:
        await msg.answer('Подпишись на нас снова, пожалуйста🥺', reply_markup=kb.check_sub_kb)

@rt.message(F.text == 'Мне повезёт!🥳')
async def forecast_(msg: Message, state: FSMContext):
    await msg.answer('Введи свою самую сокральную дату🔮:')
    await state.set_state(Form.go)
