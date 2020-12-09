import cx_Oracle
import pyodbc
import pandas as pd
import openpyxl
from copy import copy
from openpyxl.utils.dataframe import dataframe_to_rows

dsn_tns = cx_Oracle.makedsn('DPE', '1521', service_name='ORCL')
conn_ora = cx_Oracle.connect(user='LPU', password='Ring43', dsn=dsn_tns)
conn_ms = pyodbc.connect("""Driver={SQL Server Native Client 11.0};Server=dpx\mssqlserver2012;
                Database=my_base;uid=srz_admin;pwd=srz_admin""")

params = {"fam": 'Львов', "im": 'Максим', "ot": 'Александрович'}

sql_ora = '''select FIO, to_char(dr, 'dd.mm.yyyy') DR, POLIS, SMO, PROF, MKB, MKB_NAME, PERIOD, SUMV, SUMP, MO, USL_OK from LPU.VW_LPU_ZAPROS_ORGAN t where fam = :fam and im = :im and ot = :ot'''
sql_ms = '''SELECT FIO, CONVERT(VARCHAR, dr, 104) DR, POLIS, SMO, PROF, MKB, MKB_NAME, PERIOD, SUMV, SUMP, MO, USL_OK FROM [IESDB].[dbo].[K_V_Zapros_Organ] where fam = ? and im = ? and ot = ?'''

df_ora = pd.read_sql(sql_ora, con=conn_ora, params=params)
df_ms = pd.read_sql(sql_ms, con=conn_ms, params=params.values())
df = df_ora.append(df_ms)  # pd.concat([df_ms, df_ora])

# with pd.ExcelWriter('111.xlsx') as writer:
#     df.to_excel(writer, sheet_name='Приложение 7', index=False)
#     writer.save()

wb = openpyxl.load_workbook('zapros_template.xlsx')
ws = wb.active
rows = dataframe_to_rows(df, index=False, header=None)

for r_idx, row in enumerate(rows, 8):
    ws.insert_rows(r_idx + 1, 1)
    for c_idx, value in enumerate(row, 1):
        ws.cell(row=r_idx, column=c_idx, value=value)
        ws.cell(row=r_idx, column=c_idx)._style = copy(ws.cell(row=r_idx - 1, column=c_idx)._style)
wb.save('zapros_template1.xlsx')
