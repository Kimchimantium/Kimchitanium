import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import json


class DataToJson:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(self.chrome_options)

    def go_to_url(self, url='https://www.zigbang.com/home/apt/locals/30'):
        self.driver.get(url)
    def property_data_to_list(self):
        """ returns a list of real estates"""
        sub_source = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div/div')
        real_estate_list = []
        for n in range(5):
            xpath = f'//*[@id="__next"]/div[2]/div/div[2]/div/div/div[2]/div/div[6]/div/div[6]/div[{3+(2*n)}]'
            real_estate_data = sub_source.find_elements(By.XPATH, xpath)
            for element in real_estate_data:
                real_estate_list.append(element.text.split('\n'))
        return real_estate_list

    def property_list_to_dict(self, city_input):
        """returns a list containing dictionaries of each property's features"""
        real_estate_list = self.property_data_to_list()
        real_estate_dicts = []
        for n in real_estate_list:
            if len(n) == 5:
                price = n[3]
            elif len(n) == 6:
                price = n[4]
            else:
                print(f'no property available in {city_input}')
                return False
            size = n[1].split('·')
            size = size[0].strip()
            real_estate_dict = {
                'property_name': n[0],
                'property_size': size,
                'property_town': n[2],
                'property_price': price
                }
            real_estate_dicts.append(real_estate_dict)
        return real_estate_dicts

    def dump_json(self, city_input):
        """write or append if not exist as real_estate.json"""
        try:
            with open('real_estate.json', 'r', encoding='utf-8') as file:
                previous_dict = json.load(file)
        except FileNotFoundError:
            previous_dict = []

        new_real_estate_dicts = self.property_list_to_dict(city_input)

        try:
            previous_dict.extend(new_real_estate_dicts)
        except AttributeError:
            previous_dict = new_real_estate_dicts

        with open('real_estate.json', 'w', encoding='utf-8') as file:
            json.dump(previous_dict, file, indent=2, ensure_ascii=False)

        print(f'File written successfully as real_estate.json')
    def load_json(self):
        with open('real_estate.json', 'r') as file:
            return json.load(file)
