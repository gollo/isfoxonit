#!/usr/bin/env python3
import logging
import os
import random
from datetime import datetime, timedelta

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

thirsty = ["Dying for a beer", 'Will suck fatz for a pint', "This sun makes me want a beer.",
           "Anything makes me want a beer.", "12% body fat or beer? It's getting harder to choose.",
           "Don't speak to me I'm sober.", 'Sparkly water please.', "I am sooo boring without beer",
           "I look so old when I am sober", "Need a beer to wash down Fatz's tonsil glaze.",
           "Did I say I'm off the booze?", 'Pulling nose hairs.', 'Sewing buttons on my XXS shirt.',
           'Polishing the chrome pole.', "Updating my status on Facebook cause I'm not drinking don't you know",
           'Been off it for {} days, that must deserve a kiss.'.format(random.randrange(1, 50)),
           "Getting boat home, could kill a beer on the boat.",
           "This rain is making me thirsty.",
           "One fucking week to go...",
           "Trains all delayed by an hour now ffs,Drive a man to drink.", "Who needs beer anyway?"]
drink = ["Pissed as a fart.", "Get to the bar, cnut.", "Call me an Uber I need a sleep outside of my front door.",
         "Look Ma I'm making the most of a terroist incident by getting on telly pissed.",
         "New office has a pub, booze free time is not going to last."]

mThirsty = thirsty.copy()
mDrink = drink.copy()


def usage():
    return (
        "Send me a message:\n\n*/dyingtoknow@IsFoxOnItBot* - Update on how long for a drink.\n\nTry me a few times, you never know what you'll get!\n")


def sothirsty():
    global mThirsty, thirsty
    print(mThirsty)
    if len(mThirsty) == 0:
        mThirsty = thirsty.copy()
    quote = mThirsty[random.randrange(0, len(mThirsty))]
    mThirsty.remove(quote)
    print(mThirsty)
    return quote


def drinking():
    global mDrink, drink
    print(mDrink)
    if len(mDrink) == 0:
        mDrink = drink.copy()
    quote = mDrink[random.randrange(0, len(mDrink))]
    mDrink.remove(quote)
    print(mDrink)
    return quote


def start(bot, update):
    update.message.reply_text("*Hi*", parse_mode="Markdown")


def help(bot, update):
    update.message.reply_text("I don't know what you mean you obtuse Manny.\n" + usage(), parse_mode="Markdown")


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def dyintoknow(bot, update):
    logger.warn('dyingtoknow')
    today = datetime.today()
    target = datetime(year=2017, month=7, day=5, hour=0, minute=0, second=0)
    remaining = target - today
    if remaining <= timedelta(0):
        update.message.reply_text("*Time for drinkies!*\n\n*Foxy's status:*\n_" + drinking() + "_",
                                  parse_mode="Markdown")
    else:
        update.message.reply_text(
            "*Foxy's status:\n*_" + sothirsty() + "_" + "\n\n" + "*Time remaining:\n*" + "_Fatz Style:_  " + str(
                remaining), parse_mode="Markdown")


def main():
    TOKEN = "358070225:AAFKiJ7LlmwpVt5MqyYbzcA4tW4TVvOkyew"
    PORT = int(os.environ.get('PORT', '5000'))

    # Create the EventHandler and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("dyingtoknow", dyintoknow))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, help))

    # log all errors
    dp.add_error_handler(error)

    # add handlers
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)
    updater.bot.set_webhook("https://seangollschewsky.me/" + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()
