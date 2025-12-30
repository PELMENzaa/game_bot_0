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

from states import BIBA

async def biba_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="играем в биба-боба! напиши биба или боба, чтобы получить второго!",
    )
    return BIBA


async def biba(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.effective_message.text

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