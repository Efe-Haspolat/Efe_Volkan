import time


ampel = ["Rot","Gelb","Grün",""]
zeit=[0,10,1,15]


m =0
n=0
while True:
    for warten in range(0,1):
        time.sleep(zeit[m])
        print(ampel[n])
        m=m+1
        n=n+1
        if n==4:
            n=0
            m=0
        break