import time, datetime
import telepot
import requests
import json
from telepot.loop import MessageLoop

now = datetime.datetime.now()


def GetCity(city):
    response = requests.get("https://api.covid19india.org/state_district_wise.json")
    r = response.json()
    print(city.casefold())
    for i, j in r.items():
        # print(i,j)
        for k, l in j.items():
            if i == "Maharashtra":
                # print(k,l)
                for m, n in l.items():
                    # print(m,n)
                    for o, p in n.items():
                        if o == "confirmed":
                            # print(m.casefold())
                            if (m.casefold() == city.casefold()):
                                #   print(m,p)
                                return p
    return -1


def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print('Received: %s', command)
    if command.casefold() == 'hi':
        telegram_bot.sendMessage(chat_id,
                                 str("Hi! Welcome to covid19 Maharashtra info and help bot use /help for more info "))
    elif command == '/start':
        telegram_bot.sendMessage(chat_id,
                                 str("Welcome to covid 19 Maharashtra information bot type  /help  for more info "))
    elif command == 'who are you ?':
        telegram_bot.sendMessage(chat_id, str("I'm covid 19 help Bot created by Pankaj and Swapnil "))
    elif command == '/help':
        telegram_bot.sendMessage(chat_id, str(
            "I'm covid 19 help Bot \n for now I can answer following commands \n hi /start\n asking active patient in any city just send city name eg. Mumbai"))
    else:
        print(command)
        print(chat_id)
        Number = GetCity(command)
        if (Number > -1):
            telegram_bot.sendMessage(chat_id, str("Active patient in ") + str(command) + str(" = ") + str(Number))
        else:
            telegram_bot.sendMessage(chat_id, str("Sorry I dont have any info about ") + str(command) + str(
                "  as i am in testing phase please bear with me  "))


telegram_bot = telepot.Bot('')
print(telegram_bot.getMe())
MessageLoop(telegram_bot, action).run_as_thread()
print('Up and Running....')
while 1:
    time.sleep(10)
