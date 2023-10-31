import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# from dotenv import load_dotenv
# dotenv_path = BASE_DIR / '.env'
# load_dotenv(dotenv_path)  # take environment variables from .env.

tasks = []


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        'Привет! Это ваш Todo list бот. Напишите "/add <задача>", чтобы добавить задачу.')


# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    task = ' '.join(context.args)

    if not task:
        await update.message.reply_text(
            "Пожалуйста, добавьте задачу после команды /add")
        return

    tasks.append(task)

    await update.message.reply_text(f'Твоя задача "{task}" добавлена')


async def show_tasks_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not tasks:
        await update.message.reply_text(f'В списке нет задач')

    tasks_list = '\n'.join(tasks)

    await update.message.reply_text(tasks_list)


def main() -> None:
    token = os.environ.get('TELEGRAM_BOT_TOKEN')
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("add", add_task))
    app.add_handler(CommandHandler('list', show_tasks_list))

    app.run_polling()


if __name__ == '__main__':
    main()
