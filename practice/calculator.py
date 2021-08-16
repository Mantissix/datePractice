class calculator:
    @staticmethod
    def add(x, y):
        print(f'{x} + {y} = {x+y}')
        return x + y

    @staticmethod
    def sub(x, y):
        print(f'{x} - {y} = {x-y}')
        return x - y

    @staticmethod
    def multiply(x, y):
        print(f'{x} * {y} = {x*y}')
        return x * y

    @staticmethod
    def division(x, y):
        print(f'{x} / {y} = {x/y}')
        return x / y
