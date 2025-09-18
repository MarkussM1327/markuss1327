import os
os.system('cls')
def birthday():
    global x,y,cik_katram
    try:
        x=int(input('Ievadi cik gabalu ir kūkas - '))
        y=int(input('Ievadi cik draugi atnākuši - '))
        cik_katram=x/y
        return True
    except (ValueError,ZeroDivisionError):
        if ValueError and not ZeroDivisionError:
            print('Nepareiza ievade, jābūt skaitlim!')
            return False
        elif ZeroDivisionError:
           print('Nepareiza ievade, ievadē nedrīkst nulle!') 
        return False
while True:
    if birthday():
        print(f'Katram pienākas {cik_katram} kūkas gabali')
        break
    