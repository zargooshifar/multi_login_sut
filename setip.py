import iplist,time,subprocess
def setIP():
    cname = "Ethernet "     #changed
    #cname = "Wi-Fi "     #changed
    #sm = " 255.255.255.0 "  #changed
    dg = " 192.168.0.21"    #
    dns = ["192.168.0.1" ,  #fixed
           "192.168.0.11"]
    ip,ipnum = iplist.getiplist()
    sm = iplist.getSM()

    for i in range(ipnum):
        print ('trying to set ip ', ip[i])
        subprocess.call("netsh in ip add address {} {} {} {}".format(cname,ip[i],sm,dg),shell=True)
    for i in range(2):  #fixed
        print ("trying to set DNS ", dns[i])
        subprocess.call("netsh in ip add dnsservers {} {}".format(cname,dns[i]),shell=True)

    print("\nIP set, all Done!")
    return ip,ipnum

#setIP()