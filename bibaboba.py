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

async def biba(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.effective_message.text
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="боба",
    )
    if 'биба' in text.lower():
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="боба",
        )
    elif 'боба' in text.lower():
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="биба",
        )