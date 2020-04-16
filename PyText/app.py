from twilio.rest import Client
# Your new Phone Number is +18635324886
account_sid = "ACae8774929abf86f617eb200a3a9c30a1"
account_token = "850d9dbc0a422f735d6122ea20135594"
client = Client(account_sid, account_token)

call = client.messages.create(
    to="16174356637",
    from_="18635324886",
    body="I love you ya,from code exercise"
)

print(call)
