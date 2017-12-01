import os,time,subprocess,signal
p = subprocess.Popen("dispatch start --http 192.168.1.12", shell=True)
print("opend")
print(p.pid)
time.sleep(5)
subprocess.Popen("taskkill /f /im node.exe")
print("killed")
time.sleep(2)
print("end")