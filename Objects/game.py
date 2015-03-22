__author__ = 'Ingus Mat Burleson'

from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll



class Game:
    def setup(self):
        self.player = Character()
        self.monsters = [
            Goblin(),
            Troll(),
            Dragon()
        ]

        self.monster = self.get_next_monster()


    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None


    def monster_turn(self):
        if self.monster.attack():
            print("{} is attacking!".format(self.monster))

            if input("Dodge? Y/N ").lower() == "y":
                if self.player.dodge():
                    print("You dodged the attack!")
                else:
                    print("You got hit anyway")
                    self.player.wounded()
            else:
                print("{} hit you for 1 point!".format(self.monster))
                self.player.wounded()
        else:
            print("{} is not attacking this turn.  Whew!".format(self.monster))



    def player_turn(self):
        # let the player attack, rest, or quit
        player_choice = input("Do you want to Attack, Rest or Quit? A/R/Q ")
        if player_choice.lower() == 'a':
            if self.player.attack():
                if self.monster.dodge():
                    print("{} dodged your attack.".format(self.monster))
                else:
                    print("You hit {monster} for {damage} points".format(monster = self.monster, damage = 1))
                    self.monster.wounded()
            else:
                print("You missed your attack on the {}.".format(self.monster))
        elif player_choice.lower() == 'r':
            self.player.rest()
        elif player_choice.lower() == 'q';
            #exit the game
        else:
            self.player_turn()


    def cleanup(self):
        # If the monster has no more hit points:
            # up the player's experience
            # print a message
            # Get a new monster

    def __init__(self):
        self.setup()

        while self.player.hit_points and (self.monster or self.monsters):
            print(self.player)
            self.monster_turn()
            self.player_turn()
            self.cleanup()

        if self.player.hit_points:
            print("You win!")
        elif self.monsters or self.monster:
            print("You lose!")