class Animal:
    name = None
    age = None
    species = None

    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def make_sound(self):
        print(f"{self.species} издает звук")
    
    def info(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Вид: {self.species}")

    def __del__(self):
        print("Объект удален")
    
class Dog(Animal):
    breed = None
    guard_status = None

    def __init__(self, name, age, species, breed, guard_status):
        super().__init__(name, age, species)
        self.breed = breed
        self.guard_status = guard_status
    
    def info(self):
        super().info()
        print(f"Порода: {self.breed}")
        print(f"Охрана дома: {self.guard_status}")

    def guard_house(self):
        if self.guard_status:
            print("Гав Гав")
        else:
            print("Сегодня выходной")




    



    

    
