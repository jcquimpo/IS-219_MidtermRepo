from app.commands import Command
import logging

class AddCommand(Command):
    def execute(self):
        num1, num2 = input("Enter two numbers you would like to add: ").split()
        try:
            num1 = float(num1)
            num2 = float(num2)
            result = num1 + num2
            print("The sum of {} and {} is: {}".format(num1, num2, result))
            logging.info(f'The numbers added are num1: {num1} & num2: {num2}; the sum is {result}')
        except ValueError:
            print("Please enter valid numbers.")