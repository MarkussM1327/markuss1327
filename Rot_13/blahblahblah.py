import os
os.system('cls')
month_dict={
    'janvāris':1,
    'februāris':2,
    'marts':3,
    'aprīlis':4,
    'maijs':5,
    'jūnijs':6,
    'jūlijs':7,
    'augusts':8,
    'septembris':9,
    'oktobris':10,
    'novembris':11,
    'decembris':12
}

month_value_dict={
    'janvāris':0,
    'februāris':31,
    'marts':59,
    'aprīlis':90,
    'maijs':120,
    'jūnijs':151,
    'jūlijs':181,
    'augusts':212,
    'septembris':243,
    'oktobris':273,
    'novembris':304,
    'decembris':335
}

name=input('Tavs vārds - ')

birth_year=int(input('Tavs dzimšanas gads - '))

birth_month=input('Tavs dzimšanas mēnesis - ').lower()

birth_date=int(input('Tavs dzimšanas datums - '))

month_value=month_dict[birth_month]

day_value_of_user=month_value_dict[birth_month]+birth_date
print_value=-247+day_value_of_user

if print_value>1:
    print(f'Čau {name}, tava dzimšanas diena būs pēc {print_value} dienām')
elif print_value==1:
    print(f'Čau {name}, tava dzimšanas diena būs pēc {print_value} dienas')
elif print_value==0:
    print(f'Čau {name}, tava dzimšanas diena ir šodien')
elif print_value<0:
    new_print_value=365+print_value
    print(f'Čau {name}, tava dzimšanas diena būs pēc {new_print_value} dienām')

