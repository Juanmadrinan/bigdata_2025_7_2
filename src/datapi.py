import json
import requests
import pandas as pd

class DatApi:
    def __init__(self):
        self.apiURL = "https://v6.exchangerate-api.com/v6/4b48a13bb3b863e8af0a9c04/latest/USD"

    exchangeRate = {

    }

    def getData(self):

        headers = {
            'User-Agent': 'Mozilla/5.0'
        }

        get = requests.get(self.apiURL, headers=headers)
        deserialized = json.loads(get.text)
        exchangeRate = deserialized["conversion_rates"]
        df = pd.DataFrame(exchangeRate, index=[0])
        return df
