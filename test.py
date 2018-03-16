import json
import datetime
import requests
from SharepointClient import SharepointClient

client_id = "b8a4edf8-cefe-4963-9e3a-41a75027e45f"
client_secret = "Fel2tFzaF5U0zB4E34PrgdF5sCERiJZbF89f8HGfAuc="
tenant_id = "78492a87-3b48-4c10-adc5-782729cfc504"
resource = "00000003-0000-0ff1-ce00-000000000000"
site = 'acdc1805.sharepoint.com'

sharepointClient = SharepointClient(site, tenant_id, resource, client_id, client_secret)


def getDefaultHeaders(withRequestDigest = False):
    auth_token  = sharepointClient.getToken()
    header = {
        'Accept' : 'application/json;odata=verbose',
        'Content-Type' : 'application/json;odata=verbose',
        'Authorization' : 'Bearer ' + auth_token
        }
    if withRequestDigest:
        header['X-RequestDigest'] = getDigestInfo()
    return header


def test():
    r = requests.get(url = "https://%s/_api/web/lists(guid'343f9361-3eb7-48de-aa2e-7197122bd9c1')" % (site), headers = getDefaultHeaders())
    return r.text

def getListItemEntityTypeFullName(title):
    r = requests.get(url = "https://%s/_api/web/lists/GetByTitle('%s')" % (site,title), headers = getDefaultHeaders())
    reesponse = json.loads(r.text)
    return reesponse['d']['ListItemEntityTypeFullName']

def getDigestInfo():
    r = requests.post(url = "https://%s/_api/contextinfo" % (site), headers = getDefaultHeaders())
    response = json.loads(r.text)
    return response['d']['GetContextWebInformation']['FormDigestValue']

def addSession(playerID, game, duration, dumbbellsWeight,calories):
    body = {
        '__metadata': {
            'type': 'SP.Data.SessionsListItem'
            },
            'ID_x002d_nummerId' : str(playerID),
            'Game': game,
            'Dumbbel_x0020_Weight': dumbbellsWeight,
            'Calories': calories,
            'Duration': duration
        }
    r = requests.post(url = "https://%s/_api/web/lists/GetByTitle('Sessions')/items" % (site), data = json.dumps(body), headers = getDefaultHeaders(withRequestDigest= True))
   
    return json.loads(r.text)


test = addSession(playerID=2, game='stepmania', duration= 300, dumbbellsWeight=30, calories=300)
print(test)