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

MAINMENU, TALK, BIBA, GUESS_NUMBER, TICTACTOE = range(5)