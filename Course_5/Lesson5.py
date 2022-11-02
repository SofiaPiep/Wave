class Employee:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def work(self):
        return 'I am working'

class Developer(Employee):
    def __init__(self, name, last_name, language):
        super().__init__(name, last_name)
        self.language = language

    def work(self):
        return "I'm coding"

    def get_language(self):
        return f'My language is {self.language}'

    def set_language(self, newlang):
        self.language = newlang


class Tester(Employee):
    def __init__(self, name, last_name, language, test_framework):
        super().__init__(name, last_name)
        self.language = language
        self.test_framework = test_framework

    def work(self):
        return 'I can write tests'

tester1 = Tester('Olga', 'Gerber', 'Python', 'Pytest')
print(tester1.testing())
print(tester1.test_framework)

# dev1 = Developer('Max', 'Kop', 'Python')
# print(dev1.walk())
# print(dev1.language)
# print(dev1.coding())


# employee1 = Employee('Alex', 'Smith')
# print(employee1.name)
# print(employee1.last_name)
# print(employee1.walk())
#
# employee2 = Employee('John', 'Moor')