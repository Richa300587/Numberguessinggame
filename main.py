# This is a sample Python script.
from random import randint
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def difficultylevel(a):
    if a=='Easy':
        return 10
    elif a=='Hard':
        return 5
    else:
        return "Invalid Input Please enter valid input"




def numberguessing():
    print("Welcome to number guessing Game")
    print("I am going to guess an integer between 1 to 100")
    answer=randint(1,100)
    print(answer)

    m=input("Please choose level of difficulty as 'Easy' or 'Hard' ")
    while difficultylevel(m)=="Invalid Input Please enter valid input":
        m=input("Please choosen level of difficulty as 'Easy' or 'Hard' ")
    turns=difficultylevel(m)
    print(f"you have {turns} number of Turns")
    while turns>0:
        yournumber = int(input("enter your number"))
        if yournumber==answer:
            print(f"Yay your guess is right number is {yournumber}")
            break
        elif yournumber>answer:
            turns-=1
            print(f"{turns} turns left")
            print("Number is too High")
        elif yournumber<answer:
            turns-=1
            print(f"{turns} turns left")
            print("Number is too Low")
    if turns==0:
        print("you loose the game")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numberguessing()

