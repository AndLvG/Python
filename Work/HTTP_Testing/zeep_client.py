from suds.client import Client

url = "http://192.168.32.2/it/WebServices/StrahPrinService.asmx?WSDL"
client = Client(url)
print(client)  ## shows the details of this service

result = client.service.SendXmlFile2()
print(result)
