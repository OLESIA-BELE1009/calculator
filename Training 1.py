while True:
    a = float(input("Введите первое число: "))
    b = float(input("Введите первое число: "))
    operation =  input("Введите операцию (+, -, *, /): ")

    if b == 0 and operation == "/":
        print("На ноль делить нельзя")

    if operation == "+":
        print('Результат:', a + b)
    elif operation == "-":
        print(a - b)
    elif operation == "*":
        print(a * b)
    elif operation == "/":
        print(a / b)
    else:
        print("Неизвестная операция")

    answer = input("Хотите продолжить? (да/нет): ")

    if answer == "нет":
        break