from telegram import (
    Update,
    ReplyKeyboardMarkup, KeyboardButton,
    WebAppInfo
)
from telegram.ext import CallbackContext


def start_command(update: Update, context: CallbackContext):
    welcome_msg = f"Assalomu alaykum {update.effective_user.full_name}!"
    url = "https://uzum.uz/uz?srsltid=AfmBOoqj0OsERee-YXBJB7qR7Q1bACqtdfmF_3po3mfeeBHd7xFqduAt"

    update.message.reply_html(
        text=welcome_msg,
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="🛍 Buyurtma berish", web_app=WebAppInfo(url=url))],
                [KeyboardButton(text="📦Buyurtmalarim"), KeyboardButton(text="⚙️ Sozlamalar")],
                [KeyboardButton(text="ℹ️ Biz haqimizda"), KeyboardButton(text="✍️ Fikr qoldirish")]
                ], resize_keyboard=True
        )
    )

