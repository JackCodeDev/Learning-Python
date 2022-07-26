import requests
from datetime import datetime, timedelta
from flight_data import FlightData
from pprint import pprint

location_endpoints = "https://tequila-api.kiwi.com"
API_FLIGHT ="agQgVX-t76AT7W0W69uxHfFc2m_Wm0Zz"


class FlightSearch:

    def get_flight_search_location(self, city_name):
        headers = {
            "apikey": API_FLIGHT
        }
        location_params = {
            "term": city_name,
            "location_types": "city",

        }
        response = requests.get(url=f"{location_endpoints}/locations/query",
                                params=location_params, headers=headers)

        response.raise_for_status()
        code = response.json()["locations"][0]["code"]
        return code

    def check_flight(self, origin_city_code, fly_to_city, date_from, date_to):
        """
        :param fly_to_city: city_name
        :param date_from: dd/mm/yyyy
        :param date_to: dd/mm/yyyy
        :return: price
        """
        headers = {
            "apikey": API_FLIGHT
        }
        location_params = {
            "fly_from": origin_city_code,
            "fly_to": fly_to_city,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD",
        }
        response = requests.get(url=f"{location_endpoints}/v2/search",
                                params=location_params, headers=headers)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {fly_to_city}.")
            return None
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: ${flight_data.price} from {flight_data.out_date} "
              f"to {flight_data.return_date}")
        return flight_data

ORIGIN_CITY_IATA = "HAN"
DESTINATION_CITY_IATA= "SGN"
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
flight_search = FlightSearch()
flight_info = flight_search.check_flight(
    ORIGIN_CITY_IATA,
    DESTINATION_CITY_IATA,
    date_from=tomorrow,
    date_to=six_month_from_today
)
print(flight_info)
new_data = FlightSearch()
new_data.get_flight_search_location("Paris")

