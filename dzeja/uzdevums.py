import os
os.system('cls')
import requests
from bs4 import BeautifulSoup
from plyer import notification
url='https://www.nhl.com/standings/2025-02-05/division'
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
    pts_elem=soup.find('td', {"class":'sc-emwzcK lhryrG rt-td sorted sorted-0 sorted-asc'})
    result=pts_elem
    print(pts_elem)
    # notification.notify(
    #     title='Punkti komandai Las Vegas Golden Knights',
    #     message=result,
    #     timeout=10
    # )
# else:
#     notification.notify(
#         title='Kļūda!',
#         message='Nekas nav zināms!!!',
#         timeout=10
#     )