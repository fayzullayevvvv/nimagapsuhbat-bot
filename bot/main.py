from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from bot.config.settings import settings
from .handlers import start_command, cart_handler, settings_handler, information_handler, comment_handler, back_handler, language_handler


def main() -> None:
    updater = Updater(settings.BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler(command="start", callback=start_command))
    dispatcher.add_handler(MessageHandler(filters=Filters.text("📦Buyurtmalarim"), callback=cart_handler))
    dispatcher.add_handler(MessageHandler(filters=Filters.text("⚙️ Sozlamalar"), callback=settings_handler))
    dispatcher.add_handler(MessageHandler(filters=Filters.text("ℹ️ Biz haqimizda"), callback=information_handler))
    dispatcher.add_handler(MessageHandler(filters=Filters.text("✍️ Fikr qoldirish"), callback=comment_handler))
    dispatcher.add_handler(MessageHandler(filters=Filters.text("⬅️ Orqaga"), callback=back_handler))
    dispatcher.add_handler(MessageHandler(filters=Filters.text("🌐 Tilni o'zgartirish"), callback=language_handler))
    

    updater.start_polling()
    updater.idle()
