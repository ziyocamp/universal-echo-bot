from telegram import Update, ParseMode, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, ReplyKeyboardRemove
from telegram.ext import CallbackContext


def handle_photo(update: Update, context: CallbackContext):
    photo = update.message.photo[0]

    update.message.reply_photo(
        photo=photo,
        caption="siz <b>yuborgan</b> rasm",
        parse_mode=ParseMode.HTML
    )


def handle_contact(update: Update, context: CallbackContext):
    contact = update.message.contact

    update.message.reply_contact(
        first_name=contact.first_name,
        phone_number=contact.phone_number
    )


def handle_dice(update: Update, context: CallbackContext):
    dice = update.message.dice

    update.message.reply_dice(
        emoji=dice.emoji
    )


def handle_text(update: Update, context: CallbackContext):
    update.message.reply_markdown_v2(
        text=">Block quotation started"
    )
    update.message.reply_html(
        text='<b>bold</b>',
    )


def handle_main_menu(update: Update, context: CallbackContext):
    update.message.reply_markdown_v2(
        text=">Siz Bosh Menu ni Tanldingiz",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Mahsulotlar")]
            ]
        )
    )


def start(update: Update, context: CallbackContext):
    bot = context.bot
    user = update.effective_user

    bot.send_message(
        chat_id=user.id,
        text='Menu Tanlang:',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(
                        "Bosh Menu", 
                        web_app=WebAppInfo('https://kun.uz/')
                    ), 
                    KeyboardButton("Buyurtma Berish")
                ],
                [KeyboardButton("Location", request_location=True), KeyboardButton("Contact", request_contact=True)],
                [KeyboardButton("Close")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True,
        )
    )


def remove_keyboard(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Closed Keyboard',
        reply_markup=ReplyKeyboardRemove()
    )
