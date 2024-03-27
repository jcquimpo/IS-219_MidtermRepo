import logging
import os
from app.commands import Command
import pandas as pd
from app.plugins.add import AddCommand

class CsvCommand(Command):
    def execute(self):
        # Ensure the 'data' directory exists and is writable
        data_dir = './data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            logging.info(f"The directory '{data_dir}' is created")
        elif not os.access(data_dir, os.W_OK):
            logging.error(f"The directory '{data_dir}' is not writable.")
            return

        csv_file_path = os.path.join(data_dir, 'operations_history.csv')
        logging.info(f'the relative path  to save my file is {csv_file_path}')
        # Read the CSV file back into a DataFrame
        absolute_path = os.path.abspath(csv_file_path)
        logging.info(f'the absolute path  to save my file is {absolute_path}')
        df_read_operations = pd.read_csv(csv_file_path)

        # Define a dictionary with operation names as keys and corresponding functions as values
        operation_functions = {
            'add': self.add,
            'subtract': self.subtract,
            'multiply': self.multiply,
            'divide': self.divide
        }

        try:
            # Print and log each operation nicely
            print("Operations from CSV:")
            for index, row in df_read_operations.iterrows():
                # First, print and log the complete record for the operation
                operation_info = f"{row['Operation']}: {row['Num1']}, {row['Num2']}"
                print(f"Record {index}: {operation_info}")
                logging.info(f"Record {index}: {operation_info}")

                # Then, iterate through each field in the row to print and log
                for field in row.index:
                    field_info = f"    {field}: {row[field]}"
                    print(field_info)
                    logging.info(f"Index: {index}, {field_info}")

                # Calculate the result using the corresponding function from the dictionary
                operation = row['Operation'].lower()
                operation_function = operation_functions.get(operation)
                if operation_function:
                    operation_function(row['Num1'], row['Num2'])

        except:
            print("There are no operations in the history")
            logging.info(f"No history of operations")

    def add(self, num1, num2):
        result = num1 + num2
        print(f"Sum of Num1 and Num2: {result}")
        logging.info(f"Sum of {num1} and {num2}: {result}")

    def subtract(self, num1, num2):
        result = num1 - num2
        print(f"Difference of Num1 and Num2: {result}")
        logging.info(f"Difference of {num1} and {num2}: {result}")

    def multiply(self, num1, num2):
        result = num1 * num2
        print(f"Product of Num1 and Num2: {result}")
        logging.info(f"Product of {num1} and {num2}: {result}")

    def divide(self, num1, num2):
        if num2 == 0:
            print(f"Cannot divide by 0")
            logging.info(f"Cannot divide by 0")
        else:
            result = num1 / num2
            print(f"Quotient of Num1 and Num2: {result}")
            logging.info(f"Quotient of {num1} and {num2}: {result}")
