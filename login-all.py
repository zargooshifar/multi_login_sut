import requests
import time
import html2text
import os
import wifi
import sqlite3
current_file_path = __file__
current_file_dir = os.path.dirname(__file__)
pxlp = os.path.join(current_file_dir,'requests/dtbs/pxl.db')
dbfile = os.path.join(current_file_dir,'requests/dtbs/data.db')
username,password,usage,traffic,c,dn = 12345678,12345678,0,0,0,0



db = sqlite3.connect(dbfile)
db.row_factory = sqlite3.Row
# create db and import data
#db.execute('create table login (username int, password int)')
#f=open('requests/dtbs/ac.db','r')
#for line in f:
#    usr,psw = line.strip().split(',')
#    print(usr,psw)
#    db.execute('insert into login (username,password) values ({},{})'.format(usr,psw))
#    db.commit()


def deletethis():
    global username
    print('Deleting this one...')
    time.sleep(0.5)
    db.execute('delete from login where username={}'.format(username))
    db.commit()

def dbcount():
    global dn
    dn=0
    tableall = db.execute('select * from login')
    for each in tableall:
        dn += 1
    print('Accounts in Database: {}'.format(dn))

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
    table = db.execute('SELECT * FROM login ORDER BY RANDOM() LIMIT 1')
    for each in table:
        username = each['username']
        password = each['password']
    global c
    c += 1
    dbcount()
    print("Try to Login...")
    print('Try Count: ', c)

    return username,password
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
        deletethis()
        os.system('cls')
        test()
    if "Maximum number of concurrent logins reached" in html:
        print("Failed!\nReason: Max Number\n####################\n\n\nTry Again:")
        time.sleep(0.2)
        os.system('cls')
        test()

    if "does not exists" in html:
        print("\nFailed!\nReason: This username does not exists\n####################\n\n\nTry Again...")
        deletethis()
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

