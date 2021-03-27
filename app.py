import telebot
import requests
import re
import os
from twilio.rest import Client
import pyrebase
bot = telebot.TeleBot("1733329720:AAHlKaQ5ONTA85WFhvOvpdn9Wi11qfBZ2Ms", parse_mode=None)
config = {
  "apiKey": "AIzaSyDPmfNoXoIO9S7TRH1eYtgqNY-Ny3kak9E",
  "authDomain": "wbtotelebot.firebaseapp.com",
  "databaseURL": "https://wbtotelebot-default-rtdb.firebaseio.com",
  "storageBucket": "wbtotelebot.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    a = message.text
    b = a.split('@')
    print(b)
    chatt = message[-1].chat.id
    if(b[0] == "/start"):
        bot.reply_to(message, "Welcome to tele2WA bot")
    elif(b[0] == "/setsid"):
        data = {
              "sid": b[1]
             }
  
        db.child("users").child(chatt).set(data)
        bot.reply_to(message, "SID added")
    elif(b[0] == "/settoken"):
        data = {
              "token": b[1]
             }
  
        db.child("users").child(chatt).set(data)
        bot.reply_to(message, "token added")
    elif(b[0] == "/setfromphone"):
        data = {
              "fromphone": b[1]
             }
        
        db.child("users").child(chatt).set(data)
        bot.reply_to(message, "fromphone added")
    elif(b[0] == "/settophone"):
        data = {
              "tophone": b[1]
             }
        db.child("users").child(chatt).set(data)
        bot.reply_to(message, "tophone added")
    elif(b[0] == "/updatetophone"):
        data = {
              "tophone": b[1]
             }
        db.child("users").child(chatt).update(data)
        bot.reply_to(message, "tophone updated")
    elif(b[0] == "/updatefromphone"):
        data = {
              "fromphone": b[1]
             }
        db.child("users").child(chatt).update(data)
        bot.reply_to(message, "fromphone updated")
    
    elif(b[0] =="/sendWA"):
        test = db.child("users").child(chatt).get()
        p = test.val()['sid']
        q = test.val()['token']
        t = user.val()['fromphone']
        r = user.val()['tophone']
        client = Client(p,q)
        client.messages.create(body=b[1],from_="whatsapp:"+ str(t),to="whatsapp:"+str(r))
    else:
        pass
       
if __name__ == '__main__':
    main()


