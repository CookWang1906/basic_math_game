import math
import random

def start_game():
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    n = input("Please choose a game to start: ")
    
    if n == "A":
        addition()
    elif n == "B":
        subtraction()
    elif n == "C":
        multiplication()   
    elif n == "D":
        division()
    else:
        print("Please choose again!")
        return start_game()
    
def addition():
    numb1 = random.randint(1,50)
    numb2 = random.randint(1,50)
    print(f"What is {numb1} + {numb2}?")
    
    ans = int(input("Answer: "))
    if ans == numb1 + numb2:
        print("Good work! Keep it going.")
        return addition()
    else:
        print("Wrong answer, Better luck next time!")

def subtraction():
    numb1 = random.randint(1,50)
    numb2 = random.randint(1,50)
    print(f"What is {numb1} - {numb2}?")
    
    ans = int(input("Answer: "))
    if ans == numb1 - numb2:
        print("Good work! Keep it going.")
        return subtraction()
    else:
        print("Wrong answer, Better luck next time!")
        
def multiplication():
    numb1 = random.randint(1,20)
    numb2 = random.randint(1,20)
    print(f"What is {numb1} x {numb2}?")
    
    ans = int(input("Answer: "))
    if ans == numb1 * numb2:
        print("Good work! Keep it going.")
        return multiplication()
    else:
        print("Wrong answer, Better luck next time!")

def division():
    numb1 = random.randint(1,20)
    numb2 = random.randint(1,20)
    numb1 = numb1 * numb2
    print(f"What is {numb1} : {numb2}?")
    
    ans = int(input("Answer: "))
    if ans == numb1 / numb2:
        print("Good work! Keep it going.")
        return division()
    else:
        print("Wrong answer, Better luck next time!")
        
start_game()