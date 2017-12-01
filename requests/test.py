import subprocess,time
x=''
p = subprocess.Popen("dispatch start 192",stdout=subprocess.PIPE,shell=True)

while True:
  line = p.stdout.readline()

  if b"EADDRINUSE" in line:
      print('Error: EADDRINUSE')
  if not line: break


print ("end")