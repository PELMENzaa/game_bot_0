from telegram import InlineKeyboardButton, Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from states import TICTACTOE
from menu import start


async def tictactoe_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["i"] = '❌'
    query = update.callback_query  # Полная информация о нажатой кнопке
    await query.answer()  # отвечаем на запрос
    context.user_data["lst"] = [
        "⬜",
        "⬜",
        "⬜",
        "⬜",
        "⬜",
        "⬜",
        "⬜",
        "⬜",
        "⬜",
    ]
    lst = context.user_data["lst"]  # Получаем список из user_data
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
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="ход крестиков",
        reply_markup=markup,
    )
    return TICTACTOE


async def tictactoe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    i = context.user_data["i"]
    if i == '❌':
        context.user_data["i"] = '⭕'
    else:
        context.user_data["i"] = '❌'
    query = update.callback_query
    await query.answer()

    nomer_knopki = int(query.data)
    lst = context.user_data["lst"]
    if lst[nomer_knopki] == '⬜':
        lst[nomer_knopki] = i
    else:
        if i == '❌':
            context.user_data["i"] = '⭕'
        else:
            context.user_data["i"] = '❌'
        i = context.user_data['i']
    # победа
    if lst[0] == lst[1] == lst[2] == '❌':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Крестики победили!",
        )
        return await start(update, context)
    if lst[3] == lst[4] == lst[5] == '❌':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Крестики победили!",
        )
        return await start(update, context)
    if lst[6] == lst[7] == lst[8] == '❌':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Крестики победили!",
        )
        return await start(update, context)
    if lst[0] == lst[3] == lst[6] == '❌':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Крестики победили!",
        )
        return await start(update, context)
    if lst[1] == lst[4] == lst[7] == '❌':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Крестики победили!",
        )
        return await start(update, context)
    if lst[2] == lst[5] == lst[8] == '❌':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Крестики победили!",
        )
        return await start(update, context)
    if lst[0] == lst[4] == lst[8] == '❌':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Крестики победили!",
        )
        return await start(update, context)
    if lst[2] == lst[4] == lst[6] == '❌':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Крестики победили!",
        )
        return await start(update, context)
    if lst[0] == lst[1] == lst[2] == '⭕':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Нолики победили!",
        )
        return await start(update, context)
    if lst[3] == lst[4] == lst[5] == '⭕':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Нолики победили!",
        )
        return await start(update, context)
    if lst[6] == lst[7] == lst[8] == '⭕':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Нолики победили!",
        )
        return await start(update, context)
    if lst[0] == lst[3] == lst[6] == '⭕':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Нолики победили!",
        )
        return await start(update, context)
    if lst[1] == lst[4] == lst[7] == '⭕':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Нолики победили!",
        )
        return await start(update, context)
    if lst[2] == lst[5] == lst[8] == '⭕':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Нолики победили!",
        )
        return await start(update, context)
    if lst[0] == lst[4] == lst[8] == '⭕':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Нолики победили!",
        )
        return await start(update, context)
    if lst[2] == lst[4] == lst[6] == '⭕':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Нолики победили!",
        )
        return await start(update, context)
    if '⬜' not in lst:
        await context.bot.send_message(
            chat_id= update.effective_chat.id,
            text="ничя"
        )
        return await start()
        
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
    ]
    markup = InlineKeyboardMarkup(keyboard)
    if i == '⭕':
        await query.edit_message_text(
            text="Ход крестиков.",
            reply_markup=markup,
        )
    else:
        await query.edit_message_text(
            text="Ход ноликов.",
            reply_markup=markup,
        )