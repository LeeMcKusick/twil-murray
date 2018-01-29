from twilio.rest import Client
from datetime import datetime
import random

# Your Account SID from twilio.com/console
#account_sid = "123456789"
account_sid = input("Account SID: ")
# Your Auth Token from twilio.com/console
#auth_token = "abcdefghij"
auth_token  = input("Auth Token: ")

client = Client(account_sid, auth_token)

theDate = datetime.now().strftime('%m/%d/%Y')
theTime = datetime.now().strftime('%I:%M %p')

#twilioPhone = "5555555555"
twilioPhone = input("What is your Twilio number? (1231231234): ")

sendToPhone = input("What is your phone number? (1231231234): ")

message = client.messages.create(
    to="+1"+sendToPhone, 
    from_="+1"+twilioPhone,
    body="It is " + theTime + " on " + theDate + ". Here\'s Bill Murray.",
	media_url="https://www.fillmurray.com/"+str(random.randint(2, 12))+"00/"+str(random.randint(2, 12))+"00")

message2 = client.messages(message.sid).fetch()

print(message2.body)
