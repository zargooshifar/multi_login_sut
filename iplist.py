#tedade ip
global ipnum,ip,sm
def getiplist():
    try:
        ipr1 = int(input("Enter a number between 100 ~ 200\n192.168."))
        if (ipr1>255):
            print("{} not valid.".format(ipr1))
            error


    except:
        print("error! default (5) is set.")
        ipr1 = 5
    try:
        ipr2 = int(input("Enter a number between 1 ~ 200\n192.168.{}.".format(ipr1)))
        if (ipr2>255):
            print("{} not valid.".format(ipr2))
            error
    except:
        print("error! default (100) is set.")
        ipr2 = 100
    try:
        ipnum = int(input("how num ip? (Enter a number between 3 ~ 10)\n "))
        if (ipr2+ipnum > 255):
            print('192.168.{}.{} not a valid ip'.format(ipr1,ipr2+ipnum))
            error
    except:
        print("default is set . default is 5")
        ipnum = 5
    if (ipr1 > 255) or (ipr2+ipnum > 255):
        print ('192.168.{}.{} not a valid ip\nmax value for ip is 255\ntry to set defaut values.'.format(ipr1,ipr2+ipnum))
        ipr1,ipr2,ipnum = 5,100,5


    for i in range(ipnum):
        ip = ['192.168.{}.{}'.format(ipr1,ipr2+i) for i in range (ipnum)]

    return ip,ipnum
def getSM():
    x=0
    try:
        while not x in range(1,3):
            x = int(input('SUBNET MASKS:\n1. 255.255.0.0\n2. 255.255.255.0\nwhich one?  '))
            print(x)
    except:
        print('error! defualt (255.255.0.0) is set.')
        x=1
    choices = {
        1   :   "255.255.0.0",
        2   :   "255.255.255.0"
    }


    sm = choices.get(x,'')
    return sm

#x = getSM()
#print(x,'this is it')
#x,y = getiplist()

#print (x,y)
