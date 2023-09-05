import random

def level(l):
    if((l=="Easy")or(l=="easy")):
        higher_number=5
        return higher_number
    elif((l=="Medium")or(l=="medium")):
        higher_number=10
        return higher_number
    else:
        higher_number=20
        return higher_number
    
def rnd(lv,hv):
    c=random.randint(lv,hv)
    return c
print("This is number Guessing Game!! If you guess the correct number you will be the winner")
content='''
This Game contains various levels . Please select desired level
levels=Easy
       Medium
       Difficult
'''
print(content)
l=input("Enter the level of this game:-")
print("Please enter the palyers name")
low=1
high=level(l)
r=rnd(low,high)
print(r)
while True:
    try:
        v=int(input("Please enter your guess number"))
        if(v!=r):
            print("Better Luck Next Time")
            continue       
        else:
            print("congratulations you won the game") 
            break      
    except ValueError as e:
        print("Please enter the valid number ")
        continue
    break



