v=0
n=0
while n<3:
    import random
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    rez = num1 + num2
    a = input(str(num1) + " + " + str(num2) + " = ")
    if int(a) == rez:
        print("Правильно!")
        v = v + 1
    else:
        print("Ответ неверный")
        n = n + 1
print("Игра окончена. Правильных ответов: " + str(v))