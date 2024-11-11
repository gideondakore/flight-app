from twilio.rest import Client
from flight_search import FlightSearch


class NotificationManager:
  def __init__(self, flight_search_results:FlightSearch):
    self.account_sid = 'TWILIO SID KEY'
    self.auth_token = 'TWILIO AUTH TOKEN'
    self.flight_search_results = flight_search_results.search_price()


  def notify(self):
    client = Client(self.account_sid, self.auth_token)
    if len(self.flight_search_results) > 0:
      for flight in self.flight_search_results:
        message_body = (f"Low price alert! Only ${flight["price"]["total"]} to fly from {flight["origin"]}"
                        f" to {flight["destination"]} on {flight["departureDate"]} until {flight["returnDate"]}")

        message = client.messages.create(
          from_='whatsapp:TWILIO NUMBER',
          body= message_body,
          to='whatsapp:YOUR VERIFIED TWILIO NUMBER'
        )
        print(message.sid)
