from calculator_manu.Addition import Addition
from calculator_manu.Division import Division
from calculator_manu.Multiplication import Multiplication
from calculator_manu.Subtraction import Subtraction


class Calculator:
    def __init__(self):
        self.num1 = float(input("Ingrese el primer número: "))
        self.num2 = float(input("Ingrese el segundo número: "))

    @property
    def num1(self):
        return self._num1

    @num1.setter
    def num1(self, value):
        self._num1 = value

    @property
    def num2(self):
        return self._num2

    @num2.setter
    def num2(self, value):
        self._num2 = value

    def select_operation(self):
        print("Seleccione la operación que desea realizar:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")

        operation = input()

        if operation == '1':
            op = Addition(self.num1, self.num2)
        elif operation == '2':
            op = Subtraction(self.num1, self.num2)
        elif operation == '3':
            op = Multiplication(self.num1, self.num2)
        elif operation == '4':
            op = Division(self.num1, self.num2)
        else:
            print("Operación no válida")
            return

        print("El resultado es: ", op.execute())




