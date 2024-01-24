PROPERTIES = [['LIBRARY', 24600, 20500, 10250, '101'],
['BURSARY', 24600, 20500, 10250, '102'],
['LIBRARIAN_QUARTERS', 41000, 20500, 10250, '103'],
['REGISTRAR_QUARTERS', 41000, 20500, 10250, '201'],
['VC_QUARTERS', 49200, 20500, 10250, '202'],
              
['COLMAS', 57400, 41000, 20500, '203'],
['COLENVS', 57400, 41000, 20500, '301'],
['COLENG', 65600, 41000, 20500, '302'],
['COLNAS', 73800, 41000, 20500, '303'],
['BRONZE_I', 73800, 41000, 20500, '401'],
['FEMALE_SILVER_HOSTEL', 82000, 41000, 20500, '402'],
['MALE_SILVER_HOSTEL', 90200, 61500, 30750, '403'],
['EMERALD_HOSTEL', 90200, 61500, 30750, '501'],
['BRONZE_II', 98400, 61500, 30750, '502'],
['ELT', 106600, 61500, 30750, '503'],
['BUPF', 106600, 61500, 30750, '601'],
['MARQUE', 114800, 61500, 30750, '602'],
['LECTURE_HALL_I', 123000, 82000, 41000, '603'],
['LECTURE_HALL_II', 131200, 82000, 41000, '701'],
['LECTURE_HALL_III', 139400, 82000, 41000, '702'],
['SENATE', 147600, 100000, 50000, '703'],
['ADENUGA', 155800, 100000, 50000, '801']]


LOGO = "  _                 _                                       \n"+"| |               | |                                      \n"+"| |__   __ _ _ __ | | __  _ __ _   _ _ __  _ __   ___ _ __ \n"+"| '_ \ / _` | '_ \| |/ / | '__| | | | '_ \| '_ \ / _ \ '__|\n"+"| |_) | (_| | | | |   <  | |  | |_| | | | | | | |  __/ |   \n"+"|_.__/ \__,_|_| |_|_|\_\ |_|   \__,_|_| |_|_| |_|\___|_|   \n"+"v 0.1\n"+"a work of ice\n"+"LIMITS: does not support mortages and auto-saving\n"+"v 0.2 promises additional functions as jailing and player modification\n "

COMMANDS = ['help', 'start', 'funds', 'loan', 'dash', 'pay', 'debit', 'credit', 'go', 'game', 'prop',
                            'debt', 'forgive', 'buy', 'sell', 'up', 'down', "chest", "chance","bail",'cls','worth','save']

PROPERTY_NAMES = ['LIBRARY', 'BURSARY', 'LIBRARIAN_QUARTERS', 'REGISTRAR_QUARTERS', 'VC_QUARTERS', 'COLMAS', 'COLENVS',
                                          'COLENG', 'COLNAS', 'BRONZE_I', 'FEMALE_SILVER_HOSTEL', 'MALE_SILVER_HOSTEL',
                                          'EMERALD_HOSTEL', 'BRONZE_II', 'ELT', 'BUPF:', 'MARQUE', 'LECTURE_HALL_I', 'LECTURE_HALL_II', 'LECTURE_HALL_III', 'SENATE', 'ADENUGA']

COMMUNITY_CARDS = [  "Bank error in your favor. Collect $2000.",
  "You have won second prize in a beauty contest. Collect $1000.",
  "From sale of stock you get $5000.",
  "Holiday fund matures. Collect $10000.",
  "Income tax refund. Collect $2000.",
  "Life insurance matures. Collect $10000.",
  "Pay hospital fees of $10000.",
  "Pay school fees of $5000.",
  "Receive $2500 consultancy fee.",
  "You inherit $10000.",
  "Advance to Go. Collect $20000.",
  "You are assessed for street repairs: Pay $4000 per house and $11500 per hotel you own.",
  "It is your birthday. Collect $1000 from each player.",
  "Get out of Jail free. This card may be kept until needed, or traded/sold.",
  "Pay a $1000 fine or take a Chance.",
  "You are elected Chairman of the Board. Pay each player $5000.",
  "Your building loan matures: Collect $15000.",
  "Go to Jail. Go directly to Jail, do not pass Go, do not collect $20000.",
  "Pay poor tax of $1500.",
  "You have been elected chairman of the board. Pay each player $5000.",
  "Make general repairs on all your property: For each house pay $2500, for each hotel $10000.",
  "Take a trip to Reading Railroad: If you pass Go, collect $20000.",
  "You have won a crossword competition. Collect $10000.",
  "Pay a $5000 fine or take a Chance.",
  "You are assessed for street repairs: Pay $2500 per house and $10000 per hotel you own.",
  "Pay back a loan with 20% interest or Pay $6000.",
  "Collect $5000 from every player.",
  "Get a get out of jail free card.",
  "Pay $1000 and take a Chance."
]

