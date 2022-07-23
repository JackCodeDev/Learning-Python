import smtplib
from datetime import datetime
import pandas
import random


MY_EMAIL = "Your email"
MY_PASSWORD = "Your Password"
RECEIVER = "Receiver email"

today = datetime.now()
month = today.month
day = today.day
today_tuple = (month, day)

data = pandas.read_csv("birthday.csv")

birthday_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[name]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.ehlo()

        connection.login(MY_EMAIL, MY_PASSWORD)

        subject = "Happy Birthday"
        body = contents

        msg = f"Subject:{subject}\n\n{body}"

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=msg)


# MY_EMAIL = "jack.helpenglish@gmail.com"
# MY_PASSWORD = "hxplsbihmekioied"
# RECEIVER = "nguyensonhdtk94@gmail.com"
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.ehlo()
#     connection.starttls()
#     connection.ehlo()
#
#     connection.login(MY_EMAIL, MY_PASSWORD)
#
#     subject = "Hello!"
#     body = "How are you?"
#
#     msg = f"Subject:{subject}\n\n{body}"
#
#     connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECEIVER, msg=msg)
