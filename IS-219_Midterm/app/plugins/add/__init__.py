from app.commands import Command
import logging
import csv

class AddCommand(Command):
    def execute(self):
        num1, num2 = input("Enter two numbers you would like to add: ").split()
        try:
            num1 = float(num1)
            num2 = float(num2)
            result = num1 + num2
            print(f"The sum of {num1} and {num2} is: {result}")
            logging.info(f'The numbers added are num1: {num1} & num2: {num2}; the sum is {result}')
            
            with open("./data/operations_history.csv", "a", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['add', num1, num2, result])
            
        except ValueError:
            print("Please enter valid numbers.")
