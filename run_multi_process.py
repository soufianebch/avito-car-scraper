from variables import decalge,max_pages
import time
import os
import random
from os.path import exists


def generate_csv_path():
    # for i in range(100):
    r = random.randint(0,1000)
    csv_file_path = rf'.\output\avito_car_dataset{r}.csv'
        # if not exists(csv_file_path):
        #     break
    return csv_file_path

n = int(input('Number of processes you want: '))
# max_pages = int(input('number of pages: '))
page_index = decalge
for i in range(n):
    csv_file_path = generate_csv_path()
    print('process',i,'- Save path:',csv_file_path,'Pages:',page_index,'-',int(page_index+max_pages/n))
    os.system(r'start /min main.py '+csv_file_path+' '+str(page_index)+' '+str(int(page_index+max_pages/n)))
    page_index+=int(max_pages/n)

input()
