import sqlite3
rc=0
db = sqlite3.connect('requests/dtbs/datatab.db')
db.row_factory = sqlite3.Row
table = db.execute('select ROWID, * from login')
for usr1 in table:
    table2 = db.execute('select ROWID, * from login')
    for usr2 in table2:
        if usr1['rowid'] != usr2['rowid']:
            #print(usr1['username'],usr2['username'])
            if usr1['username'] == usr2['username']:
                #print(usr1['rowid'],usr2['rowid'])
                db.execute('delete from login where rowid={}'.format(usr1['rowid']))
                rc+=1
db.commit()
print(rc, ' record deleted')