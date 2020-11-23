import random 

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

    def fight(self, opponent):
        fighter_list =[ my_hero.name ,opponent]
        winner = random.choice(fighter_list)
        print("A fight ensues")
        print(f'{my_hero.name} and {opponent} are battaling to death!!')
        return(print(f'{winner} remains victorious.'))

    

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)
    my_hero.fight("slime")