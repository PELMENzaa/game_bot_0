import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
)
from dotenv import load_dotenv

import os

from bibaboba import biba

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


# callback
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # update - полная информация о том, что произошло
    # update.effective_chat - вся инфа о чате
    # update.effective_user - вся инфа о пользователе
    # update.effective_message - вся инфа о сообщении
    # update.effective_message.text - текст сообщения
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Привет {update.effective_user.first_name}!. Я бот, могу выполнять разные задачи. /biba - чтобы поиграть в биба-боба",
    )
    
async def biba_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="играем в биба-боба! напиши биба или боба, чтобы получить второго!",
    )
    return biba



if __name__ == "__main__":
    application = ApplicationBuilder().token(os.getenv("TOKEN")).build()

    # handler - обработчик
    # CommandHandler - обработчик команд
    # MessageHandler - обработчик сообщений
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("biba", biba))

    application.run_polling()