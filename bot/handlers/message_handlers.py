from telegram import (
    Update,
    ReplyKeyboardMarkup, KeyboardButton,
    WebAppInfo
)
from telegram.ext import CallbackContext
from bot.config import comment_msg


def cart_handler(update: Update, context: CallbackContext):
    update.message.reply_text("Sizda hali birorta ham buyurtma yo`q")

def settings_handler(update: Update, context: CallbackContext):
    update.message.reply_html(
        text="⚙️ Sozlamalar",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="🌐 Tilni o'zgartirish")],
                [KeyboardButton(text="📞 Telefon raqamingizni o'zgartiring")],
                [KeyboardButton(text="⬅️ Orqaga")]
            ], resize_keyboard=True
        )
    )

def information_handler(update: Update, context: CallbackContext):
    update.message.reply_text("shu yerda joylashganmiz")
    update.message.reply_text("Elektron pochta: ozodbekfayzullayev1220@gmail.com")

def comment_handler(update: Update, context: CallbackContext):
    update.message.reply_text(comment_msg)

def back_handler(update: Update, context: CallbackContext):
    welcome_msg = f"🏠 Bosh menyu"
    url = "https://uzum.uz/uz?srsltid=AfmBOoqj0OsERee-YXBJB7qR7Q1bACqtdfmF_3po3mfeeBHd7xFqduAt"

    update.message.reply_html(
        text=welcome_msg,
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="🛍Buyurtma berish", web_app=WebAppInfo(url=url))],
                [KeyboardButton(text="📦Buyurtmalarim"), KeyboardButton(text="⚙️ Sozlamalar")],
                [KeyboardButton(text="ℹ️ Biz haqimizda"), KeyboardButton(text="✍️ Fikr qoldirish")]
                ], resize_keyboard=True
        )
    )

def language_handler(update: Update, context: CallbackContext):
    update.message.reply_html(
        text="Tilni tanlang",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="🇺🇿 O'zbekcha"), KeyboardButton(text="🇷🇺 Русский")],
                [KeyboardButton(text="🇺🇸 English")],
                [KeyboardButton(text="⬅️ Orqaga")]
            ], resize_keyboard=True
        )
    )

def change_number_handler(update: Update, context: CallbackContext):
        contact_button = KeyboardButton(
             text="Mening raqamim",
             request_contact=True
        )
        update.message.reply_html(
        text="Iltimos, telefon raqamingizni yuboring",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [contact_button],
                [KeyboardButton(text="⬅️ Orqaga")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
        
def send_number_handler(update: Update, context: CallbackContext):
    contact = update.message.contact

    if contact.user_id != update.effective_user.id:
        update.message.reply_text("Faqat o'zingizni raqamingizni yuboring.")
        return
    
    phone_number = contact.phone_number

    update.message.reply_text(
        "✅ Telefon raqamingiz muvaffaqiyatli o'zgartirildi"
    )