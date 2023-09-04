from venmo_api import Client
from credentials import getToken
import config

# Get 1Password uuid for Venmo API credential. Get access token stored in 1Password and connect to Venmo client
venmo_access_token = getToken(config.venmo_uuid)
venmo = Client(access_token=venmo_access_token)

# Enter all users' venmo IDs
venmo_ids = {'rgillies28':'ryan-gillies',
             'tomgill':'thomas-gillies-4',
             'dcuth':'dan-cuthbert',
             'aconstant10':'andrew-constant',
             'BobTheChamp2016':'b-ross',
             'egillies21':'eric-gillies',
             'tevancho':'tom-evancho',
             'tflora':'tflora',
             'ChristianSwagner':'christianwagner',
             'S_Shaffer':'Stephen-Shaffer-20',
             'ConePollos':'alex-cohen-21',
             'bengalball':'Leanne-Evancho'
             }

def payout(username,payout,pool):
    recipient = venmo.user.get_user_by_username(venmo_ids[username]).id
    venmo.payment.send_money(amount=payout,note="JSFF - "+pool,target_user_id=recipient)
    print('Payment successfully sent:'+username+'-'+payout+'-'+pool)
    return 
