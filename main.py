import pandas as pd
import os
#https://repl.it/@alexandermr24/verylocalchat
#Alexander Montolio 1072200


send = []
read = []
notread = []
user = []
act =[]

def ct():
  who = input("Who is speaking:\t")
  if who in user:
    chat = input(who + ">\t")
    if chat:
      act.append(chat)
      send.append(chat)
      read.append(chat)
    else:
      print("this message below was not seen")
      s = read[-1]
      notread.append(s)
      read.pop()
      print(s+"\n")   
    ct()
  else:
    #notread.append(chat)
    print("this message below was not seen")
    s = read[-1]
    notread.append(s)
    read.pop()
    print(s+"\n")
    print("")
    print("Error Message I received that said that there was a breach and that all info is in jeopardy, we have logged you out.\n")
    menu()

def menu():
  print("""Hi this is your main page for the 
  so called 'chat', choose options to your liking.\n """)
  print("1-begin chat.\n"+"2-seen messages.\n"+"3-not seen messages\n"+"4-Activity log\n")
  n = int(input("> "))
  act.append(n)
  
  if n == 1:
    print("Welcome.")
    print("very local chat.")
    try:
      x = int(input("how many users are gonna be online? \t"))
    except:
      print("pls, enter intergers, not str.")
    act.append(x)
    if x==2:
      for i in range(x):
        us = input("User: ")
        user.append(us)
        act.append(us)
      ct()
    else:
      print("Not enough ppl, to have a conversation.")
      menu()
  if n == 2:
    act.append(n)
    s = pd.Series(read)
    print(read)
    menu()
  if n==3:
    act.append(n)
    s = pd.Series(notread)
    print(notread)
    menu()
  else:
    print("Activies: from first to last.")
    print(act)
    menu()
    
    
menu()
