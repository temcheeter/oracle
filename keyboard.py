from aiogram.utils.keyboard import(InlineKeyboardMarkup,
                                   InlineKeyboardButton,
                                   ReplyKeyboardMarkup,
                                   KeyboardButton)


check_sub_kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Подписаться🦁', url='https://t.me/+147yTrTQxyQ0MjU6')
        ],
        [
            InlineKeyboardButton(text='Проверить подписку✅', callback_data='check_sub')
        ]
    ]
)

go_kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Начать💥!', callback_data='go')
        ]
    ]
)
