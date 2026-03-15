from inherit import Animal, Dog

print("Обычное животное")
cat = Animal("Мурзик", 3, "Кошка")
cat.info()
cat.make_sound()
print()

print("Собака")
dog = Dog("Барбос", 5, "Собака", "Овчарка", "Да")
dog.info()
dog.make_sound()
dog.guard_house()
print()

print("Удаляем объекты")
del cat
del dog