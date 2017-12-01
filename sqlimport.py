import sqlite3
c=0

db = sqlite3.connect('requests/dtbs/datatab.db')
db.row_factory = sqlite3.Row
# create db and import data
try:
    db.execute('create table login (username text, password text)')
except:
    print('ok')
f=open('data.csv','r')
for line in f:
    usr,psw = line.strip().split(',')
    #print(usr,psw)
    db.execute('insert into login (username,password) values ({},{})'.format(usr,psw))
    c+=1
db.commit()
print (c,'record added')