import requests

server = "http://192.168.32.2/it/WebServices/StrahPrinService.asmx"
headers = {"SOAPAction": "http://192.168.32.2/it/WebServices/SendXmlFile2",
           "Content-Type": "text/xml; charset=utf-8"}
body = '''
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <SendXmlFile2 xmlns="http://192.168.32.2/it/WebServices/">
      <xmlInput>&lt;SMO_ZAPROS&gt;&lt;ZGLV&gt;&lt;DATA&gt;2020-06-03&lt;/DATA&gt;&lt;FILENAME&gt;Z400109_01_68215.xml&lt;/FILENAME&gt;&lt;/ZGLV&gt;
&lt;PERSON&gt;&lt;FAM&gt;Побережный&lt;/FAM&gt;&lt;IM&gt;Ростислав&lt;/IM&gt;&lt;OT&gt;Васильевич&lt;/OT&gt;&lt;W&gt;1&lt;/W&gt;&lt;DR&gt;1960-08-16&lt;/DR&gt;&lt;DOCTP&gt;14&lt;/DOCTP&gt;&lt;DOCS&gt;46 06&lt;/DOCS&gt;&lt;DOCN&gt;988652&lt;/DOCN&gt;&lt;ENP&gt;5051930833000693&lt;/ENP&gt;&lt;SNILS&gt;009-970-230 63&lt;/SNILS&gt;&lt;/PERSON&gt;&lt;/SMO_ZAPROS&gt;
</xmlInput>
    </SendXmlFile2>
  </soap:Body>
</soap:Envelope>
'''

response = requests.post(server, data=body.encode('utf-8'), headers=headers)
print(response.text)
