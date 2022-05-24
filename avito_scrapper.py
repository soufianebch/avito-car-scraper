from variables import *
import time
import csv
import random
from os.path import exists



class avitoSrapperTool:
    def __init__(self, driver, csv_file_path=csv_file_path, search_url=general_search_url,start_page_index=start_page_index,last_page_index=last_page_index):
        self.driver = driver
        self.csv_file_path = csv_file_path
        self.search_url = search_url
        self.start_page_index = start_page_index
        self.last_page_index = last_page_index
        self.search_page_index = 1
        self.extracted_listings_count = 0
    
    def get_info(self,listing):
        driver = self.driver
        try:
            driver.get(listing)
            item = dict()
            item['Lien'] = listing
            item['Prix'] = int(driver.find_element_by_css_selector('p.bGMGAj').text.replace('DH', '').replace('\u202f', ''))
            item['Ville'] = driver.find_element_by_css_selector('span.gCIGeB').text
            item['Type de carburant'] = driver.find_elements_by_css_selector('span.kUjmne')[0].text
            item['Puissance fiscale'] = driver.find_elements_by_css_selector('span.kUjmne')[1].text.replace(' CV', '')
            item['Boite de vitesses'] = driver.find_elements_by_css_selector('span.kUjmne')[2].text
            specifics = [e.text for e in driver.find_elements_by_css_selector('span.brylYP')]
            specifics_values = [e.text for e in driver.find_elements_by_css_selector('span.iVDpDk')]
            for i in range(1,len(specifics)):
                item[specifics[i]] = specifics_values[i]
            listing_equipments = [equipment.text for equipment in driver.find_elements_by_css_selector('span.kFXDVa')]
            for car_equipment in all_car_equipments:
                if car_equipment in listing_equipments:
                    item[car_equipment] = True
                else:
                    item[car_equipment] = False
            for specific in all_car_specifics:
                if specific not in list(item.keys()):
                    item[specific] = None
            return item
        except Exception as exc:
            # print(exc)
            pass

    def save_to_csv(self,item):
        try:
            if not item:
                return
            with open(self.csv_file_path, 'r', newline='') as f:
                item['Id'] = len(f.read().split('\n'))
            with open(self.csv_file_path, 'a', newline='') as f:
                header = ['Id','Lien','Ville','Secteur']+all_car_specifics+all_car_equipments+['Prix']
                dict_writer = csv.DictWriter(f, header, None)
                dict_writer.writerow(item)
            self.extracted_listings_count += 1
            print('#'+str(item['Id']),f'has been saved to {self.csv_file_path}')
            return item['Id']
        except Exception as exc:
            print(exc)

    def create_new_csv_file(csv_file_path=csv_file_path):
        file_exists = exists(csv_file_path)
        if file_exists:
            return csv_file_path
        with open(csv_file_path, 'w', newline='') as csvfile:
            header = ['Id','Lien','Ville','Secteur']+all_car_specifics+all_car_equipments+['Prix']
            writer = csv.DictWriter(csvfile, fieldnames = header)
            writer.writeheader()
        return csv_file_path

    def get_page_urls(self):
        driver = self.driver
        listings = [a.get_attribute('href') for a in driver.find_elements_by_css_selector('.listing div a')]
        with open(self.csv_file_path, 'r') as f:
            s = f.read()
            listings = [listing for listing in listings if listing not in s]
            # for line in f:
                #     for listing in listings:
                #         if listing in line:
                #             listings.remove(listing)
        return listings

    def next_page(self):
        if self.search_page_index==-1:
            search_page_index = random.randint(self.start_page_index, self.last_page_index)
        else:
            search_page_index = self.search_page_index
            self.search_page_index += 1
        print(f'>>> Page: {search_page_index}')
        self.driver.get(self.search_url+f'&o={search_page_index}')
        
        return search_page_index
