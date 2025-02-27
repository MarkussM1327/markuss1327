import os
os.system('cls')
# 1.uzdevums
dict={
    'Briseles kāposti':'4,4',
    'Seleriju saknes':'4,2',
    'Brokoļi':'3,0',
    'Ziedkāposti':'2,9',
    'Burkāni':'2,9',
    'Sarkanās bietes':'2,5',
    'Salāti':'1,8',
    'Upenes':'6,8',
    'Avenes':'5,0',
    'Zemenes':'4,0',
    'Jāņogas':'2,5',
    'Āboli':'2,3',
    'Apelsīni':'2,2',
    'Plūmes':'1,7'
}
def smth():
    global ievade
    ievade=input('Ievadi produktu - ')
    if ievade in dict:
        print(f'Šis produkts izvada {dict[ievade]}  balastvielu daudzumu gramos uz 100 g')
    else:
        print('Nepareizi ievadīts produkts vai produkts nav uz plakāta')
while True:
    smth()
    if ievade in dict:
        break
# 2.uzdevums
def no_vowels():
    global word,word2
    word=input('Ievadi vārdu - ')
    word2=word.strip().replace('a','').replace('e','').replace('i','').replace('o','').replace('u','').replace('A','').replace('E','').replace('I','').replace('O','').replace('U','')
    print(word2)
no_vowels()
# 3.uzdevums
def cocacola():
    total = 0  
    print("Lūdzu, ievietojiet monētas (atbalstām: 5, 10, 20, 50 centi). Dzēriena cena: 90 centi.")
    
    while total < 90:
        try:
            coin = int(input("Ievadiet monētas vērtību centos: "))
            if coin in [5, 10, 20, 50]:
                total += coin
                print(f"Jūs esat ievietojuši kopā: {total} centi.")
            else:
                print("Šādu monētu nepieņemam. Mēģiniet vēlreiz.")
        except ValueError:
            print("Lūdzu, ievadiet derīgu monētu vērtību kā veselu skaitli.")
    
    change = total - 90
    if change > 0:
        print(f"Paldies! Jūsu atlikums ir {change} centi.")
    else:
        print("Paldies, ka iegādājāties dzērienu!")

cocacola()

    