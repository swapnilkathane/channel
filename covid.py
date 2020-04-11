import time, datetime
import telepot
import requests
import json

from bs4 import BeautifulSoup as bs

k=open("swapnil.txt",'r',encoding="utf-8")
care=k.read()

def GetNews():
    response = requests.get("https://www.indiatoday.in/coronavirus")
    response2=requests.get("https://lokmat.news18.com/tag/corona-virus/")
    soup=bs(response.text, "html.parser")
    soup2=bs(response2.text, "html.parser")
    #print(soup.prettify())
    latest_news=soup.find_all('div', class_='pollution-right')
    latest_news2=soup2.find('div', class_="photo-story")
    op=(latest_news[0].text)
    op2=(latest_news[1].text)
    op3=(latest_news[2].text)
    return op,op2,op3

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
                            #z=print(m,p)
                            # print(m.casefold())
                            if (m.casefold() == city.casefold()):

                                #   print(m,p)
                                return p
    return -1



def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print('Received: %s', command)
    if command.casefold() == '/hi':
        telegram_bot.sendMessage(chat_id,
                                 str("Hi! Welcome to covid-19 Maharashtra. \n I am here to tell you number of active cases in your city. \n  To start with it please enter /start \nTo know more use /help "))
    elif command == "/news":
        op,op2,op3 = GetNews()
        telegram_bot.sendMessage(chat_id,str(op ) + str("\n") + str("\n")+ str(op2)   + str("\n") + str("\n") + str(op3) + str( "\n source :-IndiaToday"))
    elif command == '/start':
        telegram_bot.sendMessage(chat_id,
                             str("Enter your city name to know, \n number of active cases in your city"))
    elif command == '/precautions':
        telegram_bot.sendMessage(chat_id,
                             str(care))
    elif command == 'who are you ?':
        telegram_bot.sendMessage(chat_id, str("I'm covid 19 help Bot created by Pankaj and Swapnil "))
    elif command == '/help':
        telegram_bot.sendMessage(chat_id, str(
            "I'm in my devlopment phase. \n I am responsive only to /start, /help, /hi, /news, /precautions and who are you ? \n Please bear with me." ))
    else:
        print(command)
        print(chat_id)
        Number = GetCity(command)
        if (Number > -1):
            telegram_bot.sendMessage(chat_id, str("Active patient in ") + str(command) + str(" = ") + str(Number))
        else:
            telegram_bot.sendMessage(chat_id, str("Please Enter Correct Spelling or use /help"))


telegram_bot = telepot.Bot('')
print(telegram_bot.getMe())
MessageLoop(telegram_bot, action).run_as_thread()
print('Up and Running....')
while 1:
    time.sleep(10)




