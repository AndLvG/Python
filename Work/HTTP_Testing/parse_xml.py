from suds.client import Client
import xml.etree.ElementTree as ET
from xml.dom import minidom
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
result = client.service.SendXmlFile2(zapros)
print(result)

# root = ET.parse('xml_file.xml').getroot()
root = ET.fromstring(result)
# print(root.tag)

for x in root[0]:
    print(x.tag, x.attrib, x.text)
#
#
# xmldoc = minidom.parse(result)
# itemlist = xmldoc.getElementsByTagName('OTVET')
# print(len(itemlist))
# print(itemlist[0].attributes['name'].value)
# for s in itemlist:
#     print(s.attributes['name'].value)
#
#
#
# # You can use BeautifulSoup:
# x="""<foo>
#    <bar>
#       <type foobar="1"/>
#       <type foobar="2"/>
#    </bar>
# </foo>"""
#
# y=BeautifulSoup(x)
# >>> y.foo.bar.type["foobar"]
# u'1'
#
# >>> y.foo.bar.findAll("type")
# [<type foobar="1"></type>, <type foobar="2"></type>]
#
# >>> y.foo.bar.findAll("type")[0]["foobar"]
# u'1'
# >>> y.foo.bar.findAll("type")[1]["foobar"]
# u'2'
