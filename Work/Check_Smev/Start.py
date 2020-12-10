import pyodbc
import pandas as pd
import datetime
import schedule, time
import smtplib
import configparser
from email.mime.text import MIMEText
from email.header import Header

SQL = """SELECT CASE WHEN DATEDIFF(day, MAX(date), GETDATE()) > 1 THEN 'PROBLEM' ELSE 'OK' END STATUS
         FROM   [IESDB].[IES].[R_NSI_SMEV_SERVICE_BACK]"""
CONN_STR = """Driver={SQL Server};
                                Server=dpx\mssqlserver2012;
                                Database=my_base;
                                uid=srz_admin;
                                pwd=srz_admin"""


#  Проверка активности по последней дате
def Smev_have_PROBLEM():
    try:
        conn = pyodbc.connect(CONN_STR)
        df = pd.read_sql_query(SQL, conn)
    except Exception as pe:
        Write_Log('Ошибка подключения к DBX\MSSQLSERVER2012')
        print(pe)
        Write_Log('Уведомляем о проблеме на почту')
        Send_problem_email('Проверка СМЭВ. Ошибка подключения к DBX\MSSQLSERVER2012\n\n' + str(pe))
        return False
    if df.iloc[0]['STATUS'] == 'PROBLEM':
        flag = True
    else:
        flag = False
    return flag


def Write_Log(text):
    t = f'{datetime.datetime.now().strftime("%d-%m-%Y %H-%M")} - {text}'
    print(t)
    with open('history.log', 'a') as fd:
        fd.write(t + "\n")


def Check_Smev():
    if Smev_have_PROBLEM():
        Write_Log('Есть проблемы. Отправляем на почту')
        Send_problem_email()


def Send_problem_email(txt=''):
    parser = configparser.ConfigParser()
    parser.read('start.ini')
    host = parser.get('mail', 'host')
    port = parser.get('mail', 'port')
    to = parser.get('mail', 'to_users').split(',')

    if txt == '':
        msg = MIMEText('Отсутствуют запросы с ЕПГУ о стоимости услуг более одного дня\n\n' + SQL, 'plain', 'utf-8')
    else:
        msg = MIMEText(txt, 'plain', 'utf-8')
    msg['Subject'] = Header("Проблемы в работе СМЭВ", 'utf-8')
    msg['From'] = parser.get('mail', 'from_email')
    msg['To'] = ", ".join(to)

    s = smtplib.SMTP(host, port, timeout=10)
    # s.set_debuglevel(1)
    try:
        s.sendmail(msg['From'], to, msg.as_string())
    finally:
        s.quit()


Write_Log('Сервис проверки активности по запросам стоимости услуг с ЕПГУ')
Write_Log('Выполняется во воремя указанное в start.ini. Отправляет на почту админу сообщение если запросов не было более одного дня"')
Write_Log('--------------')
Check_Smev()

parser = configparser.ConfigParser()
parser.read('start.ini')
signal_time = parser.get('main', 'signal_time')

# schedule.every(diff_hour).hours.do(Check_Smev)
schedule.every().day.at(signal_time).do(Check_Smev)
while True:
    schedule.run_pending()
    time.sleep(1)

# pip install pyodbc
# pip install pandas
# pip install schedule
