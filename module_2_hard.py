import random

number = random.randint(3, 20)
print('Первый камень шепчет тебе', number)

first_number = number
for i in range(1, first_number):
    for j in range(1, first_number):
        if first_number % (i + j) == 0 and i != j and i < j:
            result = i, j
            print("На соседнем камне начертай ", result)
print("Молодец, Индиана Джонс!")