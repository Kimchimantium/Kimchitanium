from data_to_json import DataToJson as dj
from get_user_city_url import GetUserCity as guc
from google_sheet_upload import GoogleSheetify as gs
import requests, json
from oauth2client.service_account import ServiceAccountCredentials
import gspread

# CONSTANTS
GOOGLE_API_KEY = 'AIzaSyDoj5-kpQMBvTkkrsG2BLvq044YjnCT7K0'
GOOGLE_OAUTH_ID = '947166277127-o9r7f2ph1lo8ee5e63ru5tbqtna6nsfk.apps.googleusercontent.com'
GOOGLE_OAUTH_PWD = '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'
GOOGLE_SERVICE_ACCOUNT = 'dukso123@mythical-device-167200.iam.gserviceaccount.com'
SHEET_ID = '19OZwUKqdMshosCL7bGbHa-dlSGAtIh30p75Ye0rJJhM'

searching = True
guc, dj, gs = guc(), dj(), gs()
while searching:
    # getting url of the selected city
    guc.get_city_list()
    guc.save_city_list()
    try:
        city_index, city_input = guc.user_input_city()
    except ValueError:
        break
    city_url = guc.click_city(city_index)
    # get and save chosen city's property data as json list
    dj.go_to_url(url=city_url)
    property_list = dj.property_data_to_list()
    property_dict = dj.property_list_to_dict(city_input)
    if not property_dict:
        continue
    dj.dump_json(city_input)

# transfer data to google spreadsheet
property_json = dj.load_json()
print(f'added data successfully\ndata added: {property_json}')
gs.send_to_sheet(property_json)
