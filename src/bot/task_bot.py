# from telegram import Update, BotCommand
# from telegram.ext import Updater, CommandHandler, CallbackContext
from services.task_service import create_task, list_tasks
from auth.auth import is_admin
# import logging
from telegram.ext import *
from telegram import Update
# import queue
API_KEY = '7344889088:AAFNIMNeQoN7rOJoWm4eC-dbZo9VMNOTF7o'

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Welcome to Task Bot! Use /help for available commands.")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    commands = [
        "/create_task <username> <task_description> - Assign a task to a user",
        "/list_tasks - List all tasks assigned to you",
        "/update_task <task_id> <status> - Update task status",
    ]

    # Use await to send messages asynchronously
    await update.message.reply_text("\n".join(commands))

async def create_task_handler(update: Update, context: CallbackContext):
    if not await is_admin(update):
        await update.message.reply_text("Only admins can create tasks.")
        return

    args = context.args
    if len(args) != 2:
       await update.message.reply_text("Usage: /create_task <username> <task_description>")
    return


async def list_tasks_handler(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    response = list_tasks(user_id)
    await update.message.reply_text(response)


def main():

    application = Application.builder().token(API_KEY).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("create_task", create_task_handler))
    application.add_handler(CommandHandler("list_tasks", list_tasks_handler))
    application.add_handler(CommandHandler("update_task", list_tasks_handler))
    application.run_polling()


if __name__ == "__main__":
    main()
