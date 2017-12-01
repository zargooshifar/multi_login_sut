import subprocess,time
i=0
def checkwifi():
    proc = subprocess.Popen('netsh wlan show interfaces',shell=True,stdout=subprocess.PIPE)
    connection = False
    while True:
      line = proc.stdout.readline().decode('ascii')
      if line != '':
        #print (line.strip())
        if ': connected' in line:
            connection = True
        elif ': disconnected' in line:
            connection = False
        if 'Signal' in line:
            signal = line.strip().split(" : ")[1].strip()
      else:
        break
    if connection == True:
        print ('WiFi is Connected. Signal Strength is {}'.format(signal))
        return 1
    else:
        print('Wifi is not Connect.')
        wificonnect()
        return 0
#scan ssids

def scan():
    proc = subprocess.Popen('netsh wlan show networks',shell=True,stdout=subprocess.PIPE)
    ssids=[]
    while True:
      line = proc.stdout.readline().decode('ascii')
      if line != '':
    
        if 'SSID' in line:
            #print (line.strip())
            ssids.append(line.strip().split(" : ")[1].strip())
      else:
        break
    wnum = len(ssids)
    #print("{} wifi is founded.".format(wnum))
    #for i in range (wnum-1):
    #    print ("{}  :  {}".format(i,ssids[i]))
    return ssids,wnum
def wificonnect():
    global i
    ssid,wnum = scan()
    if wnum == 0:
        "Wifi is Down"
        time.sleep(3)
    else:
        print('{} wifi founded.'.format(wnum))
        if i < wnum:
            i += 1 
        else:
            i = 0
        print("try to connect wifi number {} : {}".format(i,ssid[i-1]))
        proc = subprocess.Popen('netsh wlan connect name={} ssid={}'.format(ssid[i-1],ssid[i-1]),shell=True,stdout=subprocess.PIPE)
        time.sleep(3)
        checkwifi()