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
    keyboard = [['больше', 'меньше'],['угадал']]
    markup = ReplyKeyboardMarkup(keyboard)
    if text == 'загадал':
        context.user_data['gran_up'] = 101
        context.user_data['gran_down'] = 0
        context.user_data['middle'] = (context.user_data['gran_down'] + context.user_data['gran_up']) // 2
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= f'{context.user_data['middle']}?',
            reply_markup=markup
        )
    elif 'больше' in text.lower() or 'меньше' in text.lower():
        if 'больше' in text.lower():
            context.user_data['gran_down'] = context.user_data['middle']
        elif 'меньше' in text.lower():
            context.user_data['gran_up'] = context.user_data['middle']
        context.user_data['middle'] = (context.user_data['gran_down'] + context.user_data['gran_up']) // 2
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= f'{context.user_data['middle']}?',
            reply_markup=markup
        )
    elif 'угадал' in text.lower():
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= 'ура! я выиграл!'
        )
        return await start(update, context)
    if context.user_data['middle']==100:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= 'значит ты загадал 100! я выиграл!'
        )
        return await start(update, context)
    elif context.user_data['middle']==0:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= 'значит ты загадал 0! я выиграл!'
        )
        return await start(update, context)
    if context.user_data['gran_up'] - context.user_data['gran_down'] <= 1:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= 'нет такого числа! ты обманываешь меня! отправляемся в главное меню'
        )
        return await start(update, context)
    elif text == 'шот я передумал':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text= 'окей, возвращаемся в главное меню'
        )
        return await start(update, context)
    