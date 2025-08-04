from telegram import Update, ParseMode
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
