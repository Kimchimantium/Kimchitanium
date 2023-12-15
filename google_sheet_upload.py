import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSheetify:
    def __init__(self):
        # default gspread scope - available in doc
        self.scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
        ]
        # how to get the key json file: google.com/cloud -> console -> IAM -> service accounts ->
        # add_key -> create key as json
        self.json_key_path = "google_service_account_key.json"

        # get access using scope and key_path_json
        self.credential = ServiceAccountCredentials.from_json_keyfile_name(self.json_key_path, self.scope)
        self.gspread_credit = gspread.authorize(self.credential)

        # project spreadsheet's url
        self.spreadsheet_url = "https://docs.google.com/spreadsheets/d/19OZwUKqdMshosCL7bGbHa-dlSGAtIh30p75Ye0rJJhM/edit#gid=0"
        doc = self.gspread_credit.open_by_url(self.spreadsheet_url)
        # parameter as sheet's page name
        self.sheet = doc.worksheet("sheet1")

    def send_to_sheet(self, property_json):
        # jsoned list of dictionarys' dictionary's keys as the first row of the sheet
        headers = list(property_json[0].keys())
        values = [[row_data[col] for col in headers] for row_data in property_json]
        self.sheet.update('A1', [headers] + values)
