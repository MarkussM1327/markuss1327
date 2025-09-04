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
# name=input('Tavs vārds - ')

# birth_year=int(input('Tavs dzimšanas gads - '))

birth_month=input('Tavs dzimšanas mēnesis - ').lower()

# birth_date=int('Tavs dzimšanas datums - ')

month_value=month_dict[birth_month]
print(month_value)
