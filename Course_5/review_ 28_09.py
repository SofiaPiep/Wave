from animal import Animal
from dog import Dog
from cat import Cat

animal = Animal( name='Tuzik', weight=10)
print(animal.__dict__)

dog1 = Dog('Barbos', 3, 12, 'Yardterrer')
print(dog1.__dict__)

dog1.print_info()
dog1.is_barking()

cat1 = Cat('Murzik', 2, 4)
print(cat1.__dict__)
cat1.print_info()