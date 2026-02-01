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
from openai import OpenAI
from states import TALK
from menu import start

async def talk_start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="чтобы поговорить, напиши что нибудь!, когда надоест, напиши слово меню"
    )
    return TALK


async def talk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.effective_message.text
    chat_id = update.effective_chat.id
    if text.lower() == "привет":
        await context.bot.send_message(
            chat_id=chat_id,
            text="Здарово, брат!",
        )
    elif text.lower() == "пока":
        await context.bot.send_message(chat_id=chat_id, text="пока, бро, возращайся!")
    elif text.lower() == "спасибо":
        await context.bot.send_message(chat_id=chat_id, text="обращайся")
    elif text.lower() == "а как какать":
        await context.bot.send_message(
            chat_id=chat_id,
            text="ну смотри... надо снять штаны, потом снять трусы, сесть, а дальше всё само пойдёт",
        )
    elif text.lower() == "какая погода":
        await context.bot.send_message(
            chat_id=chat_id,
            text="ХОЛОДНО!!!"
        )
    elif text.lower() == "ахах":
        await context.bot.send_message(
            chat_id=chat_id, text="АХАХАХАХАХАХХХХХАХААХАХАХААХАХАХАХАХАХАХААХ"
        )
    elif text.lower() == "спасибо":
        await context.bot.send_message(chat_id=chat_id, text="обращайся")
    elif "а как какать" in text.lower():
        await context.bot.send_message(
            chat_id=chat_id,
            text="ну смотри... надо снять штаны, потом снять трусы, сесть, а дальше всё само пойдёт",
        )
    elif "ахах" in text.lower():
        await context.bot.send_message(
            chat_id=chat_id, text="АХАХАХАХАХАХХХХХАХААХАХАХААХАХАХАХАХАХАХААХ"
        )
    elif "ура" in text.lower():
        await context.bot.send_message(chat_id=chat_id, text="роблокс")
    elif "котики" in text.lower():
        await context.bot.send_message(chat_id=chat_id, text="Лучшие")
    elif text == 'меню' or text == 'Меню':
        await context.bot.send_message(
            chat_id=chat_id,
            text="возвращаемся в меню"
            )

        return await start(update, context)
    else:
        if len(context.user_data["previous_message"]) > 10:
            context.user_data["previous_message"].pop(0)
            context.user_data["previous_message"].pop(0)
        client = OpenAI()
        response = client.responses.create(
            model="gpt-5-nano",
            reasoning={"effort": "low"},
            input=[
                {
                    "role": "developer",
                    "content": "ты телеграмм бот, который отвечает на сообщения пользователей в дружелюбной манере. Отвечай как главный приколист в компании. отвечай кратко, только на русском языке.",
                }
            ]
            + context.user_data["previous_message"]
            + [{"role": "user", "content": text}],
        )
        response_text = response.output_text
        await context.bot.send_message(chat_id=chat_id, text=response_text)
        context.user_data["previous_message"].append({"role": "user", "content": text})
        context.user_data["previous_message"].append(
            {"role": "assistant", "content": response_text}
        )
