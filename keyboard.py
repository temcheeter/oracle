from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton


check_sub_kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Подписаться🦁', url='https://t.me/+-JBJ5OD-_oUxMDFi')
        ],
        [
            InlineKeyboardButton(text='Проверить подписку✅', callback_data='check_sub')
        ]
    ]
)

