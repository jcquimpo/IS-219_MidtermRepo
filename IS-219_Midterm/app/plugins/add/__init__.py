from app.commands import Command


class AddCommand(Command):
    def execute(self):
        num1, num2 = input("Enter two numbers you would like to add: ").split()
        try:
            num1 = float(num1)
            num2 = float(num2)
            result = num1 + num2
            print("The sum of {} and {} is: {}".format(num1, num2, result))
        except ValueError:
            print("Please enter valid numbers.")