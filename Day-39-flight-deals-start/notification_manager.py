from twilio.rest import Client

TWILIO_SID = "AC80f187f805ec2348f769f3ac2c4ddd93"
TWILIO_AUTH_TOKEN = "cbd00a938a2973b6ff7b5a60e958848f"
TWILIO_VIRTUAL_NUMBER = "+19206718445"
TWILIO_VERIFIED_NUMBER = "+84389675880"


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
