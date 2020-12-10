from datetime import datetime
import smtplib
import configparser

parser = configparser.ConfigParser()
parser.read('start.ini')


def send_mail(txt):
    host = parser.get('mail', 'host')
    port = parser.get('mail', 'port')
    subject = "Информация о логах WinSCP"
    to = parser.get('mail', 'to_users')
    fr = parser.get('mail', 'from_email')
    txt = 'Присутствуют критические ошибки в логе\n\n' + txt
    body = "\r\n".join((
        "From: %s" % fr,
        "To: %s" % to,
        "Subject: %s" % subject,
        "",
        txt
    )).encode('cp1251')
    smtpObj = smtplib.SMTP(host, port)
    # smtpObj.starttls()
    # smtpObj.login(fr, 'rjppfy.dt')
    smtpObj.sendmail(fr, [to], body)
    smtpObj.quit()


with open(parser.get('main', 'path'), "r", encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()
    dtime = datetime.now()
    text = []
    days_to_read = int(parser.get('main', 'days_to_read'))
    for str in lines:
        if 'Exception' in str or 'denied' in str:
            dt = datetime.strptime(str[2:12], '%Y-%m-%d')
            if (dtime - dt).days <= days_to_read:
                text.append(str)
    if len(text) != 0:
        send_mail("\n".join(text))

# pyinstaller - F - -onefile LogParserWinScp.py
