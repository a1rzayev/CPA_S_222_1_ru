# подключаем нужные пакеты для телеграма и логгинга(введения отчетов)
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import logging

# подключаем логгинг
logging.basicConfig(level=logging.INFO)

# сохраняем токен(ключ для доступа к боту)
TOKEN = "7718572264:AAEk9Jp4vkJgjOFnKm08gSHaT9Jto4qPid4"

# функция для приветствия
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# функция для ответа
async def text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    await update.message.reply_text(f'Hello {update.effective_user.first_name}, You said: {text}')

# запускаем приложение с помощью токена
app = ApplicationBuilder().token(TOKEN).build()

# подключаем обработчики для работы ответов
app.add_handler(CommandHandler("hello", hello))
app.add_handler(MessageHandler(filters.TEXT & ~ filters.COMMAND, text))
app.run_polling()