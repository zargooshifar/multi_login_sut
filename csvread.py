import random
import csv
import os


file_size=700
f=open("ac.csv",'r')
offset=random.randrange(file_size)
f.seek(offset)
f.readline()
random_line=f.readline()
print(random_line)
username,password = random_line.split(",")
password.strip()
print(username)
print(password)


f.close()
