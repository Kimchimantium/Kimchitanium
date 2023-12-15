from data_to_json import DataToJson as dj
import requests, json
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
import json, time

ZIGBANG_URL = 'https://www.zigbang.com/home/apt/map?latitude=37.5663306&longitude=126.9782351&zoom=9'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(chrome_options)
driver.get('https://www.naver.com')



