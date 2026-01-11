from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ContextTypes
)

from states import BIBA

async def biba_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    query = update.callback_query
    await query.answer()
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="играем в биба-боба! напиши биба или боба, чтобы получить второго!",
    )
    return BIBA


async def biba(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    keyboard = [
        ['Биба'],['Боба']
    ]
    markup = ReplyKeyboardMarkup(keyboard)
    text = update.effective_message.text
    if 'биба' in text.lower():
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="боба",
            reply_markup=markup
        )
    elif 'боба' in text.lower():
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="биба",
            reply_markup=markup
        )