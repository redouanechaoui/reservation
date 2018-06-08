from twilio.rest import TwilioRestClient
class Notification():
    def __init__(self, message, number):
        self.message = message
        self.number = number

    def send_text_message(message, number):
        account_sid = "AC18609aae178f4cc17a70e7e4cb9a2e28"
        auth_token = "cb76fd04880163697e6e92321191ffb3"
        client = TwilioRestClient(account_sid, auth_token)

        message = client.messages.create(
            to=number,
            from_="+18504047730",
            body=message)

        message.sid
