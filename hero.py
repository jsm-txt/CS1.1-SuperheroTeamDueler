import random 
from ability import Ability
from armor import Armor

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
        

    def fight(self, opponent):
        fighter_list =[ my_hero.name ,opponent]
        winner = random.choice(fighter_list)
        print("A fight ensues")
        print(f'{my_hero.name} and {opponent} are battaling to death!!')
        return(print(f'{winner} remains victorious.'))

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

    def defend(self, damage):
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
        block = self.defend(damage)
        damage -= block
        self.current_health -= damage
        return


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    # my_hero = Hero("Grace Hopper", 200)
    # print(my_hero.name)
    # print(my_hero.current_health)
    # my_hero.fight("slime")

    # ability = Ability("Great Debugging", 50)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # print(hero.abilities)

    # If you run this file from the terminal
    # this block of code is executed.
    # ability = Ability("Great Debugging", 50)
    # another_ability = Ability("Smarty Pants", 90)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # hero.add_ability(another_ability)
    # print(hero.attack())

    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.current_health)