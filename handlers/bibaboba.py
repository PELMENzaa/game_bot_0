from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ContextTypes
)

from config.states import BIBA, MAINMENU
from handlers.menu import start

async def biba_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    query = update.callback_query
    await query.answer()
    
    keyboard = [
        ['Биба','Боба'],['Вернуться в меню']]
    markup = ReplyKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="играем в биба-боба! напиши биба или боба, чтобы получить второго!",
        reply_markup=markup
    )
    return BIBA


async def biba(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    keyboard = [
        ['Биба','Боба'],['Вернуться в меню']
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
    elif 'вернуться в меню' in text.lower():
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="возвращаемся в главное меню"
        )
        return await start(update, context)