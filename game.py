import logging
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler,
)

from dotenv import load_dotenv

import os

from states import GUESS_NUMBER, MAINMENU

load_dotenv()
async def game_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    query = update.callback_query
    await query.answer()

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text= 'так. ну я значит угадываю число, кароче, отвечай, больше, меньше или угадал'
    )
    keyboard = [['загадал'],['шот я передумал']]
    markup = ReplyKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text= 'число от 1 до 100.',
        reply_markup=markup
    )
    return GUESS_NUMBER
    
async def game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.effective_message.text
    if text == 'загадал':
        pass
    if text == 'шот я передумал':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= 'окей, возвращаемся в главное меню'
        )
        return MAINMENU
    