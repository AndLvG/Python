from suds.client import Client
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

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
# result = client.service.SendXmlFile2(zapros)
result = """
<SMO_ZAPROS>
  <OTVET>
    <EERP>-7</EERP>
    <REPL>В локальной базе данные не найдены. Требуется запрос в Центральный сегмент застрахованных.
Такой запрос возможен только через 'Автоматическую индентификацию застрахованных' в режиме файлового обмена</REPL>
  </OTVET>
</SMO_ZAPROS>
"""
print(result)

# ===== ElementTree
# root = ET.parse('xml_file.xml').getroot()
# root = ET.fromstring(result)
# print(root.tag)

# for x in root[0]:
#     print(x.tag, x.attrib, x.text)
# for x in root.findall('OTVET'):
#     item = x.find('EERP').text
#     price = x.find('REPL').text
#     print(item, price)


#
#
# # You can use BeautifulSoup:
x = """<foo>
   <bar>
      <type foobar="1"/>
      <type foobar="2"/>
   </bar>
</foo>"""

# y = BeautifulSoup(x, 'xml')
# print(y.foo.bar.type["foobar"])
#
# print(y.foo.bar.findAll("type"))
#
# print(y.foo.bar.findAll("type")[0]["foobar"])
# print(y.foo.bar.findAll("type")[1]["foobar"])

y = BeautifulSoup(result, 'xml')
print(y.SMO_ZAPROS.OTVET.REPL)
print(y.SMO_ZAPROS.OTVET.REPL.text)

