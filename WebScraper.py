from bs4 import BeautifulSoup
import requests


response = requests.get('https://www.d20pfsrd.com/magic-items/potions')

soup = BeautifulSoup(response.text, 'html.parser')

# posts = soup.findChild('tr')
# posts = soup.findAll('caption')

table = soup.findAll('table')[6]
# table2 = table.findAll('caption','Table: Potion Costs')

for tr in table.findAll('tr'):
    print('--------------------------------------------------------------------------------------------------')
    for td in tr.findAll('td'):
        print(td.get_text())
        # print(td.get_text().encode('utf-8'))
