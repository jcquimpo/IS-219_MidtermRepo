from app.commands import Command


class SubtractCommand(Command):
    def execute(self):
        num1, num2 = input("Enter two numbers you would like to subtract: ").split()
        try:
            num1 = float(num1)
            num2 = float(num2)
            result = num1 - num2
            print("The difference of {} and {} is: {}".format(num1, num2, result))
        except ValueError:
            print("Please enter valid numbers.")