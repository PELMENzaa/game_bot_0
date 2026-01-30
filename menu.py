import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler,
)
from states import MAINMENU


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
            [InlineKeyboardButton("Поговорим", callback_data='talk')],
            #[InlineKeyboardButton("Поиграем в Биба-Боба", callback_data='biba')],
            [InlineKeyboardButton("Угадай моё число", callback_data='guess_number')],
            [InlineKeyboardButton("хочу поиграть в крестики-нолики с другом", callback_data='tictactoe')]
        ]
    markup = InlineKeyboardMarkup(keyboard)
    context.user_data['previous_message'] = []
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Привет {update.effective_user.first_name}!. чем займемся?",
        reply_markup=markup
        
    )
    return MAINMENU