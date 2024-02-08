import math
import random

def start_game():
    print("A. Addition and Subtraction")
    n = input("Please choose a game to start: ")
    
    if n == "A":
        addition()
    else:
        print("Please choose again!")
        
def addition():
    numb1 = random.randint(1,50)
    numb2 = random.randint(1,50)
    print(f"What is {numb1} + {numb2}?")
    
    ans = int(input("Answer: "))
    if ans == numb1 + numb2:
        print("Good work! Keep it going.")
    else:
        print("Wrong answer, don't give up!")

def subtraction():
    numb1 = random.randint(1,50)
    numb2 = random.randint(1,50)
    print(f"What is {numb1} - {numb2}?")
    
    ans = int(input("Answer: "))
    if ans == numb1 - numb2:
        print("Good work! Keep it going.")
    else:
        print("Wrong answer, don't give up!")
        
start_game()

playAgain1 = 'yes'
while playAgain1 == 'yes':
    addition()
    subtraction()
    print("\nDo you want to play again? Yes(1)/No(2)")
    choice = input("1 or 2?: ")
    
playAgain2 = 'yes'
while playAgain2 == 'yes':
    multiplication()
    division()
    print("\nDo you want to play again? Yes(1)/No(2)")
    choice = input("1 or 2?: ")