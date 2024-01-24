from game_maker import *

def parse(game, prompt):
    prompt = prompt.split(' ') 
    for e in prompt:#if user enters extra spaces
        if e == " " or e == '':
            del e
    cmd = prompt[0]

   # try:
    if cmd == 'start':
        
        if len(prompt) == 2:
            
            game_filename = game.get_game_file(prompt[1])

            if game_filename:#---for now saving files hasn't been implemented, so files cannot be saved
                game.current_game = game_filename
                game.resume_game(game_filename)
                print(f'!successfully resumed the game {game_filename}.game')
            else:
                print(f'the game_file {prompt[1]}.game could not be found')
                
        elif len(prompt) == 3:

            no_players = game.get_no_players(prompt[2])
            
            if  prompt[1] == "new":
                if no_players:
                    game.NO_PLAYERS = no_players
                    game.start_game(None)
                else:
                    print(f'invalid number of players specified')
            else:
                print('specify new game with "new" keyword')
        else:
            print('invalid number of arguments')

    elif cmd == "help":

        if len(prompt) == 1:
            for command in game.COMMANDS:
                print(f'{command}\n {game.HELP[command]})')

        elif len(prompt) == 2:

            help_doc = game.get_help(prompt[1])

            if help_doc:
                print(f'{prompt[1]}\n {help_doc}')
            else:
                print(f'no documentation on {prompt[1]}')

        else:
            print('invalid number of arguments')

    elif cmd == "save":

        if len(prompt) == 1:

            gamefile = game.current_game
            
            if gamefile:
                game.save_game(gamefile)
            else:
                print('specify the name of a new game file')
            
        elif len(prompt) == 2:

            gamefile = game.get_game_file(prompt[1])
            if not gamefile:
                game.save_game(prompt[1])
            else:
                game.save_game(gamefile)#re write the save file
        
        else:
            print('invalid number of arguments')

    elif cmd == 'cls':

        if len(prompt) == 1:
            system('cls')
            game.logo()
        else:
            print('invalid number of arguments')

    elif cmd == "":
        pass

    elif cmd == "calc":

        if len(prompt) == 3:

            a = game.get_amount(prompt[1])
            b = game.get_amount(prompt[2])

            if a or a == 0: #if 0, then will always return false
                if b or b == 0:
                    print(f'RESULT: {a + b}')
                else:
                    print(f'invalid numerical {prompt[2]}')
            else:
                print(f'invalid numerical {prompt[1]}')

        elif len(prompt) == 4:

            a = game.get_amount(prompt[1])
            op = game.get_operator(prompt[2])
            b = game.get_amount(prompt[3])

            if a or a == 0:
                if op:
                    if b or b == 0:
                        print(f'RESULT: {game.calculate(a,b,op)}')
                    else:
                        print(f'invalid numerical {prompt[3]}')
                else:
                    print('invalid operator {prompt[2]}')
            else:
                print(f'invalid numerical {prompt[1]}')


    elif cmd in game.PLAYER_NAMES:
        if len(prompt) == 1:
            
            print(game.get_player(cmd))
        else:
            print(f'invalid number of arguments')

    elif cmd in game.PROPERTY_CODES:
        
        if len(prompt) == 1:
            
            prop = game.get_property(cmd)
            if prop:            #this check is uneccessary, but it does follow the pattern
                print(prop)
            else:
                print(f'property with code {cmd} does not exist')

        else:
            print('invalid number of arguments')

    elif cmd == "land":

        if len(prompt) == 3:
            
            player = game.get_player(prompt[1])
            prop = game.get_property(prompt[2])
            
            if prop:
                if player:
                    if not prop.is_unowned():
                        if not player.is_owner(prop):
                            if game.can_afford(player, prop.rent):
                                player.deduct(prop.rent)
                                prop.owner.profit(prop.rent)
                                prop.increase_earning_index()
                                print(f'{player.name} has paid to {prop.owner.name} the rent of {prop.name}')
                            else:
                                print(f'{player.name} cannot afford rent for {prop.name}')
                                player.add_debt(prop.owner, prop.rent)
                                prop.owner.add_debtor(player.name)
                                print(f'{player.name}\'s debts > {player.debts}')
                        else:
                            print(f'{player.name} is the owner of {prop.name}')
                    else:
                        print(f'{prop.name} is not owned by any player')
                else:
                    print(f'{prompt[1]} does not exist in this game')
            else:
                print(f'property with code {prompt[2]} does not exist')
            
        else:
            print('invalid number of arguments')
    
    elif cmd == 'funds':

        if len(prompt) == 1:
            print('funds')
            for player in game.PLAYERS:
                print(f'{player.name} > #{player.funds}')
        
        elif len(prompt) == 2:
            player = game.get_player(prompt[1])
            if player:
                print(f'{player.name} > N{player.funds}')
            else:
                print(f'{player} does not exist in this game')  
        else:
            print('invalid number of arguments')
       
    elif cmd == "loan":

        if len(prompt) == 4:
            sender = game.get_player(prompt[1])
            getter = game.get_player(prompt[2])
            amount = game.get_amount(prompt[3])
            if getter:
                if sender:
                    if amount or amount == 0:
                        if game.can_afford(sender, amount):
                            
                            sender.deduct(amount)
                            #sender.add_debtor(getter.name)
                            
                            getter.profit(amount)
                            getter.add_debt(sender,amount)   

                            print(f'{sender.name} borrows to {getter.name} {amount}')
                            print(f'{sender.name} > {sender.funds}')
                            print(f"{sender.name}'s debtors > {sender.debtors}")
                            
                                
                            print(f'{getter.name} > {getter.funds}')
                        else:
                            print(f'{sender.name} doesn\'t have enough funds for this transanction')
                    else:
                        print(f'invalid amount {prompt[3]}')
                else:
                    print(f'invalid sender {propmpt[1]}')# a bit out of order, i apologize
            else:
                print(f'invalid recipient {prompt[2]}')
                
        elif len(prompt) == 3:
            
            getter = game.get_player(prompt[1])
            amount = game.get_amount(prompt[2])

            if getter:
                if amount or amount == 0:
                    getter.profit(amount)
                    getter.add_debt('WEMA', amount)
                    
                        
                    game.add_bank_debt(getter.name, amount)
                    print(f'{getter.name} borrows  from WEMA {amount}')
                    print(f'{getter.name} > {getter.funds}')
                    print(f'{getter.name} > {getter.debts}')
                else:
                    print(f'invalid amount {prompt[2]}')
            else:
                print(f'invalid recipient {prompt[1]}')
            
        else:
            print('invalid number of arguments')

    elif cmd == 'dash':

        if len(prompt) == 4:

            sender = game.get_player(prompt[1])
            getter = game.get_player(prompt[2]) # a lot of encapsulation is possible,
            amount = game.get_amount(prompt[3])                   ##speed over perfection however
                    
            if sender:
                if getter:
                    if amount or amount == 0:
                        if game.can_afford(sender,amount):
                            sender.deduct(amount)
                            getter.profit(amount)
                            
                                
                            print(f'{sender.name} sends to {getter.name} {amount}')
                            print(f'{sender.name} > {sender.funds}')
                            print(f'{getter.name} > {getter.funds}')
                        else:
                            print(f'{sender.name} does not have enough funds for this transanction')
                    else:
                        print(f'invalid amount {prompt[3]}')
                else:
                    print(f'{prompt[2]} does not exist in this game')
            else:
                print(f'{prompt[1]} does not exist in this game')

        elif len(prompt) == 3:
            
            getter = game.get_player(prompt[1])
            amount = game.get_amount(prompt[2])
            if getter:
                if amount or amount == 0:
                    getter.profit(amount)
                    
                        
                    print(f'{getter.name} receives from WEMA {amount}')
                    print(f'{getter.name} > {getter.funds}')
                else:
                    print(f'invalid amount {prompt[2]}')
            else:
                print(f'{getter.name} does not exist in this game')
        else:
            print('invalid number of arguments')

    elif cmd == 'pay':
        
        if len(prompt) == 4:
            ower = game.get_player(prompt[1])
            being_owed = game.get_player(prompt[2])
            amount = game.get_amount(prompt[3])

            if ower:
                if being_owed:
                    if amount or amount == 0:
                        if being_owed.has_debtor(ower.name):
                            if game.can_afford(ower, amount):
                                if game.is_within_owed_amount(ower,being_owed.name,amount):
                                    ower.reduce_debt(being_owed, amount)
                                    ower.deduct(amount)
                                    being_owed.profit(amount)
                                    
                                        
                                    print(f'{ower.name} pays back {being_owed.name} {amount}')
                                    print(f'{ower.name} > {ower.funds}')
                                    print(f'{being_owed.name} > {being_owed.funds}')
                                else:
                                    print(f'{ower.name} doesn\'t owe {being_owed.name} up to {amount}')
                            else:
                                print(f'{ower.name} doesn\'t have enough for this transanction')
                                
                        else:
                            print(f'{ower.name} does not owe {being_owed.name}')
                    else:
                        print(f'invalid amount {prompt[3]}')
                else:
                    print(f'invalid recipient {prompt[2]}')
            else:
                print(f'{prompt[1]} does not exist in this game')
            
        elif len(prompt) == 3:
            
            getter = game.get_player(prompt[1])
            amount = game.get_amount(prompt[2])
            
            if getter:
                if amount or amount == 0:
                    if game.can_afford(getter,amount):
                        if game.is_owing_bank(getter.name): #again, bad code, should just put this in one function
                            if game.is_within_owed_amount(getter, "WEMA", amount):#perhaps should have made bankker an object
                                getter.deduct(amount)
                                getter.reduce_debt('WEMA',amount)
                                game.reduce_bank_debt(getter.name, amount)
                                
                                    
                                    
                                print(f'{getter.name} pays back to WEMA {amount}')
                                print(f'{getter.name} > {getter.funds}')
                                print(f'{getter.name} > {getter.debts}')
                            else:
                                print(f'{getter.name} does not owe WEMA up to {amount}')
                        else:
                            print(f'{getter.name} does not owe WEMA')
                    else:
                        print(f'{getter.name} does not have the funds for that transanction')
                else:
                    print(f'invalid amount {prompt[2]}')
            else:
                print(f'{prompt[1]} does not exist in this game')

    elif cmd == 'debit':

        if len(prompt) == 3:
            getter = game.get_player(prompt[1])
            amount = game.get_amount(prompt[2])

            if getter:
                if amount or amount == 0:
                    getter.deduct(amount)
                    print(f'{getter.name} pays to WEMA {amount}')
                    print(f'{getter.name} > {getter.funds}')
                    
                        
                else:
                    print(f'invalid amount {prompt[2]}')
            else:
                print(f'{getter.name} does not exist in this game')
            
        else:
            print('invalid number of arguments')

    elif cmd == "credit":

        if len(prompt) == 3:
            
            getter = game.get_player(prompt[1])
            amount = game.get_amount(prompt[2])
            
            if getter:
                if amount or amount == 0:
                    getter.profit(amount)
                    
                        
                    print(f'{getter.name} receives from WEMA {amount}')
                    print(f'{getter.name} > {getter.funds}')
                else:
                    print(f'invalid amount {prompt[2]}')
            else:
                print(f'{prompt[1]} does not exist in this game')
            
        else:
            print('invalid number of arguments')

    elif cmd == "go":

        if len(prompt) == 2:
            getter = game.get_player(prompt[1])
            if getter:
                getter.profit(20000)
                print(f'{getter.name} receives from mummy monthly allowance of 20,000')
                print(f'{getter.name} > {getter.funds}')
                
                    
            else:
                print(f'{prompt[1]} does not exist in this game')
        else:
            print('invalid number of arguments')
        
    elif cmd == "game":
        buf = ""
        for player in game.PLAYERS:
            print(player)
            
        
    elif cmd == "prop":

        if len(prompt) == 1:
            for player in game.PLAYERS:
                print(f'{player.name} > {player.properties}')
                
        elif len(prompt) == 2:
            player = game.get_player(prompt[1])
            if player:
                print(f'{player.name} > {player.properties}')
            else:
                print(f'{prompt[1]} does not exist in this game')
        
        else:
            print('invalid number of arguments')

    elif cmd == "debt":
        
        if len(prompt) == 1:
            for player in game.PLAYERS:
                print(f'{player.name}\'s debts > {player.debts}')
                print(f'{player.name}\'s debtors > {player.debtors}\n')
                

        elif len(prompt) == 2:
            player = game.get_player(prompt[1]) #sacrificied efficiency to defend the pattern
            if player:                                              #or so i say
                print(f'{player.name}\'s debts > {player.debts}')
                print(f'{player.name}\'s debtors > {player.debtors}')
                
                    
            else:
                print(f'{prompt[1]} does not exist this game')

        elif len(prompt) == 3:
            player = game.get_player(prompt[1])
            amount = game.get_amount(prompt[2])
            if player:
                if amount or amount == 0:
                    game.add_bank_debt(player.name, amount)
                    player.add_debt("WEMA",amount)
                    print(f'{player.name} > {player.debts}')
                    
                        
                else:
                    print(f'invalid amount {prompt[1]}')
            else:
                print(f'{prompt[1]} does not exist in this game')

        elif len(prompt) == 4:
            player = game.get_player(prompt[1])
            indebted = game.get_player(prompt[2])
            amount = game.get_amount(prompt[3])
            
            if player:
                if indebted:
                    if amount or amount == 0:
                        if indebted.not_have_debtor(player.name):
                            indebted.add_debtor(player.name)
                        player.add_debt(indebted, amount)
                        print(f'{player.name} is owing {indebted.name} {amount}')
                        print(f'{player.name} > {player.debts}')
                        
                            
                    else:
                        print(f'invalid amount {prompt[3]}')
                else:
                    print(f'invalid recipient {prompt[2]}')
            else:
                print(f'{prompt[1]} does not exist in this game')
        else:
            print('invalid number of arguments')

    elif cmd == 'forgive':
        
        if len(prompt) == 3:
            indebted = game.get_player(prompt[1])
            ower = game.get_player(prompt[2])
        
            if ower:
                if indebted:
                    if indebted.has_debtor(ower):
                        print(f'{indebted.name} has forgiven {ower.name} of all debts')
                        ower.reduce_debt(indebted, ower.debts[indebted.name])
                        
                            
                    else:
                        print(f'{ower.name} does not owe {indebted.name}')
                else:
                    print('invalid recipient {prompt[2]}')
            else:
                print(f'{prompt[1]} does not exist in this game')

        elif len(prompt) == 4:
            
            indebted = game.get_player(prompt[1])
            ower = game.get_player(prompt[2])
            amount = game.get_amount(prompt[3])

            if ower:
                if indebted:
                    if amount or amount == 0:
                        if indebted.has_debtor(ower):
                            if game.is_within_owed_amount(ower, indebted.name, amount):
                                ower.reduce_debt(indebted, amount)
                                print(f'{indebted.name} has forgiven {ower.name} of {amount}')
                                print(f'{ower.name} > {ower.debts}')
                                
                                    
                            else:
                                print(f'{ower.name} does not owe {indebted.name} up to {amount}')
                        else:
                            print(f'{ower.name} does not owe {indebted.name}')
                    else:
                        print(f'invalid amount {prompt[3]}')
                else:
                    print('invalid recipient {prompt[2]}')
            else:
                print(f'{prompt[1]} does not exist in this game')                
            
        else:
            print('invalid number of arguments')


    elif cmd == "buy":

        if len(prompt) == 3:
            buyer = game.get_player(prompt[1])
            prop = game.get_property(prompt[2])

            if buyer:
                if prop:
                    if game.can_afford(buyer, prop.buying_cost):
                        if prop.is_unowned():
                            buyer.deduct(prop.buying_cost)
                            buyer.add_property(prop)
                            prop.owner = buyer
                            print(f'{buyer.name} has acquired {prop.name}')
                            print(f'{buyer.name} > {buyer.property_names}')
                            print(f'{buyer.name} > {buyer.funds}')
                            
                                
                        else:
                            print(f'{prop.name} is already owned by {prop.owner.name}')
                    else:
                        print(f'{buyer.name} cannot afford {prop.name}')
                else:
                    print(f'property with code {prompt[2]} does not exist')
            else:
                print(f'{prompt[1]} does not exist in this game')
            
        else:
            print('invalid number of arguments')

    elif cmd == "sell":

        if len(prompt) == 3:
            seller = game.get_player(prompt[1])
            prop = game.get_property(prompt[2])
            
            if seller:
                if prop:
                    if seller.is_owner(prop):
                        seller.profit(prop.value)
                        seller.remove_property(prop)
                        prop.no_houses = 0
                        prop.reevaluate()
                        print(f'{seller.name} has sold {prop.name} to WEMA')
                        print(f'{seller.name} > {seller.funds}')
                        
                            
                    else:
                        print(f'{prop.name} is not owned by {seller.name}')
                else:
                    print(f'property with code {prompt[2]} does not exist')
            else:
                print(f'{prompt[1]} does not exist in this game')

        elif len(prompt) == 5:
            seller = game.get_player(prompt[1])
            buyer =  game.get_player(prompt[2])
            prop = game.get_property(prompt[3])
            profit = game.get_amount(prompt[4])

            if seller:
                if buyer:
                    if prop:
                        if profit or profit == 0:
                            if game.can_afford(buyer, prop.value + float(profit)):
                                if seller.is_owner(prop):
                                    seller.profit(prop.value + float(profit))
                                    buyer.deduct(prop.value + float(profit))
                                    
                                        
                                    seller.remove_property(prop)
                                    buyer.add_property(prop)
                                    print(f'{seller.name} sold {prop.name} to {buyer.name} for {prop.value + float(profit)}')

                                else:
                                    print(f'{prop.name} is not owned by {seller.name}')
                            else:
                                print(f'{buyer.name} cannot afford {prop.name}')
                        else:
                            print(f'invalid amount {prompt[4]}')
                    else:
                        print(f'property with code {prompt[2]} does not exist')
                else:
                    print(f'invalid recipient{prompt[2]}')
            else:
                print(f'{prompt[1]} does not exist in this game')
        else:
            print('invalid number of arguments')

    elif cmd == "up":
        
        if len(prompt) == 2:
            #owner = game.get_player(prompt[1])
            prop = game.get_property(prompt[1])
            #if owner:
            if prop:
                if not prop.is_unowned():
                    if game.can_afford(prop.owner, prop.house_cost):
                        if prop.is_not_maxed_out():
                            prop.build_house()
                            prop.owner.deduct(prop.house_cost)
                            print(f'{prop.owner.name} has built a new house on {prop.name}')
                            prop.reevaluate()
                            print(prop)
                            
                                
                            print(f'{prop.owner.name} > {prop.owner.funds}')
                        else:
                            print(f'{prop.name} already has the max amount of houses')
                    else:
                        print(f'{prop.owner.name} does not have the funds for that transanction')
                else:
                    print(f'{prop.name} is not owned by any player')
            else:
                print(f'property with code {prompt[1]} does not exist')
            #else:
               # print(f'{prompt[1]} does not exist in this game')
        else:
            print('invalid number of arguments')

    elif cmd == "down":

        if len(prompt) == 2:
            #owner = game.get_player(prompt[1])
            prop = game.get_property(prompt[1])
            #if owner:
            if prop:
                #if owner.is_owner(prop):
                if not prop.is_unowned():
                    if prop.is_not_minimum():
                        prop.demolish_house()
                        prop.owner.profit(prop.house_cost - float(prop.house_cost/4))
                        print(f'{prop.owner.name} has demolished a house on {prop.name}')
                        prop.reevaluate()
                        print(prop)
                        
                            
                        print(f'{prop.owner.name} > {prop.owner.funds}')
                    else:
                        print(f'{prop.name} doesn\'t have any houses on it')
                    #else:
                        #print(f'{owner.name} does not own {prop.name}')
                else:
                    print(f'{prop.name} is not owned by any player')
            else:
                print(f'property with code {prompt[1]} does not exist')
            #else:
                #print(f'{prompt[1]} does not exist in this game')
        else:
            print('invalid number of arguments')

    elif cmd == "bail":

        if len(prompt) == 2:

            player = game.get_player(prompt[1])
            
            if player:
                player.deduct(10000)    
                print(f'{player.name} has paid the bail price of 10,000cp')
                print(f'{player.name} > {player.funds}')
            else:
                print(f'{prompt[1]} does not exist in this game')

        else:
            print('invalid number of arguments')


    elif cmd == "chance":

        if len(prompt) == 1:

            print(game.get_chance())
            
        else:
            print('inavlid number of arguments')

    elif cmd == "chest":

        if len(prompt) == 1:

            print(game.get_community())
            
        else:
            print('inavlid number of arguments')


    elif cmd == "worth":

        if len(prompt)  == 1:
            rankings = {}
            for player in game.PLAYERS:
                rankings[player.name] = game.worth(player)
            for player_name in rankings:
                print(f'{player_name} > {rankings[player_name]}')
                
        elif len(prompt) == 2:

            player = game.get_player(prompt[1])
            if player:
                print(f'{player.name} > {game.worth(player)}')
            else:
                print(f'{prompt[1]} does not exist in this game')
        
        else:
            print('invalid number of arguments')


            
    else:
        print(f'invalid command - {cmd}')


    #except:
        #print('!error within prompt')




