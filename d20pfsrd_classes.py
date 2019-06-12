from bs4 import BeautifulSoup
import requests

class d20pfsrd:
    def __init__(self,tabnum,url):
        self.response = requests.get(url).content
        self.unicode_str = self.response.decode('utf8')
        self.soup = BeautifulSoup(self.unicode_str, 'html.parser')

        self.table = self.soup.findAll('table')[tabnum]
        self.table_tr = self.table.findAll('tr')

        self.list1 = []
        self.list2 = []

    def list_generator(self):
        for i in self.table_tr:
            self.table_td = i.findAll('td')
            tmp = []
            for j in self.table_td:
                table_clean = tmp.append(j.get_text())
            self.list1.append(tmp)
        self.list1.pop(0)
        return self.list1

    def dict_convertion(self,input_list):
        for item in input_list:
            self.var1 = item[0]
            self.var2 = item[1]
            self.var3 = item[2]
            self.var4 = item[3]
            self.var5 = item[4]
            # self.var4 = {
            #     'Minor':self.var1,
            #     'Medium':self.var2,
            #     'Major':self.var3,
            #     'Potion':self.var4,
            #     'Price':self.var5
            # }
            self.list2.append({'Minor':self.var1, 'Medium':self.var2, 'Major':self.var3, 'Potion':self.var4, 'Price':self.var5})
        return self.list2
