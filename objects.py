from CONSTANTS import *

class property:
    
    def __init__(self, name, buying_cost, house_cost, rent, code):
        self.name = name
        self.house_cost = house_cost
        self.no_houses = 0
        self.buying_cost = buying_cost
        self.owner = "None"
        self.code = code

        self.earning_index = 0

        self.init_rent = rent
        self.house_rent = int(self.house_cost) / 4
        self.rent = int((self.house_rent *  self.no_houses) + self.init_rent)
        self.value = self.buying_cost + self.earning_index #just to make some profit at least
        
        
    def __repr__(self):
        return f'\n{self.name}_ \n code > {self.code}\n Rent > {self.rent} \n BuyingCost > {self.buying_cost} \n HouseCost > {self.house_cost}\n No_Houses > {self.no_houses}\n OwnedBy > {self.owner.name if self.owner != "None" else "None"}\n value > {self.value}'

    def details(self):
        return f'{self.name}|{self.house_cost}|{self.no_houses}|{self.buying_cost}|{self.owner.name if self.owner != "None" else "None"}|{self.code}|{self.earning_index}|{self.init_rent}|{self.house_rent}|{self.rent}|{self.value}'
        #does all this data need to be saved?
        
    def increase_earning_index(self):
         self.earning_index += int(self.rent*0.1)
        
    def reevaluate(self):
        self.rent = (self.house_cost *  self.no_houses) + self.init_rent
        self.value = self.buying_cost + self.rent + self.earning_index
    
    def is_unowned(self):
        if self.owner == "None":
            return True
        else:
            return False

    def is_not_maxed_out(self):
        if not self.no_houses == 5:
            return True
        else:
            return False

    def is_not_minimum(self):
        if not self.no_houses == 0:
            return True
        else:
            return False

    def build_house(self):
        self.no_houses += 1

    def demolish_house(self):
        self.no_houses -= 1

class player:
    def __init__(self):
        self.name = None
        self.funds = 20000
        self.properties = []
        self.property_names = []
        
        self.debts = {}
        self.debtors = []
    def __repr__(self):
        return f'_{self.name}__\n funds > {self.funds}\n properties > {self.property_names}\n debts > {self.debts}'

    def details(self):
        return f'{self.name}|{self.funds}|{make_string(self.property_names)}|{make_string(self.debts)}|{make_string(self.debtors)}'

    def deduct(self,amount):
        if self.funds < amount:
            print(f'{self.name} has now gotten bankrupt')
            #disown property and all that
        self.funds -= amount
    def profit(self,amount):
        self.funds += amount
    def add_debt(self,sender,amount):
        if sender != 'WEMA':
            try:
                self.debts[sender.name] += amount
            except:
                self.debts[sender.name] = amount #relies on non-existence being the only possible fault
                sender.debtors.append(self.name)
        else:
            try:
                self.debts['WEMA'] += amount
            except:
                self.debts['WEMA'] = amount #relies on non-existence being the only possible fault

    def not_have_debtor(self,ower_name):
        if ower_name in self.debtors:
            return False
        else:
            return True

    def has_debtor(self, ower_name):
        if ower_name in self.debtors:
            return True
        else:
            return False

    def add_debtor(self, name):
        if name not in self.debtors:
            self.debtors.append(name)
            
    def is_debtless(self,person_im_owing_name):
        if self.debts[person_im_owing_name] ==  0:
            return True
        else:
            return False
        
    def reduce_debt(self, person_im_owing, amount):
        if person_im_owing != "WEMA":
            self.debts[person_im_owing.name] -= amount
            if self.is_debtless(person_im_owing.name):
                print(f'{self.name} no longer owes {person_im_owing.name}')
                del self.debts[person_im_owing.name]
                del person_im_owing.debtors[person_im_owing.debtors.index(self.name)] #delete from the indebted's debitor list
        else:
            self.debts["WEMA"] -= amount
            if self.is_debtless("WEMA"):
                del self.debts["WEMA"]

    def add_property(self, prop):
        self.properties.append(prop)
        self.property_names.append(prop.name)
        prop.owner = self

    def remove_property(self, prop):
        del self.properties[self.properties.index(prop)]
        print(f'removed {prop.name}')
        del self.property_names[self.property_names.index(prop.name)]
        print(f'removed from property_names file')
        prop.owner = "None" #this function must come before, or ownership transfer will be overwritten
        print(f'set owner of {prop.name} to {prop.owner}')
        
    def is_owner(self, prop):
        if prop.name in self.property_names:
            return True
        else:
            return False

    
    
          

        
