from bs4 import BeautifulSoup
import requests

class d20pfsrd:
    def __init__(self,table_num,url):
        self.response = requests.get(url).content
        self.unicode_str = self.response.decode('utf8')
        self.soup = BeautifulSoup(self.unicode_str, 'html.parser')
        self.table = self.soup.findAll('table')[table_num]
        self.table_tr = self.table.findAll('tr')

        # self.list1 = []
        # self.list2 = []

    def list_generator(self,num_of_columns,start_column = -1,end_column = -1):
        item_stats_list = []
        #---------------------------------#
        # Creates a list of a lists
        # containing items attributes
        #---------------------------------#
        for i in self.table_tr:
            self.table_td = i.findAll(['td','th'])
            tmp = []
            for j in range(start_column,end_column):
                tmp.append(self.table_td[j].get_text())
            item_stats_list.append(tmp)
        key = (item_stats_list[0])
        item_stats_list.pop(0)
        #----------------------------------#
        # Creates a list of dictionaries
        # containing items attributes
        #----------------------------------#
        item_stats_dict = []
        for item in item_stats_list:
            tmp = {}
            for i in range(len(item)):
                tmp[key[i]] = item[i]
            item_stats_dict.append(tmp)
        return item_stats_dict
