import pyodbc
import pandas as pd

CONN_STR = """Driver={SQL Server Native Client 11.0};
                                Server=dpx\mssqlserver2012;
                                Database=my_base;
                                uid=srz_admin;
                                pwd=srz_admin"""

conn = pyodbc.connect(CONN_STR)
df = pd.read_sql("""SELECT IESDB.dbo.lv_GetXML() AS x""", conn)
xml_file = df.iloc[0]['x']
with open("D:\\1\\ksg23_2.xml", "w") as xml_writer:
    xml_writer.write(xml_file)
print('Готово')

