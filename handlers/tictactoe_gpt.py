from telegram import InlineKeyboardButton, Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from config.states import TICTACTOE_GPT
from handlers.menu import start
from openai import OpenAI
from utils.render_board import render_board

async def tictactoe_gpt_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print('GPT')
    query = update.callback_query  # Полная информация о нажатой кнопке
    await query.answer()  # отвечаем на запрос
    context.user_data["lst"] = [
        "⬜",
        "⬜",
        "⬜",
        "⬜",
        "⬜",
        "⬜",
        "⬜",
        "⬜",
        "⬜",
    ]
    lst = context.user_data["lst"]  # Получаем список из user_data
    
    markup = render_board(lst)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="ход крестиков",
        reply_markup=markup,
    )
    return TICTACTOE_GPT


async def tictactoe_gpt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ables = ['1','2','3','4','5','6','7','8','9']
    i = '❌'
    
    query = update.callback_query
    await query.answer()

    nomer_knopki = int(query.data)
    lst = context.user_data["lst"]
    if lst[nomer_knopki] == '⬜':
        lst[nomer_knopki] = i

        markup = render_board(lst)
        
        await query.edit_message_text(
            text="Щас будет ходить ИИ",
            reply_markup=markup)
        
        client = OpenAI()
        response = client.responses.create(
            model="gpt-5-nano",
            reasoning={"effort": "low"},
            input=[
                {
                    "role": "developer",
                    "content": "ты -- бот, играющий в крестики нолики. ты получаешь доску, пиши только номер клетки, в которую ставишь нолик",
                }
            ]
            + [{"role": "user", "content": "|".join(context.user_data["lst"])}],
        )
        response_text = response.output_text
    if response_text in ables:
        response_text = int(response_text)
        lst[response_text-1] = '⭕'
        gpt = False
    if lst[0] == lst[1] == lst[2] == '❌':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Крестики победили!",
        )
        return await start(update, context)
    if lst[3] == lst[4] == lst[5] == '❌':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Крестики победили!",
        )
        return await start(update, context)
    if lst[6] == lst[7] == lst[8] == '❌':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Крестики победили!",
        )
        return await start(update, context)
    if lst[0] == lst[3] == lst[6] == '❌':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Крестики победили!",
        )
        return await start(update, context)
    if lst[1] == lst[4] == lst[7] == '❌':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Крестики победили!",
        )
        return await start(update, context)
    if lst[2] == lst[5] == lst[8] == '❌':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Крестики победили!",
        )
        return await start(update, context)
    if lst[0] == lst[4] == lst[8] == '❌':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Крестики победили!",
        )
        return await start(update, context)
    if lst[2] == lst[4] == lst[6] == '❌':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Крестики победили!",
        )
        return await start(update, context)
    if lst[0] == lst[1] == lst[2] == '⭕':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Нолики победили!",
        )
        return await start(update, context)
    if lst[3] == lst[4] == lst[5] == '⭕':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Нолики победили!",
        )
        return await start(update, context)
    if lst[6] == lst[7] == lst[8] == '⭕':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Нолики победили!",
        )
        return await start(update, context)
    if lst[0] == lst[3] == lst[6] == '⭕':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Нолики победили!",
        )
        return await start(update, context)
    if lst[1] == lst[4] == lst[7] == '⭕':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Нолики победили!",
        )
        return await start(update, context)
    if lst[2] == lst[5] == lst[8] == '⭕':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Нолики победили!",
        )
        return await start(update, context)
    if lst[0] == lst[4] == lst[8] == '⭕':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Нолики победили!",
        )
        return await start(update, context)
    if lst[2] == lst[4] == lst[6] == '⭕':
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Нолики победили!",
        )
        return await start(update, context)
    if '⬜' not in lst:
        await context.bot.send_message(
            chat_id= update.effective_chat.id,
            text="ничя"
        )
        return await start()
        
    markup = render_board(lst)
    
    await query.edit_message_text(
        text="Ходи",
        reply_markup=markup)