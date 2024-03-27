from app.commands import Command
import logging
import csv

class DivideCommand(Command):
    def execute(self):
        num1, num2 = input("Enter two numbers you would like to divide: ").split()
        try:
            num1 = float(num1)
            num2 = float(num2)
            
            if num2 == 0:
                print("Cannot divide by zero. Please enter a non-zero divisor.")
                logging.error("Attempted to divide by zero.")
                return
            
            result = num1 / num2
            print("The quotient of {} and {} is: {}".format(num1, num2, result))
            logging.info(f'The numbers divided are num1: {num1} & num2: {num2}; the quotient is {result}')
            
            with open("./data/operations_history.csv", "a", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['divide', num1, num2, result])
            
        except ValueError:
            print("Please enter valid numbers.")