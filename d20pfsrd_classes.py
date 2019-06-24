from bs4 import BeautifulSoup
import requests
import json
import os
import sys
import time

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
                print(item[i])
                tmp[key[i]] = item[i].replace('—','-')
            item_stats_dict.append(tmp)
        # print(tmp)
        # time.sleep(20)
        return item_stats_dict

class File_Handler:
    def Open_File(self,file_name):
        if file_name.endswith('.json'):
            with open(os.path.join(sys.path[0], file_name)) as json_file:
                data = json.load(json_file)
                return data
            json_file.closed
        else:
            print('File type not supported')

class scribe:
    def write_json(self,dict,datacard_name):
        # with open('./datacards/'+datacard_name) as existing_json_file:
        #     data = json.load(existing_json_file)
        #     print(data)
        with open('./datacards/'+datacard_name,'w') as json_file:
            json.dump(dict, json_file, ensure_ascii=False, indent=4)

    def append_json(self,datacard_name,input_list):
        with open('./datacards/'+datacard_name) as existing_json_file:
            data = json.load(existing_json_file)
            for i in input_list:
                data.append(i)
        existing_json_file.closed

        with open('./datacards/'+datacard_name,'w') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        json_file.closed

class num_finder:
    def stringsearch(string):
        list = []
        num = ''
        for i in range(len(string)):
            if '0' <= string[i] <= '9':
                num += string[i]
            elif num != '' and num[0] != '0':
                list.append(num)
                num = ''
            elif num != '' and num[0] == '0':
                list.append(num[1:])
                num = ''
        if actual != '':
            list.append(num)
        return list
