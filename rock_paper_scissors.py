print(" R = ROCK \n P = PAPER \n S = SCISSORS ")
x=input("Enter your game [R/P/S]")
import random
import string
def specific_string(length):
    global y
    sample_string = 'RPS'
    y = ''.join((random.choice(sample_string) for x in range(length)))
    print("Game entered by Computer is ",y )
specific_string(1)
if(x=='R' and y=='P'):
    print("You Win")
elif(x=='R' and y=='R'):
    print("Match draw")
elif(x=='R' and y=='S'):
    print("Computer Wins")
elif(x=='P' and y=='P'):
    print("Match Draw")
elif(x=='P' and y=='S'):
    print("Computer Wins")
elif(x=='P' and y=='R'):
    print("You Win")
elif(x=='S' and y=='P'):
    print("You Win")
elif(x=='S' and y=='S'):
    print("Match Draw")
elif(x=='S' and y=='R'):
    print("Computer Wins")
else:
    print("Wrong Input")
