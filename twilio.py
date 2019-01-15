# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import scraping_variables


# Your Account Sid and Auth Token from twilio.com/console
account_sid = scraping_variables.account_sid1
auth_token = scraping_variables.auth_token1
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Test",
                     from_= scraping_variables.twinum,
                     to= scraping_variables.num
                 )






