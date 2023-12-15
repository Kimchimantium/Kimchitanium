import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import json, time, os


class GetUserCity:
    def __init__(self):
        self.searching = True
        self.ZIGBANG_URL = 'https://www.zigbang.com/home/apt/map?latitude=37.5663306&longitude=126.9782351&zoom=9'
        self.chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(self.chrome_options)
        self.city_names_list = []
        time.sleep(2)

    def get_city_list(self):
        """search city names available in Seoul"""
        self.driver.get(self.ZIGBANG_URL)
        city_name_elements = self.driver.find_elements(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div[6]')
        for city_name in city_name_elements:
            self.city_names_list = city_name.text.split('\n')[::2]

    def save_city_list(self):
        """save the city_names_list as text"""
        if not os.path.exists('city_list.txt'):
            with open('city_list.txt', 'w', encoding='utf-8') as file:
                json.dump(self.city_names_list, file, ensure_ascii=False)

    def user_input_city(self):
        """get input city from user"""
        city_index = None
        city_input = None
        while self.searching:
            city_input = input('Which city do u want property info of? type "stop" to end the code\n')
            if city_input in self.city_names_list:
                city_index = self.city_names_list.index(city_input) + 1
                break
            elif city_input == 'stop':
                self.searching = False
                break
            else:
                print('not an available city, try again')
                pass
        if city_index is not None:
            return city_index, city_input
        else:
            return city_input


    def click_city(self, city_index):
        """click the input city to see the properties in it
        returns the url of the city selected"""
        city_to_click = self.driver.find_element(By.XPATH, f'//*[@id="__next"]/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div[6]/div[{city_index}]')
        city_to_click.click()
        time.sleep(1)
        return self.driver.current_url
