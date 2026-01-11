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

from states import TALK

async def talk_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        
    query = update.callback_query
    await query.answer()
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='чтобы поговорить, напиши что нибудь!'
    )
    return TALK

async def talk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.effective_message.text
    if "привет" in text.lower():
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Здарово, брат!",
        )
    elif 'пока' in text.lower():
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='пока, бро, возращайся!'
        )
    elif 'спасибо' in text.lower():
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='обращайся'
        )
    elif 'а как какать' in text.lower():
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='ну смотри... надо снять штаны, потом снять трусы, сесть, а дальше всё само пойдёт'
        )
    elif 'ахах' in text.lower():
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='АХАХАХАХАХАХХХХХАХААХАХАХААХАХАХАХАХАХАХААХ'
        )
    elif 'ура' in text.lower():
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='роблокс'
        )
    elif 'котики' in text.lower():
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Лучшие'
        )
    # чтобы тут обрабатывались 5 рандомных фраз
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
        )