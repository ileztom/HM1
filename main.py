import random
#ex1
array = list(range(1, 11))
print("Массив", array)

reversed_array = array[::-1]
print("Перевернутый массив: ", reversed_array)
#ex2
random_array = [random.randint(1, 20) for _ in range(10)]
print("Рандомный массив", random_array)

random_array.sort(reverse=True)
print("Рандомный массив по убыванию:", random_array)
#ex3
car = [
    ["honda vezel", 2015, 1.5],
    ["lexus es250", 2019, 2.0],
    ["lexus rx300", 2019, 2.0],
    ["mazda axela", 2017, 1.5],
    ["mazda cx-3", 2019, 2.0],
    ["mitsubishi pajero", 2017, 3.0],
    ["nissan juke", 2017, 1.5]
]
car.sort(key=lambda x: x[1])
for row in car:
    print("|", end=" ")
    for item in row:
        print(item, end=" | ")
    print()
