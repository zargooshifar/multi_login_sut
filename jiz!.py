import setip,subprocess,time,logintab,os


px = open("dtbs/px","r")
pxe = open("dtbs/pxe","r")
pxj = open("dtbs/pxj","r")
pxr = open("dtbs/pxr","r")
for line in px:
	print (line.rstrip())
	time.sleep(0.00)

px.close()

input("Attention:\n      This app developed by Jacob Zarg, plz dont use it without his permission...")


ip,ipnum = setip.setIP()
for line in pxj:
    print (line.rstrip())
    time.sleep(0.00)
pxj.close()
def jiz():
    for i in range (ipnum):
        cmd = r"nd.exe node_modules\dispatch-proxy\bin\dispatch.js start --http " + ip[i]
        print(cmd)
        subprocess.Popen(cmd,shell=True)
        time.sleep(0.5)
        logintab.test()
        pkill = "taskkill /f /im nd.exe "

        os.system(pkill)
        os.system(pkill)
        os.system(pkill)
        print ("Login Succeded!")

    for line in pxe:
        print (line.rstrip())
        time.sleep(0.00)
    pxe.close()
    for line in pxr:
        print (line.rstrip())
        time.sleep(0.00)
    pxr.close()
    print("\n\n\n\n\nAll Done!\nsocks ready!\n")
    ipall=''
    for i in range (ipnum):
        ipall = ipall + ' ' + ip[i]
    dcmd = r'nd.exe node_modules\dispatch-proxy\bin\dispatch.js start ' + ipall
    while 1==1:
        subprocess.call(dcmd,shell=True)

jiz()