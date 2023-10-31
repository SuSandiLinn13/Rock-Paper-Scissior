import sys
import random
from enum import Enum

#output RPS.ROCK.....
#can use replace method 
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

# print(RPS(1))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)
# sys.exit()

print('hey')
playerchoice = input("Enter : 1 for Rock, 2 for Paper, 3 for Scissors ")
# print(playerchoice)

player = int(playerchoice)
# print(type(player))
if player < 1 or player > 3 : 
    sys.exit("Out of the Bound!")

computerChoice = random.choice('123')
computer = int(computerChoice)

print("")
print("You chose " + str(RPS(player)).replace("RPS.",'')+ '.')
print("Python chose " + str(RPS(computer)).replace("RPS.",'') + '.')
print('')

if player == computer:
    print("WIthdraw!!")
elif player == 1 and computer == 3 :
    print("You Win!!")
elif player == 2 and computer == 1: 
    print("You Win!!")
elif player == 3 and computer == 2: 
    print("You Win!1")
else :
    print('Python Wins!!')
print('')
