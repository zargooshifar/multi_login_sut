import sqlite3



db = sqlite3.connect('x.db')
db.row_factory = sqlite3.Row

table = db.execute('select * from login')

for usr in table:
    print (usr['username'])
