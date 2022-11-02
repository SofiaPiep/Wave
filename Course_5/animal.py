class Animal():
    COLOR = 'grey'

    def __init__(self, name='Animal', age=0, weight=8):
        self.name = name
        self.age = age
        self.weight = weight
        print('Create object of Animal')

    def print_info(self):
        print(f"Animal's name is {self.name} with weight {self.weight} kg and age {self.age} years old")

    # def get_name(self):
    #     return self.__name if self.__name else None
    #
    # def set_name(self):
    #     self.__name = name
    #     self.COLOR = 'blue'
