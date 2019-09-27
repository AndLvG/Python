 class Person:

    def __init__(self, n, sn, pn, d):
        self.a = ''
        self.d = d
        self.n = n
        self.sn = sn
        self.pn = pn

    def get_phone(self):
        for i, j in self.d.items():
            if i == 'private':
                return j
            else:
                return None

    def get_name(self):
        return f'{self.pn} {self.n} {self.sn}'

    def get_work_phone(self):
        if 'work' in self.d:
            return self.d['work']
        else:
            return None

    def get_sms_text(self):
        return f'Уважаемый {self.n} {self.sn}! Примите участие в нашем беспроигрышном конкурсе для физических лиц'


class Company:

    def __init__(self, name_of_company, kind_of_act, d, *k):
        self.name_of_company = name_of_company
        self.kind_of_act = kind_of_act
        self.d = d
        self.k = k

    def get_phone(self):
        if 'contact' in self.d:
            return self.d['contact']
        elif 'contact' not in self.d:
            for i in self.k:
                if i.get_work_phone():
                    return i.get_work_phone()
            else:
                return None

    def get_name(self):
        return self.name_of_company

    def get_sms_text(self):
        return f'Для компании {self.name_of_company} есть супер предложение!' \
            f' Примите участие в нашем беспроигрышном конкурсе для {self.kind_of_act}'


def send_sms(*objects):
    for e in objects:
        if e.get_phone():
            print(f'Отправлено СМС на номер {e.get_phone()} с текстом: {e.get_sms_text()}')
        else:
            print(f'Не удалось отправить сообщение абоненту: {e.get_name()}')