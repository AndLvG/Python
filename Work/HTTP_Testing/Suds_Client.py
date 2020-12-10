from suds.client import Client

url = "http://192.168.32.2/it/WebServices/StrahPrinService.asmx?WSDL"
client = Client(url)
# print(client)  ## shows the details of this service

zapros = """
<SMO_ZAPROS>
<ZGLV>
<DATA>2020-06-03</DATA>
<FILENAME>Z400109_01_68215.xml</FILENAME>
</ZGLV>
<PERSON><FAM>Побережный</FAM><IM>Ростислав</IM><OT>Васильевич</OT><W>1</W><DR>1960-08-16</DR><DOCTP>14</DOCTP><DOCS>46 06</DOCS><DOCN>988652</DOCN><ENP>5051930833000693</ENP><SNILS>009-970-230 63</SNILS></PERSON></SMO_ZAPROS>
"""
result = client.service.SendXmlFile2(zapros)
print(result)
