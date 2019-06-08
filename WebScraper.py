from bs4 import BeautifulSoup
import requests


response = requests.get('https://www.d20pfsrd.com/magic-items/potions')

soup = BeautifulSoup(response.text, 'html.parser')

# posts = soup.findChild('tr')
# posts = soup.findAll('caption')

for caption in soup.findAll('caption'):
    # print(caption)
    if caption.get_text() == 'Table: Potion Costs':
        print(caption)
