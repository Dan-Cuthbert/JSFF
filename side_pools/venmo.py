from venmo_api import Client
from credentials import getToken
import config

# Enter all users' venmo IDs
venmo_ids = {'rgillies28':'Ryan-Gillies',
             'TomGill':'Thomas-Gillies-4',
             'dcuth':'Dan-Cuthbert',
             'aconstant10':'Andrew-Constant',
             'BobTheChamp2016':'B-Ross',
             'egillies21':'Eric-Gillies',
             'tevancho':'tom-evancho',
             'tflora':'tflora',
             'ChristianSwagner':'ChristianWagner',
             'S_Shaffer':'Stephen-Shaffer-20',
             'ConePollos':'Alex-Cohen-21',
             'bengalball':'Leanne-Evancho'
             }

def payout(username,payout,pool):
    # Get 1Password uuid for Venmo API credential. Get access token stored in 1Password and connect to Venmo client
    venmo_access_token = getToken(config.venmo_uuid)
    venmo = Client(access_token=venmo_access_token)
    recipient = venmo.user.get_user_by_username(username).id
    venmo.payment.send_money(amount=payout,note=pool,target_user_id=recipient)
    return 
