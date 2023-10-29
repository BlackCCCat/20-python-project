# Write your code here
import random


class Dice():
    def __init__(self, dice_sides):
        self.dice_sides = dice_sides
        self.dice = self.generateDice(dice_sides)

    def generateDice(self, dice_sides):
        return range(1, dice_sides + 1)
    
    def rollDice(self):
        return random.choice(self.dice)


def main():
    continue_game = 'y'
    while continue_game == 'y':
        dice_sides = int(input("Select the type of dice to roll (e.g., 6, 20 or custom): "))
        roll_dice_num = int(input("How many dice would you like to roll?"))
        print(f'Rolling {roll_dice_num} {dice_sides}-sided dice...')
        dice = Dice(dice_sides)
        dice_result = []
        total_result = 0
        for i in range(roll_dice_num):
            dice_res = dice.rollDice()
            dice_result.append(dice_res)
            total_result += dice_res
        print(f'Results: {dice_result}')
        print(f'Total: {total_result}')
        continue_game = input("Would you like to continue? (y/n)").lower()
        



if __name__ == '__main__':
    main()