# vards = input("Kā tevi sauc?")
# vecums = input("cik tev gadu?")
# vards = vards.strip().title()
# print("Sveiks " + vards + ", tev ir " + vecums,"gadi")
# #print("Sveiks, \"labo skolēn\"")
# print(vards, vecums, "gadīgs", sep='?????')
# x = float(input('cik ir x '))
# y = float(input('cik ir y '))
# z = x + y
# print(round(z,1))
# string=input('Ievadi simbolu virkni: ')
# print(f'Simbolu virknes garums: {len(string)}')
#es par if sen jau zinu
import os
os.system('cls')
print("\n")
a=int(input('koeficents a '))
b=int(input('koeficents b '))
c=int(input('koeficents c '))
d=b**2-4*a*c
if d>0:
    x1=(-b+d**0.5)/2*a
    x2=(-b-d**0.5)/2*a
    print(f'x1={x1}, x2={x2}')
elif d==0:
    x=-b/2*a
    print(f'x={x}')
else:
    print('Nav sakņu')

