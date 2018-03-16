import json
import requests

class SharepointClient(object):
    """Sharepoint online client"""

    def __init__(self, site, tenant_id, resource, client_id, client_secret):
        self.site = site
        self.tenant_id = tenant_id
        self.resource = resource
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_request_url = "https://accounts.accesscontrol.windows.net/%s/tokens/OAuth/2" % (self.tenant_id)

    def getToken(self):
        headers = {
        'Content-Type' : 'application/x-www-form-urlencoded'
        }
        payload = {
            'grant_type' : 'client_credentials',
            'client_id' : '%s@%s' % (self.client_id, self.tenant_id),
            'client_secret': self.client_secret,
            'resource': '%s/%s@%s' % (self.resource, self.site, self.tenant_id)
            }

        r = requests.post(url=self.token_request_url, data=payload, headers = headers)
        response = json.loads(r.text)
        return response['access_token']




