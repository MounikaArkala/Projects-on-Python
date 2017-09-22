from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACf0d1ec6d1d3be5c1b4e8e6dab6cedda7"
# Your Auth Token from twilio.com/console
auth_token  = "5246efacf3bc83c387d2c92df8616d30"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14697349118", 
    from_="+14695186918",
    body="Hello nehu dear this is me Mounika Arkala, Good Morning! did you wake up")

print(message.sid)
