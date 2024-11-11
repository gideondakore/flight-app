import requests

USERNAME = "YOUR USERNAME"
PASSWORD = "YOUR PASSWORD"

class DataManager:
    def __init__(self):
        self.sheety_url = "YOUR SHEETY URL"
        self.sheety_headers = {
    "Authorization": "Basic SHEETY ACCESS KEY",
    "Content-Type": "application/json"
}


    def sheety_get_data(self):
        sheety_response = requests.get(url=f"{self.sheety_url}", headers=self.sheety_headers, auth=(USERNAME, PASSWORD))
        data = sheety_response.json()
        return data

    def sheety_put_data(self, city_name: str):
        city_id = int

        sheet_data = self.sheety_get_data()

        for city in sheet_data["prices"]:
            if city_name.lower() == (city["city"]).lower():
                city_id = city["id"]

        sheety_body = {
            "price": {
                "iataCode": city_name
            }
        }

        sheety_response = requests.put(url=f"{self.sheety_url}/{city_id}", json=sheety_body, headers=self.sheety_headers,
                                       auth=(USERNAME, PASSWORD))

