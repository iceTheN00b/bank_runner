from objects import *
from CONSTANTS import *
from os import system, listdir, mkdir, chdir
import time
from random import choice
#import keyboard
from threading import Thread

class game_maker: #game_maker class really is just the banker

    def __init__(self):
        self.PLAYERS = []
        self.PLAYER_NAMES = []
        self.NO_PLAYERS = 0
        self.OWING_BANK = []
        self.BANK_DEBTS = {}
        self.COMMANDS = COMMANDS
        self.HELP = HELP
        
        self.PROPERTY_NAMES = PROPERTY_NAMES
        self.PROPERTIES = []
        self.PROPERTY_CODES = []
        self.COMMUNITY = []
        self.CHANCE = []

        self.logger = True

        self.current_game = False

        self.game_started = False
        
        if 'saved_games' not in listdir():
            print('*created "saved_games" folder')
            mkdir('saved_games')

        self.logo()

    def details(self):
        return f'{make_string(self.BANK_DEBTS)}'
    
    def logo(self):
        system('cls')
        print(LOGO)
          
#______<READER FUNCTIONS>_______#
    
    def read_player_file(filename):
        f = open(filename,'r')
        details = f.readlines()
        f.close()
        return details

    def read_property_file(filename):
        f = open(filename,'r')
        details = f.readlines()
        f.close()

    #______<STARTER FUNCTIONS>_______#

    def obtain_player_names(self):
        for i in range(0,self.NO_PLAYERS):
            p = player()
            name = input(f'enter name of player {i+1} > ').split(' ')[0]
            if name in self.PLAYER_NAMES:    #or name in self.PROPERTY_CODES:
                print('DUPLICATE NAME')
                print('RAHHH')
                exit(-1)
            if name in self.COMMANDS:
                print('PLAYER NAME CANNOT BE COMMAND')
                print('RAHHH')
                exit(-1)
            if name in self.PROPERTY_NAMES:
                print('PLAYER NAME CANNOT BE PROPERTY NAME')
                print('RAHHH')
                exit(-1)
            p.name = name
            self.PLAYERS.append(p)
            self.PLAYER_NAMES.append(p.name)
            print(f'added {name} to the game!')

    #_____<CONTINUE FUNCTIONS>______#

    def set_players(self,details):
        no_players = int(details[0])
        players = []
        print(f'starting game with {no_players} number of players')
        
        return no_players, players

    #______<IN-GAME>_____________#

    def return_player(self,name):
        for player in self.PLAYERS:
            if player.name == name:
                return player

    def get_player(self,name):
        if name in self.PLAYER_NAMES:
            return self.return_player(name)
        else:
            return False

    def get_amount(self,amount):
        try:
            amount = float(amount)
            return amount
        except:
            return False

    def get_operator(self, operator):
        if operator in ['+','-','*','%','/','//','>','<','^']:
            return operator
        else:
            return False

    def calculate(self, a, b, op):
        if op == '+':
            return a+b
        elif op == '-':
            return a-b
        elif op == '*':
            return a*b
        elif op == "%":
            return a%b
        elif op == '/':
            if b == 0:
                return 'DIVISION BY ZERO' #as is neccassary
            else:
                return a/b
        elif op == "//":
            if b*b == 0:
                return 'DIVISION BY ZERO'
            else:
                return a//b
        elif op == '>':
            return a>b
        elif op == '<':
            return a<b
        elif op == '^':
            return a^b

    def can_afford(self, payer, amount):
        if payer.funds >= amount:
            return True
        else:
            return False

    def is_within_owed_amount(self,ower, being_owed_name, amount):
        if ower.debts[being_owed_name] >= amount:
            return True
        else:
            return False
    
    def delete_player(self,name):
        pass

    def return_property(self, prop_code):
        for prop in self.PROPERTIES:
            if prop.code == prop_code:
                return prop

    def get_property(self, prop_code):
        if prop_code in self.PROPERTY_CODES:
            return self.return_property(prop_code)
        else:
            return False
        
    def is_owing_bank(self, player_name):
        if player_name in self.OWING_BANK:
            return True
        else:
            return False
        
    def add_bank_debt(self, player_name, amount): #this allows players to borrow from bank even if owing
        if self.is_owing_bank(player_name):  #id like some flexibility being possible
            self.BANK_DEBTS[player_name] += amount
        else:
            self.BANK_DEBTS[player_name] = amount
            self.OWING_BANK.append(player_name)

    def reduce_bank_debt(self, player_name, amount):
        self.BANK_DEBTS[player_name] -= amount
        if self.BANK_DEBTS[player_name] == 0:
            print(f'{player_name} is no longer owing the bank')
            del self.OWING_BANK[self.OWING_BANK.index(player_name)]

    def initialize_properties(self):
        for pdetails in PROPERTIES: #property details
            p = property(name = pdetails[0],
                                 buying_cost = pdetails[1],
                                 house_cost = pdetails[2],
                                 rent = pdetails[3],
                                 code = pdetails[4])
            self.PROPERTIES.append(p)
            self.PROPERTY_CODES.append(str(pdetails[4]))
        print(f'*initialized properties')


    def initialize_community_and_chance(self):
        self.COMMUNITY = COMMUNITY_CARDS
        self.CHANCE = CHANCE_CARDS

    def get_chance(self):
        return choice(self.CHANCE)

    def get_community(self):
        return choice(self.COMMUNITY)

    def get_game_file(self, filename):
        game_files = listdir('saved_games')
        print(game_files)
        if f'{filename}.game' in game_files:
            return filename
        else:
            return False

    def clear_players_and_properties(self):#in case the game is started mid game
        self.NO_PLAYERS = 0
        self.PLAYERS = []
        self.PROPERTIES = []

    def save_game(self,gamefilename):
        f = open(f'saved_games\{gamefilename}.game','w')
        buf  = ""
        f.write(str(self.NO_PLAYERS) + '\n')
        f.write(self.details() + '\n')
        for player in self.PLAYERS:
            buf += player.details() + '\n'
        for prop in self.PROPERTIES:
            buf += prop.details() + '\n'
        f.write(buf)
        f.close()
        print(f'saved this game as {gamefilename}.game')

    def resume_no_players(self, details):
        self.NO_PLAYERS = int(details)
        print(f'number of players > {self.NO_PLAYERS}')

    def resume_properties(self, details):
        for detail in details:
            print(detail)
            detail = detail.split('|')
            p = property(0,0,0,0,0) #lets just null everything for now
            p.name = detail[0]
            p.house_cost = float(detail[1])
            p.no_houses = float(detail[2])
            p.buying_cost = float(detail[3])
            p.owner = "None" if detail[4] == "None" else "{insert player here}"#requrires player names
            p.code = detail[5];
            p.earning_index = float(detail[6])
            p.init_rent = float(detail[7])
            p.house_rent = float(detail[8])
            p.rent = float(detail[9])
            p.value = float(detail[10])
            self.PROPERTIES.append(p)
            self.PROPERTY_CODES.append(p.code)
            self.PROPERTY_NAMES.append(p.name)
            print(f'!resumed property {p.name}')
        print(self.PROPERTY_CODES)
        print(self.PROPERTY_NAMES)

    def resume_players(self, details):
        for detail in details:
            p = player()
            detail = detail.split('|')
            p.name = detail[0]
            p.funds = float(detail[1])
            p.property_names = detail[2].split(',')
            p.debtors = detail[4].split(',')
            for debt_details in detail[3].split(','):
                if debt_details != "":
                    thisdebt = debt_details.split('-')
                    p.debts[thisdebt[0]] = float(thisdebt[1])
            self.PLAYER_NAMES.append(p.name)
            self.PLAYERS.append(p)
            print(f'!resumed player {p.name}')

    def resume_bank(self, details):
        if str(details)== "\n":
            print('no debts to the bank were incurred')
            pass
        else:
            print(f'debt details > {details}')
            for debt_details in details.split(','):
                print(f'a debt : {debt_details}')
                if debt_details != "\n":
                    thisdebt = debt_details.split('-')
                    self.OWING_BANK.append(thisdebt[0])
                    print(self.OWING_BANK)
                    self.BANK_DEBTS[thisdebt[0]] = float(thisdebt[1])
                    print(self.BANK_DEBTS)
            

    def round_it_up(self):#set the player propeties and set the property owners
        for player in self.PLAYERS:
            for prop_name in player.property_names:
                player.properties.append(self.get_property(prop_name))
        for prop in self.PROPERTIES:
            if prop.owner != "None":
                prop.owner = self.get_player(prop.owner)
            
        
    def resume_game(self, filename):
        self.clear_players_and_properties()
        f = open(f'saved_games\{filename}.game','r')
        details = f.readlines()
        self.resume_no_players(details[0])
        self.resume_bank(details[1]);
        self.resume_players(details[self.NO_PLAYERS : self.NO_PLAYERS + 2])
        self.resume_properties(details[self.NO_PLAYERS + 2:])
        self.round_it_up()
        print(f'restored game {filename}.game')
        f.close()

            #now the big boys
    def get_no_players(self, number):
        try:
            number = int(number)
            if number < 13 and number > 1:
                return number
            else:
                return False
        except:
            return False

    def get_help(self, help_keyword):
        if help_keyword in self.HELP:
            return self.HELP[help_keyword]
        else:
            return False

    def worth(self, player):
        w = 0
        w += player.funds
        for prop in player.properties:
            w += prop.value
        for debt in player.debts:
            w -= player.debts[debt]
        for debtor_name in player.debtors:
            debtor = self.get_player(debtor_name)
            if debtor:
                w += debtor.debts[player.name]
            else:
                print(debtor)
                return "could not parse this debt"
        return w

    def log(self, information):
        if self.logger == True:
            f = open('saved_games/game.log','r')
            old = f.read()
            f.close()
            f = open('saved_games/game.log','w')
            info = ""
            if isinstance(information, list):
                for e in information:
                    info += str(e) + " "#get rid of '\n'
                new = old + info + '\n'
                f.write(new)
                f.close()
            else:
                f.write(old + information)
                f.close()

    def refresh_log(self):
        f = open('saved_games/game.log','w')
        f.write('')
        f.close()
        
    def start_game(self, game_file):
        if game_file == None:
            self.PLAYERS = []
            self.PLAYER_NAMES = []
            print('*initiating initialization sequence')
            time.sleep(0.6)
            print('*initializing bank_runner')
            time.sleep(0.6)
            print(f'*starting game with {self.NO_PLAYERS}')
            print('*now requesting player names')
            self.obtain_player_names()
            print('*initializing properties')
            time.sleep(0.6)
            self.initialize_properties()
            self.initialize_community_and_chance()
            print('!ready to play')
            time.sleep(1)
            self.logo()
            self.game_started = True
            #self.refresh_log()
        else:
            f = open(game_file, 'r')
            contents = f.readlines();f.close()
            
