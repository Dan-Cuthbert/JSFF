from venmo_api import Client
from credentials import getToken
import config

# Get 1Password uuid for Venmo API credential. Get access token stored in 1Password and connect to Venmo client
venmo_access_token = getToken(config.venmo_uuid)
venmo = Client(access_token=venmo_access_token)

# Get user ID for given username
recipient = venmo.user.get_user_by_username('Samantha-Pezzimenti').id

# Send money from default payment source
venmo.payment.send_money(amount=1.00,note="test",target_user_id=recipient)

# payment_methods = venmo.payment.get_payment_methods()
# for p in payment_methods:
#     print(p)
