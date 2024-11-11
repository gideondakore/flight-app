import requests

class FlightData:

    def __init__(self):
        self.armadeus_url_token = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.armadeus_api_headers = {
            "Content-type": "application/x-www-form-urlencoded"
        }
        self.armadeus_api_data = {
            "grant_type": "client_credentials",
            "client_id": "ARMADEUS API KEY",
            "client_secret": "ARMADEUS API SECRET"
        }
        self.access_token_data = self.access_token()

    def access_token(self):

        armadeus_response = requests.post(url=self.armadeus_url_token, data=self.armadeus_api_data, headers=self.armadeus_api_headers)
        data = armadeus_response.json()

        self.access_token_data =  data["access_token"]
        return data["access_token"]

    def armadeus_iata(self, country_name: str):
        armadeus_data = {
            "keyword": country_name,
            "max": 1
        }

        armadeus_headers = {
            "Authorization": f"Bearer {self.access_token_data}"
        }


        armadeus_url_city_search = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

        armadeus_api_response = requests.get(url=armadeus_url_city_search, params=armadeus_data,
                                             headers=armadeus_headers)

        data = armadeus_api_response.json()

        if "errors" in data and len(data["errors"]) > 0:
            if data["errors"][0]["code"] in [38192, 38191]:
                self.access_token()
                self.armadeus_iata(country_name)
        else:
            print("ARMADEUS: ", data)
            return data

