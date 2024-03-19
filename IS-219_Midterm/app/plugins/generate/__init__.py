import random
from app.commands import Command


class GenerateCommand(Command):
    def execute(self):
        num = random.random()
        print("Here is your generated number: ", num)
