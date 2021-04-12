import telebot
import requests
import re
import os
from twilio.rest import Client
import pyrebase
bot = telebot.TeleBot("Replace this with telegram bot father key", parse_mode=None)
config = {
  "apiKey": "",
  "authDomain": "",
  "databaseURL": "",
  "storageBucket": ""
}
x = 0
y = 0
z = 0
q = 0
firebase = pyrebase.initialize_app(config)
db = firebase.database()

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    a = message.text
    b = a.split('@')
    print(b)
    global x
    global y
    global z
    global q
    chatt = message.chat.id
    if(b[0] == "/start"):
        bot.reply_to(message, "Welcome to tele2WA bot")
    elif(b[0] == "/setsid"):
        x = b[1]
        print(x)
        bot.reply_to(message, "SID added")
    elif(b[0] == "/settoken"):
        y = b[1]
        print(y)
        bot.reply_to(message, "token added")
    elif(b[0] == "/setfromphone"):
        z = b[1]
        print(z)
        bot.reply_to(message, "fromphone added")
    elif(b[0] == "/settophone"):
        q = b[1]
        print(q)
        data = {
          "sid":x,
          "token":y,
          "fromphone":z,
          "tophone":q
         }
        db.child("users").child(chatt).set(data)
        bot.reply_to(message, "details added")
    elif(b[0] == "/updatetophone"):
        data4 = {
              "tophone": b[1]
             }
        db.child("users").child(chatt).update(data4)
        bot.reply_to(message, "tophone updated")
    elif(b[0] == "/updatefromphone"):
        data5 = {
              "fromphone": b[1]
             }
        db.child("users").child(chatt).update(data5)
        bot.reply_to(message, "fromphone updated")
    
    elif(b[0] =="/send"):
        test = db.child("users").child(chatt).get()
        p = test.val()['sid']
        d = test.val()['token']
        t = test.val()['fromphone']
        r = test.val()['tophone']
        client = Client(p,d)
        client.messages.create(body=b[1],from_="whatsapp:"+ str(t),to="whatsapp:"+str(r))
    else:
        pass
bot.polling()

