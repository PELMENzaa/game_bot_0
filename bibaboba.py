import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
)
from dotenv import load_dotenv

import os

async def biba(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="боба",
    )
    if 'биба' in update.effective_message.text.lower():
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="боба",
        )
    elif 'боба' in update.effective_message.text.lower():
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="биба",
        )