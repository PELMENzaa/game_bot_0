import logging
from telegram import Update
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

from states import GUESS_NUMBER

load_dotenv()
async def game_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text= 'так. ну я значит угадываю число, кароче, отвечай, больше, меньше или угадал'
    )
    return GUESS_NUMBER

async def game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = Update.effective_message.text