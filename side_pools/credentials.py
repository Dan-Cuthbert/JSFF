from onepassword import OnePassword

op = OnePassword()

def getToken(uuid):
    access_token = op.get_item(uuid, fields="access_token")
    return access_token["access_token"]
