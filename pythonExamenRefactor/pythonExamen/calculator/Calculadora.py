def calculator():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    print("Seleccione la operación que desea realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    operation = input()

    if operation == '1':
        result = num1 + num2
        print("El resultado de la suma es: ", result)
    elif operation == '2':
        result = num1 - num2
        print("El resultado de la resta es: ", result)
    elif operation == '3':
        result = num1 * num2
        print("El resultado de la multiplicación es: ", result)
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print("El resultado de la división es: ", result)
        else:
            print("Error: División por cero no está permitida")
    else:
        print("Operación no válida")

calculator()