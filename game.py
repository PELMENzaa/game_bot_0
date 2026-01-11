from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from states import GUESS_NUMBER
from menu import start

async def game_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    query = update.callback_query
    await query.answer()

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text= 'так. ну я значит угадываю число, кароче, отвечай, больше, меньше или угадал'
    )
    keyboard = [['загадал'],['шот я передумал']]
    markup = ReplyKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text= 'число от 1 до 100.',
        reply_markup=markup
    )
    return GUESS_NUMBER
    
async def game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.effective_message.text
    if text == 'загадал':
        keyboard = [['больше', 'меньше'],['угадал']]
        markup = ReplyKeyboardMarkup(keyboard)
        gran_up = 100
        gran_down = 0
        is_game_over = False
        while not is_game_over:
            text = update.effective_message.text
            middle = (gran_down + gran_up) // 2
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text= f'{middle}?',
                reply_markup=markup
            )
            
        
            if 'больше' in text.lower():
                gran_down = middle
            elif 'меньше' in text.lower():
                gran_up = middle
            elif 'угадал' in text.lower():
                start(update, context)
                is_game_over = True
                await context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text= 'ура! я выиграл!'
                )
            if middle == 99 and 'больше' in text.lower():
                await context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text= 'значит ты загадал число 100!\nура! я выиграл!'
                )
            start(update, context)
            is_game_over = True
    if text == 'шот я передумал':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= 'окей, возвращаемся в главное меню'
        )
        start(update, context)
    