from suds.client import Client
url="http://wsf.cdyne.com/WeatherWS/Weather.asmx?WSDL"
client = Client(url)
print client ## shows the details of this service

result = client.service.GetWeatherInformation() 
print result 