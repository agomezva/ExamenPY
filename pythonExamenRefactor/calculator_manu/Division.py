class Division:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def execute(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: División por cero no está permitida"