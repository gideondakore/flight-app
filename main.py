from flight_search import FlightSearch
from notification_manager import NotificationManager


flight_search = FlightSearch()

notification = NotificationManager(flight_search)
notification.notify()



