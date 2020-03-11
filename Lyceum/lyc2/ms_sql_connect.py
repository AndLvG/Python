import pypyodbc
import pandas as pd

cnxn = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        "Server=server_name;"
                        "Database=db_name;"
                        "uid=User;pwd=password")
df = pd.read_sql_query('select * from table', cnxn)