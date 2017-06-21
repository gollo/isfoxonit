import random
from datetime import datetime, timedelta
from time import sleep

import telepot
from telepot.loop import MessageLoop

today = datetime.today()
target = datetime(year=2017, month=7, day=5, hour=0, minute=0, second=0)
remaining = target - today
print(str(remaining))
oldtarget = datetime(year=2017, month=5, day=5, hour=0, minute=0, second=0)
# remaining = oldtarget - today
remaining = target - target
if remaining <= timedelta(0):
    print("Drinkies!!")
else:
    print("Not Yet")

print(str(remaining))


def usage():
    return ("Send me a message:\n\n*/dyingtoknow@IsFoxOnItBot* - Update on how long for a drink.\n\nTry me a few times, you never know what you'll get!\n")


def drinking():
    drink = ["Pissed as a fart.", "Get to the bar, cnut.", "Call me an Uber I need a sleep outside of my front door.",
             "Look Ma I'm making the most of a terroist incident by getting on telly pissed."]
    return drink[random.randrange(0, len(drink))]


def sothirsty():
    thirsty = ["Dying for a beer", 'Will suck fatz for a pint', "This sun makes me want a beer.",
               "Anything makes me want a beer.","12% body fat or beer? It's getting harder to choose.","Don't speak to me I'm sober.",'Sparkly water please.',"I am sooo boring without beer","I look so old when I am sober","Need a beer to wash down Fatz's tonsil glaze.","Did I say I'm off the booze?",'Pulling nose hairs.','Sewing buttons on my XXS shirt.','Polishing the chrome pole.',"Updating my status on Facebook cause I'm not drinking don't you know","I've been off it for ${random.randrange(1,50)} days, that must deserve a kiss."]
    return thirsty[random.randrange(0, len(thirsty))]


print(usage())
print(drinking())
print()
print(sothirsty())

print("Time remaining: " + str(remaining) + "\n" + drinking())


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']


    print('Got command: %s' % command)

    if command == '/dyingtoknow' or str(command).lower() == '/dyingtoknow@isfoxonitbot':
        today = datetime.today()
        target = datetime(year=2017, month=7, day=5, hour=0, minute=0, second=0)
        remaining = target - today
        #remaining = target - target
        if remaining <= timedelta(0):
            print("Drinkies!!")
            bot.sendMessage(chat_id, "*Time for drinkies!*\n\n*Foxy's status:*\n_" + drinking() +"_", parse_mode="Markdown")
            #bot.sendMessage(chat_id, "*testing bold*,_testing italics_", parse_mode="Markdown")
        else:
            bot.sendMessage(chat_id, "*Foxy's status:\n*_"+sothirsty() +"_"+ "\n\n" + "*Time remaining:\n*" + "_Fatz Style:_  "+str(remaining), parse_mode="Markdown")

    else:
        bot.sendMessage(chat_id, "I don't know what you mean you obtuse Manny.\n" + usage(), parse_mode="Markdown")


bot = telepot.Bot('358070225:AAFKiJ7LlmwpVt5MqyYbzcA4tW4TVvOkyew')

MessageLoop(bot, handle).run_as_thread()
print('I am listening ...')

while 1:
    sleep(10)

