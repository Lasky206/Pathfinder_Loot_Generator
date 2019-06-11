from bs4 import BeautifulSoup
import requests

class d20pfsrd:
    def __init__(self,tabnum):
        self.response = requests.get('https://www.d20pfsrd.com/magic-items/potions').content
        self.unicode_str = self.response.decode('utf8')
        self.soup = BeautifulSoup(self.unicode_str, 'html.parser')

        self.table = self.soup.findAll('table')[tabnum]
        self.table_tr = self.table.findAll('tr')

        self.list1 = []

    def list_generator(self):
        for i in self.table_tr:
            self.table_td = i.findAll('td')
            tmp = []
            for j in self.table_td:
                table_clean = tmp.append(j.get_text())
                self.list1.append(tmp)
        return self.list1


    # dict = {'minor':'', 'medium':'', 'major':'', 'Potion':'', 'Price':''}
