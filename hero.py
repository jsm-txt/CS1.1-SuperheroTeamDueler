import random 
from ability import Ability
from armor import Armor
from weapon import Weapon
from team import Team

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
    # we know the name of our hero, so we assign it here
        self.name = name
    # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
    # when a hero is created, their current health is
    # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # TODO: This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.
        self.abilities.append(weapon)


    def fight(self, opponent):
        # if hero.abilities == False:
        #     if opponent.abilities == False:
        #         print(f"{opponent.name} draw")
        #     else:print(f"{hero.name} lost")
        # if opponent.abilities ==  True:
        #     if hero.abilities == False:
        #         print(f"{opponent.name} wins")

        print("A fight ensues")
        while hero.current_health >= 0 or opponent.current_health >= 0 :
            power = hero.attack()
            # print(power)
            opponent.take_damage(power)
            print(f'Opponent health is {opponent.current_health}')

            power2 = opponent.attack()
            # print(power2)
            hero.take_damage(power2)
            print(f'Hero health is {hero.current_health}')
            print(f'{hero.name} and {opponent.name} are battaling to death!!')
            if hero.is_alive() == False:
                break
            if opponent.is_alive() == False:
                break
            
        
        if hero.current_health >= 0:
            return print(f'{opponent.name} remains victorious!!')
        if opponent.current_health >=0:
            return print(f'{hero.name} remains victorious!!')

        

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)
        

    def attack(self):
        total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
        # return the total damage
        return total_damage

    def add_armor(self, armor):
        '''Add armor to self.armors
        Armor: Armor Object
        '''
        # TODO: Add armor object that is passed in to `self.armors`
        self.armors.append(armor)

    def defend(self):
        '''Calculate the total block amount from all armor blocks.
        return: total_block:Int
        '''
        # TODO: This method should run the block method on each armor in self.armors
        total_block = 0
        # loop through all of our hero's abilities
        for armor in self.armors:
            # add the damage of each attack to our running total
            total_block += armor.block()
        # return the total damage
        return total_block

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        # TODO: Create a method that updates self.current_health to the current
        # minus the the amount returned from calling self.defend(damage).
        block = self.defend()
        damage = damage - block

        # print(block)
        # print(damage)
        if block > damage:
            damage = 0
        
        self.current_health -= damage
        return

    def is_alive(self):  
        '''Return True or False depending on whether the hero is alive or not.
        '''
        # TODO: Check the current_health of the hero.
        # if it is <= 0, then return False. Otherwise, they still have health
        # and are therefore alive, so return True

        if self.current_health <= 0:
            # print("false")
            return False
        else:
            # print("true") 
            return True 



# if __name__ == "__main__"
#     # If you run this file from the terminal
#     # this block is executed.

    
#     # print(my_hero.name)
#     # print(my_hero.current_health)
#     # my_hero.fight("slime")

    
#     # hero = Hero("Grace Hopper", 200)
    
#     # print(hero.abilities)

#     # If you run this file from the terminal
#     # this block of code is executed.
#     # ability = Ability("Great Debugging", 50)
#     # another_ability = Ability("Smarty Pants", 90)
#     # hero = Hero("Grace Hopper", 200)
#     # hero.add_ability(ability)
#     # hero.add_ability(another_ability)
#     # print(hero.attack())

#     # hero = Hero("Grace Hopper", 200)
#     # hero.take_damage(50)

#     # print(hero.current_health)
#     # hero.take_damage(150)
#     # print(hero.is_alive())
#     # hero.take_damage(15000)
#     # print(hero.is_alive())
#     hero = Hero("Grace Hopper", 200)
#     ability = Ability("Great Debugging", 50)
#     weapon = Weapon("Lasso of Truth", 90)
#     hero.add_ability(ability)
#     hero.add_weapon(weapon)
#     print(hero.attack())
#     shield = Armor("Shield", 50)
#     hero.add_armor(shield)
    

#     # hero2 = Hero("slime", 200)
#     # hero2.add_ability(ability)
#     # hero2.add_armor(shield)

#     # hero.fight(hero2)

    