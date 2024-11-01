import os
os.system('cls')
import random
live=0
blank=0
count=random.randint(2,6)
a=random.randint(0,1)
b=random.randint(0,1)
def buckshot():
    global live 
    global blank
    global count
    global a
    global b
    global c
    if a==1:
        live+=1
        return 'live'
    elif a==0:
        blank+=1
        return 'blank'
    elif count==2 and a==0:
        b==1
        live+=1
        return 'live'
    elif count==2 and a==1:
        b==0
        blank+=1
        return 'blank'
    elif count>2:
        c=random.randint(0,1)
        if c==1:
            live+=1
            return 'live'
        else:
            blank+=1
            return 'blank'
    elif count==3 and a==1 and b==1:
        c==0
        blank+=1
        return 'blank'
    elif count==3 and a==0 and b==0:
        c==1
        live+=1
        return 'live'
    