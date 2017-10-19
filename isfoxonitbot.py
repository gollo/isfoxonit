"""Fox is on it bot. Reports foxy's drinking status."""
import logging
import os
import random
from datetime import datetime, timedelta

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - '
                           '%(message)s')
LOGGER = logging.getLogger(__name__)

TOKEN = "358070225:AAFKiJ7LlmwpVt5MqyYbzcA4tW4TVvOkyew"
THIRSTY = ["Dying for a beer", 'Will suck fatz for a pint',
           "This sun makes me want a beer.", "Anything makes me want a beer.",
           "12% body fat or beer? It's getting harder to choose.",
           "Don't speak to me I'm sober.", "Sparkly water please.",
           "I am sooo boring without beer", "I look so old when I am sober",
           "Need a beer to wash down Fatz's tonsil glaze.",
           "Did I say I'm off the booze?", "Pulling nose hairs.",
           "Sewing buttons on my XXS shirt.",
           "Updating my status on Facebook cause "
           "I'm not drinking don't you know",
           'Been off it for {} days, that must deserve a kiss.'.format
           (random.randrange(1, 50)),
           "Getting boat home, could kill a beer on the boat.",
           "This rain is making me thirsty.", "One fucking week to go...",
           "New office has a pub, booze free time is not going to last.",
           "Trains all delayed by an hour now ffs, drive a man to drink.",
           "Who needs beer anyway?"]
DRINK = ["Pissed as a fart.", "Get to the bar, cnut.",
         "Call me an Uber I need a sleep outside of my front door.",
         "Look Da I'm making the most of a terroist incident by getting on "
         "telly pissed.",
         "Droney droney droney... tree tree tree!!! Feck!!!",
         "Ah Guiness. The farts of the gods."]

mThirsty = THIRSTY.copy()
mDrink = DRINK.copy()
myState = "thirsty"


def gcloud_envs_print():
    """Print GAE env variables."""
    gcloud_envs = ['GAE_INSTANCE', 'GAE_MEMORY_MB', 'GAE_VERSION', 'PORT',
                   'GCLOUD_PROJECT', 'GAE_SERVICE']
    output = ""
    for genv in gcloud_envs:
        if genv in os.environ:
            output = output + genv + ": " + os.environ[genv] + "\n"
    return output


def usage():
    """Return usage message."""
    return (
        "Send me a message:\n\n*/dyingtoknow@IsFoxOnItBot* - "
        "Update on how long for a drink.\n\nTry me a few times, "
        "you never know what you'll get!\n")


def sothirsty():
    """Provide a semi random thirsty quote."""
    global mThirsty
    print(mThirsty)
    if len(mThirsty) == 0:
        mThirsty = THIRSTY.copy()
    quote = mThirsty[random.randrange(0, len(mThirsty))]
    mThirsty.remove(quote)
    print(mThirsty)
    return quote


def drinking():
    """Provide a semi-random drinking quote."""
    global mDrink
    print(mDrink)
    if len(mDrink) == 0:
        mDrink = DRINK.copy()
    quote = mDrink[random.randrange(0, len(mDrink))]
    mDrink.remove(quote)
    print(mDrink)
    return quote


def start(bot, update):
    """Get the bot going."""
    update.message.reply_text("*Hi*", parse_mode="Markdown")


def help_isfoxonit(bot, update):
    """Message for help or not understood."""
    update.message.reply_text("I don't know what you mean you obtuse Manny.\n"
                              + usage(), parse_mode="Markdown")


def bot_error(bot, update, error):
    """Log a generic error."""
    #LOGGER.warning('Update "%s" caused error "%s"' % (update, error))
    LOGGER.warning("Update %s caused error %s", update, error)


def switch(bot, update):
    """Toggle foxy's state."""
    LOGGER.debug("Switch: %s", update)
    global myState
    if myState == "thirsty":
        myState = "pissed"
        update.message.reply_text("Switched from thirsty to "
                                  + myState + ".\n", parse_mode="Markdown")
    else:
        myState = "thirsty"
        update.message.reply_text("Switched from pissed to "
                                  + myState + ".\n", parse_mode="Markdown")


def dyingtoknow(bot, update):
    """Return info on foxy's drinking status."""
    LOGGER.info('dyingtoknow')
    today = datetime.today()
    target = datetime(year=2017, month=10, day=1, hour=17, minute=0, second=0)
    remaining = target - today
    if remaining <= timedelta(0) or myState == "pissed":
        update.message.reply_text("*Time for drinkies!*\n\n*Foxy's status:*\n_"
                                  + drinking() + "_", parse_mode="Markdown")
    else:
        update.message.reply_text(
            "*Foxy's status:\n*_" + sothirsty() + "_"
            + "\n\n" + "*Time remaining:\n*" + "_Fatz Style:_  "
            + str(remaining), parse_mode="Markdown")


def print_sysinfo(bot, update):
    """Print out some sysinfo."""
    import sysinfo
    LOGGER.info(str("\n" + sysinfo.sysinfo() + "\n" + gcloud_envs_print()))
    update.message.reply_text(sysinfo.sysinfo())


def main():
    """Start bot, tell Telegram."""
    port = int(os.environ.get('PORT', '5000'))

    # Create the EventHandler and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    fox_dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    fox_dispatcher.add_handler(CommandHandler("start", start))
    fox_dispatcher.add_handler(CommandHandler("help", help_isfoxonit))
    fox_dispatcher.add_handler(CommandHandler("dyingtoknow", dyingtoknow))
    fox_dispatcher.add_handler(CommandHandler("switch", switch))
    fox_dispatcher.add_handler(CommandHandler("sysinfo", print_sysinfo))

    # on noncommand i.e message - echo the message on Telegram
    fox_dispatcher.add_handler(MessageHandler(Filters.text, help))

    # log all errors
    fox_dispatcher.add_error_handler(bot_error)

    # add handlers
    updater.start_webhook(listen="0.0.0.0",
                          port=port,
                          url_path=TOKEN)
    updater.bot.set_webhook("https://isfoxonit.duckdns.org/" + TOKEN)
    updater.idle()


if __name__ == '__main__':
    """Main."""
    main()
