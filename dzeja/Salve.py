import os
os.system('cls')
import requests
from bs4 import BeautifulSoup
from plyer import notification
url='https://weather.com/en-IN/weather/today/l/56.95,24.11?par=google&temp=c'
def data(url):
    try:
        r=requests.get(url, timeout=10)
        r.raise_for_status()
        return r.text
    except requests.exceptions.RequestException as e:
        print(f'Kļūda: {e}')
        return None
htmldata=data(url)
if htmldata:
    soup=BeautifulSoup(htmldata, 'html.parser')
    # print(soup.prettify())
    temp_elem=soup.find('span', {'data-testified':'TemperatureValue'})
    rain_elem=soup.find('span', {'data-testified':'ProcantageValue'})
    temp= temp_elem.text if temp_elem else 'Nav datu'
    mitrums=rain_elem.text if rain_elem else 'Nav nokrišņu info'
    result=f'Pašreizēja temperatūra Rīgā: {temp}\n Mitrums: {mitrums}'
    notification.notify(
        title='laika ziņas Rīgā',
        message=result,
        timeout=10
    )
else:
    notification.notify(
        title='Kļūda!',
        message='Nekas nav zināms!!!',
        timeout=10
    )

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
<<<<<<< HEAD
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

=======
# print("\n")
import math
# a=int(input('koeficents a '))
# b=int(input('koeficents b '))
# c=int(input('koeficents c '))
# d=b**2-4*a*c
# if d>0:
#     x1=(-b+d**0.5)/(2*a)
#     x2=(-b-d**0.5)/(2*a)
#     print(f'x1={x1}, x2={x2}')
# elif d==0:
#     x=-b/2*a
#     print(f'x={x}')
# else:
#     print('Nav sakņu')
>>>>>>> 83f1f34520d5bb9eb4a19001e480fc1e6ba55171
