import os
os.system('cls')
import random
c=0
base_1=0
base_2=0
base_3=0
runs=0
def baseball():
    global c
    global base_1
    global base_2
    global base_3
    global runs
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    if a-b == 2 or a-b == -2:
        print('Single')
        if base_1==0 and base_2==0 and base_3==0:
            base_1+=1
        elif base_1==1 and base_2==0 and base_3==0:
            base_2+=1
        elif base_1==0 and base_2==1 and base_3==0:
            base_3+=1
            base_1+=1
            base_2-=1
        elif base_1==0 and base_2==0 and base_3==1:
            base_3-=1
            base_1+=1
            runs+=1
        elif base_1==1 and base_2==1 and base_3==0:
            base_3+=1
        elif base_1==0 and base_2==1 and base_3==1:
            base_1+=1
            base_2-=1
            runs+=1
        elif base_1==1 and base_2==0 and base_3==1:
            base_2+=1
            base_3-=1
            runs+=1
        elif base_1==1 and base_2==1 and base_3==1:
            runs+=1
    elif a-b == 1 or a-b == -1:
        print('Double')
        if base_1==0 and base_2==0 and base_3==0:
            base_2+=1
        elif base_1==1 and base_2==0 and base_3==0:
            base_1-=1
            base_2+=1
            base_3+=1
        elif base_1==0 and base_2==1 and base_3==0:
            runs+=1
        elif base_1==0 and base_2==0 and base_3==1:
            base_2+=1
            base_3-=1
            runs+=1
        elif base_1==1 and base_2==1 and base_3==0:
            base_1-=1
            base_2+=1
            base_3+=1
            runs+=1
        elif base_1==0 and base_2==1 and base_3==1:
            base_3-=1
            runs+=2
        elif base_1==1 and base_2==0 and base_3==1:
            base_1-=1
            base_2+=1
            runs+=1
        elif base_1==1 and base_2==1 and base_3==1:
            base_1-=1
            runs+=2
    elif a-b == 0:
        print('Homerun')
        runs+=base_1+base_2+base_3+1
        if base_1==1:
            base_1-=1
        if base_2==1:
            base_2-=1
        if base_3==1:
            base_3-=1
    elif a-b == 3 or a-b == -3:
        print('Flyout')
        c+=1
        if base_2==1 and base_3==0 and c in[0,1]:
            base_2-=1
            base_3+=1
        elif base_2==0 and base_3==1 and c in[0,1]:
            base_3-=1
            runs+=1
        elif base_2==1 and base_3==1 and c in[0,1]:
            base_2-=1
            runs+=1
    elif a-b == -9:
        print('Base on Balls')
        if base_1==0 and base_2==0 and base_3==0:
            base_1+=1
        elif base_1==1 and base_2==0 and base_3==0:
            base_2+=1
        elif base_1==0 and base_2==1 and base_3==0:
            base_1+=1
        elif base_1==0 and base_2==0 and base_3==1:
            base_1+=1
        elif base_1==1 and base_2==1 and base_3==0:
            base_1+=1
        elif base_1==0 and base_2==1 and base_3==1:
            base_1+=1
            base_2-=1
        elif base_1==1 and base_2==0 and base_3==1:
            base_2+=1
        elif base_1==1 and base_2==1 and base_3==1:
            runs+=1
    else:
        print('out')
        c+=1

while True:
    baseball()
    if c==3:
        print('Inning over')
        print(f'{runs} Runs scored')
        break


