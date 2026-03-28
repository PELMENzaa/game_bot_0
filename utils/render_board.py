from telegram import InlineKeyboardButton, InlineKeyboardMarkup
def render_board(lst):
    # игра продолжается
        keyboard = [
            [
                InlineKeyboardButton(lst[0], callback_data="0"),
                InlineKeyboardButton(lst[1], callback_data="1"),
                InlineKeyboardButton(lst[2], callback_data="2"),
            ],
            [
                InlineKeyboardButton(lst[3], callback_data="3"),
                InlineKeyboardButton(lst[4], callback_data="4"),
                InlineKeyboardButton(lst[5], callback_data="5"),
            ],
            [
                InlineKeyboardButton(lst[6], callback_data="6"),
                InlineKeyboardButton(lst[7], callback_data="7"),
                InlineKeyboardButton(lst[8], callback_data="8"),
            ],
            [   InlineKeyboardButton('меню', callback_data='menu')
            ]
        ]
        markup = InlineKeyboardMarkup(keyboard)