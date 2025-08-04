from config import TOKEN
from telegram.ext import Updater, MessageHandler, Filters
from handlers import handle_photo, handle_contact, handle_dice, handle_text


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.photo, handle_photo))
    dispatcher.add_handler(MessageHandler(Filters.contact, handle_contact))
    dispatcher.add_handler(MessageHandler(Filters.dice, handle_dice))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_text))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
