class User:
    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def login(self):
        return 'Login in user account'


user_1 = User('Nick', 'Smith', 'nick@mail')

print(user_1.fname)
print(user_1.login())


class Admin(User):
    def __init__(self, fname, lname, email, password):
        super().__init__(fname, lname, email)
        self.__password = password

    def login(self):
        return 'Login in admin account'

    def get_password(self):
        return f'Your password is {self.__password}'

    def set_password(self, new_password):
        self.__password = new_password
        return self.__password

    def edit(self):
        return 'Edit the profile'

admin_1 = Admin('Max', 'Johnson', 'max@mail', '135jkl')
print(admin_1.login())
print(admin_1.lname)
print(admin_1.edit())
print(admin_1.get_password())
admin_1.set_password('576fff')
print(admin_1.get_password())
