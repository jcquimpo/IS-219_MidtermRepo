from app.commands import Command
import logging

class DivideCommand(Command):
    def execute(self):
        num1, num2 = input("Enter two numbers you would like to divide: ").split()
        try:
            num1 = float(num1)
            num2 = float(num2)
            result = num1 / num2
            print("The quotient of {} and {} is: {}".format(num1, num2, result))
            logging.info(f'The numbers divided are num1: {num1} & num2: {num2}; the quotient is {result}')
        except ValueError:
            print("Please enter valid numbers.")