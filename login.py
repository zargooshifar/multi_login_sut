import random
import csv
import os
import requests
import time
f=open("dtbs/ac.db",'r')

def getup():
    offset=random.randrange(0,476)
    offset= offset*21
    f.seek(offset)
    f.readline()
    random_line=f.readline()
    username,password = random_line.split(",")
    password = password.strip()
    
    print(username)
    print(password)
    if password[:3] == "136":
        return username,password
    else:
        print ("Not Tabrizian!\nNext!\n")
    return 0,0


def load():
    username=0
    while (username == 0) :
        username,password = getup()
    
    proxies = {"http": "127.0.0.1:8080"}
    data = {'username': username, 'password': password} #fixed
    r = requests.post('http://172.16.254.2/login', data=data, proxies=proxies)  #url changed for test
    import html2text
    html = html2text.html2text(r.text)
    print("\nlogin...")
    return html

def login():
    html=load()
    if "Wrong password" in html:
        print("Wrong Password\ntry again:")
        login()
    if "Maximum number of concurrent logins reached" in html:
        print("Max Number\ntry again:")
        login()

    if "does not exists" in html:
        print("does not exists\ntry again:")
        login()
    if "No user found" in html:    #this is for test
        print("does not exists\ntry again:")
        login()
    if "User Traffic quota has exceeded" in html:
        print("Max Number\ntry again:")
        login()
    if "If nothing happens," in html:
        pxl=open("dtbs/pxl","r")
        for line in pxl:
            print (line.rstrip())
            time.sleep(0.00)
        print("##################################################")
        print("################>  Logged IN!!  <#################")
        print("##################################################\n\n")
		
        ##time.sleep(10)    # pause
        #f.close()
