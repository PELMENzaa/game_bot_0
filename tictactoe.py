from telegram import Update
from telegram.ext import (
    ContextTypes
)
from states import TICTACTOE
async def tictactoe_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="Игра Крестики-Нолики начинается! Выберите клетку, чтобы сделать ход."
    )
    return TICTACTOE