def make_string(listitem):
        string = ""
        if isinstance(listitem, list):
            for e in listitem:
                string += e + ','
        elif isinstance(listitem, dict):
            for key in listitem:
                string += f'{key}-{listitem[key]},' # ",being owed-amount,
        return string

CHANCE_CARDS = [    "Advance to GO. Collect $20000.",
    "Advance to BURSARY. If you pass Go, collect $20000.",
    "Advance to CONSULT ANNEX. If you pass Go, collect $20000.",
    "Advance to DE' BRANCH. If you pass Go, collect $20000.",
    "Advance to EMERALD HOSTEL. If you pass Go, collect $20000.",
    "Advance to LIBERIAN'S QUARTERS. If you pass Go, collect $20000.",
    "Advance to SENATE. If you pass Go, collect $20000.",
    "Advance to the nearest COLLEGE OF MEDICINE ADMINISTRATIVE BLOCK. If there are no COLLEGE OF MEDICINE ADMINISTRATIVE BLOCK spaces left, draw a new card. If you pass Go, collect $20000.",
    "Advance to the nearest LECTURE HALL. If there are no LECTURE HALL spaces left, draw a new card. If you pass Go, collect $20000.",
    "Advance to the nearest VC'S QUARTERS. If there are no VC'S QUARTERS spaces left, draw a new card. If you pass Go, collect $20000.",
    "Bank pays you dividend of $5000.",
    "Get out of Jail Free. This card may be kept until needed or sold.",
    "Go back 3 spaces.",
    "Go directly to Jail. Do not pass Go, do not collect $20000.",
    "Make general repairs on all your property: For each house, pay $2500; For each hotel, pay $10000.",
    "Pay poor tax of $1500.",
    "Take a ride to COLENVS. If you pass Go, collect $20000.",
    "Take a walk to FEMALE SILVER HOSTEL. If you pass Go, collect $20000.",
    "Pay 10,000 for portal access fee",
    "Take a walk to SAMBEF. If you pass Go, collect $20000.",
    "You have been elected chairman of the board. Pay each player $5000.",
    "Your building and loan matures. Receive $15000.",
    "You have won a crossword competition. Collect $10000.",
    "You have won a lawsuit. Collect $10000.",
    "You inherit $10000.",
    "Advance to SUSPENSION. Do not pass Go, do not collect $20000.",
    "Advance to COLMAS. If you pass Go, collect $20000.",
    "Give a  player (whom is not owing you) 10,000",
    "Advance to the nearest LIBRARY. If there are no LIBRARY spaces left, draw a new card. If you pass Go, collect $20000.",
    "Advance to the nearest BRONZE II. If there are no BRONZE II spaces left, draw a new card. If you pass Go, collect $20000."
              
]

HELP = {'help':'returns help documentation\n help [optional=function_name]',
                'start':'starts a new game, or loads \n NEW GAME: start \'new\' [no_players]\n RESUME GAME: start [name of saved game]',
                'cls' : 'clear the screen\n cls',
                'funds':'returns player funds\n funds [optional= name_of_player]',
                'loan':'borrow money from bank or other player\n loan [player_loaning] [player_loaning] [amount]',
                'dash':'grant money from one player to another\n dash [player_granting] [player_being_granted] [amount]',
                'pay': 'pay back debt to another player\n pay [player_owing] [optional=player_being_owed] [amount]',
                'debit':'pay money to bank\n debit [player] [amount]',
                'credit':'receive money from bank\n credit [player] [amount]',
                'go':'add 20,000 GO allowance to player\n go [player]',
                'game':'print all players and their details\n game',
                'prop':'print a player or all player\'s properties\n prop [optional=player]',
                'debt':'print all players debt, print a specific player\'s debt, add a debt between player and bank, or add a debt between player and another player\n PRINT ALL DEBTS: debt\n PRINT PLAYER DEBT: debt [player]\n ADD PLAYER DEBT TO BANK: debt [player] [amount]\n ADD PLAYER DEBT TO OTHER PLAYER: debt [player_owing] [player_being_owed] [amount]',
                'forgive':'forgive debt between players\n forgive [player_forgiving] [player_being_forgiven] [amount]',
                'buy':'obtain a property\n buy [player] [property_code]',
                'sell':'sell a property to bank or other player\n sell [player_selling] [optional=player_buying] [property_code] [optional=profit_amount]',
                'up':'build a house on a property\n up [property_code]',
                'down':'demolish a house on a property\n down [property_code]',
                'chance':'return a chance card\n chance',
                'chest':'return a community chest card\n chest',
                'bail':'deduct 10,000cp from a player as bail money\n bail [player_name]',
                'worth':"print a player's total worth\n worth [optional=player_name]",
                'save':"save the current game\n save [optional=gamefile_name]"
                }
