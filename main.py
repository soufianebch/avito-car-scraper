import variables
from variables import *
from avito_scrapper import *
from selenium import webdriver
from datetime import datetime
import random
import sys

def open_session():
    options = webdriver.ChromeOptions()
    options.add_argument('log-level=2')
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(executable_path=executable_path, options=options)
    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver


def main():
    try:
        csv_file_path = sys.argv[1]
        start_page_index = int(sys.argv[2])
        last_page_index = int(sys.argv[3])
        search_page_index = -1
    except Exception as exc:
        search_page_index = None
        csv_file_path = variables.csv_file_path
        start_page_index = variables.start_page_index
        last_page_index = variables.last_page_index
        # print(exc)
        # input('...')
        pass
    driver = open_session()
    driver.get('https://www.avito.ma/')
    avitoSrapper = avitoSrapperTool(
        driver=driver, search_url=general_search_url,csv_file_path=csv_file_path,start_page_index=start_page_index,last_page_index=last_page_index)
    time.sleep(3)
    avitoSrapper.search_page_index = search_page_index if search_page_index else int(input('start page index (-1 for random): '))
    avitoSrapperTool.create_new_csv_file(avitoSrapper.csv_file_path)
    start_time = datetime.now()  # to calculate speed
    while True:
        if avitoSrapper.extracted_listings_count % 15:
            # suspend after every 15 extraction so you don't get blocked
            time.sleep(random.randint(5, 10))

        try:
            avitoSrapper.next_page()
            listings = avitoSrapper.get_page_urls()
            for listing in listings:
                time.sleep(random.randint(1, 3))
                item = avitoSrapper.get_info(listing)
                avitoSrapper.save_to_csv(item)

            speed = avitoSrapper.extracted_listings_count / \
                (datetime.now() - start_time).total_seconds()  # Speed
            print('Speed', speed, 'row/second..')
            print('in 24h: ~', int(speed*24*60*60), 'row.')
        except Exception as exc:
            print(exc)
            driver.refresh()
            pass
    driver.close()
    driver.quit()

if __name__ == "__main__":
    main()
