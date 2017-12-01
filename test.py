"""import subprocess,os,time

dcmd = "dispatch start "
p = subprocess.Popen(dcmd,shell=True,bufsize=1)

print ("xx")

time.sleep(2)
"""

ip = ['192.168.0.1' , '192.168.0.2']

cmd = "ip number is {}".format(ip[1])

print(cmd)