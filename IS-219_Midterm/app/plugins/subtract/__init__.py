from app.commands import Command
import logging

class SubtractCommand(Command):
    def execute(self):
        num1, num2 = input("Enter two numbers you would like to subtract: ").split()
        try:
            num1 = float(num1)
            num2 = float(num2)
            result = num1 - num2
            print("The difference of {} and {} is: {}".format(num1, num2, result))
            logging.info(f'The numbers subtracted are num1: {num1} & num2: {num2}; the difference is {result}')
        except ValueError:
            print("Please enter valid numbers.")