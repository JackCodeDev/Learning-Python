import requests
from datetime import datetime
import smtplib

MY_EMAIL = "jack.helpenglish@gmail.com"
MY_PASSWORD = "hxplsbihmekioied"

MY_LATITUDE = 21.028511
MY_LONGITUDE = 105.804817


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LATITUDE-5 <= iss_latitude and iss_longitude <= MY_LONGITUDE:
        return True


def is_night():
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0

    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    print(data)
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


if is_iss_overhead() and is_night():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL,MY_PASSWORD)
    connection.sendmail(
        from_addr= MY_EMAIL,
        to_addrs= MY_EMAIL,
        msg="Subject:Look up👆👆\n\nThe ISS above you on the sky."
    )
