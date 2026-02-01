import logging
from telegram import (
    Update,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
)
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler,
    CallbackQueryHandler,
)


from dotenv import load_dotenv

load_dotenv()

import os

from modes.bibaboba import biba, biba_start
from modes.talk import talk, talk_start
from modes.game import game_start, game
from modes.menu import start
from states import MAINMENU, TALK, BIBA, GUESS_NUMBER, TICTACTOE
from modes.tictactoe import tictactoe_start, tictactoe

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    application = ApplicationBuilder().token(os.getenv("TOKEN")).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            MAINMENU: [
                CallbackQueryHandler(pattern="talk", callback=talk_start),
                CallbackQueryHandler(pattern="biba", callback=biba_start),
                CallbackQueryHandler(pattern="guess_number", callback=game_start),
                CallbackQueryHandler(pattern="tictactoe", callback=tictactoe_start),
            ],
            TALK: [MessageHandler(filters.TEXT & ~filters.COMMAND, talk)],
            BIBA: [MessageHandler(filters.TEXT & ~filters.COMMAND, biba)],
            GUESS_NUMBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, game)],
            TICTACTOE: [CallbackQueryHandler(callback=tictactoe, pattern="^[0-8]$")],
        },
        fallbacks=[CommandHandler("start", start)],
    )
    #кикишки
    application.add_handler(conv_handler)
    application.run_polling()
