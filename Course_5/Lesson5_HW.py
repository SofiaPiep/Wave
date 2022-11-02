class Human():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def live(self):
        return "I'm alive"

class Woman(Human):
    def __init__(self, name, surname, status, children):
        super().__init__(name, surname)
        self.status = status
        self.kinder = children

    def urlaub(self):
        return "It's the best time for a vacation!"

    def dating(self):
        return "I'm looking for a BF"


class Man(Human):
    def __init__(self, name, surname, job, hobby):
        super().__init__(name, surname)
        self.job = job
        self.hobby = hobby

    def __friends(self):
        return "Today is Saturday! Where are you?"


hum1 = Human('Olga', 'Gerber')
print(hum1.live())

woman1 = Woman('Anna', 'Dorn', 'single', 3)
print(woman1.kinder)
print(woman1.urlaub())

man1 = Man('Maik', 'Wasserman', 'Driver', 'Fishing')
print(man1.hobby)
print(man1._Man__friends())