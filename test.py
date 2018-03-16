from SharepointClient import SharepointClient

client_id = "b8a4edf8-cefe-4963-9e3a-41a75027e45f"
client_secret = "Fel2tFzaF5U0zB4E34PrgdF5sCERiJZbF89f8HGfAuc="
tenant_id = "78492a87-3b48-4c10-adc5-782729cfc504"
resource = "00000003-0000-0ff1-ce00-000000000000"
site = 'acdc1805.sharepoint.com'

client = SharepointClient(site, tenant_id, resource, client_id, client_secret)

print(client.getToken())