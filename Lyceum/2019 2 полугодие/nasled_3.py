class Profile:
    def __init__(self, prof):
        self.prof = prof
        # self.inf = ''

    def info(self):
        return self.inf

    def describe(self):
        prof = self.prof
        print(prof, Profile.info(self))


class Vacancy(Profile):
    def __init__(self, prof, inf):
        super().__init__(prof)
        self.inf = "Предлагаемая зарплата:" + str(inf)


class Resume(Profile):
    def __init__(self, prof, inf):
        super().__init__(prof)
        self.inf = "Стаж работы:" + str(inf)
