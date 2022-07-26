from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager
#This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

data_new = DataManager()
sheet_data = data_new.get_destination_data()
flight_search = FlightSearch()
ORIGIN_CITY_IATA = "LON"

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
notification_manager = NotificationManager()

print(sheet_data)
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_flight_search_location(row["city"])
    print(sheet_data)
    data_new.destination_data = sheet_data
    data_new.update_destination_codes()

today = datetime.now() + timedelta(1)
six_month_from_today = datetime.now() + timedelta(6 * 30)

for destination in sheet_data:
    flight = flight_search.check_flight(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        date_from=today,
        date_to=six_month_from_today,
    )

    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}"
            f"-{flight.origin_airport} to {flight.destination_city}"
            f"-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
    )

