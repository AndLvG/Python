class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, user, message):
        pass

    def post(self, message):
        pass

    def info(self):
        return ''

    def describe(self):
        print('{}\n{}'.format(self.name, self.info))


class Person(User):
    def __init__(self, name, date):
        super().__init__(name)
        self.date = date

    def info(self):
        return 'Дата рождения: {}'.format(self.date)

    def subscribe(self, user):
        pass


class Community(User):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description

    def info(self):
        return 'Описание: {}'.format(self.description)
