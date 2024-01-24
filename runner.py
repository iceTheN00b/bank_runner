from parser import *

def run():
    game = game_maker()
    while True:
        profit = parse(game, input('\n|bank_runner>> '))

run()
