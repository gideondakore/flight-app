import requests
from flight_data import FlightData
from data_manager import DataManager

class FlightSearch:
    search_results = []

    def __init__(self):
        self.url = "https://test.api.amadeus.com/v1/shopping/flight-destinations"
        self.flight_data = FlightData()


    def search_price(self):
        sheety_data = DataManager()
        sheety_flight_data = sheety_data.sheety_get_data()

        headers = {
            "Authorization": f"Bearer {self.flight_data.access_token_data}"
        }

        for city in sheety_flight_data["prices"]:
            params = {
                "origin": city["iataCode"],
                "maxPrice": city["lowestPrice"]
            }

            response = requests.get(url=self.url, params=params, headers=headers)
            data = response.json()

            if "errors" in data and len(data["errors"]) > 0:
                if data["errors"][0]["code"] in [38192, 38191]:
                    self.flight_data.access_token()
                    self.search_price()


            if "data" in data and len(data["data"]) > 0:
                # if data["data"][0]["origin"] == city["iataCode"]:
                #     self.search_results.append(data)
                new_flight_data = [flight for flight in data["data"] if flight["origin"] == city["iataCode"]]
                self.search_results.extend(new_flight_data)

        return self.search_results









