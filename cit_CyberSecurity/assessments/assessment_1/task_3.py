






# Author NAVEEN REDDY
# Date : 28/08/2021
# Version : 1.0

# Rock Paper Scissors game
# Two Players

print("Welcome to Rock, Paper, Scissors!")
print("Let's begin ...")
name1 = input("Player 1: What's your name? ")
name2 = input("Player 2: What's your name?\n")

print("Hello " + name1 + " and " + name2)
print(name2 + ": Close your eyes!")

choice1 = input(name1 + ": enter 'r' for rock, 'p' for paper, and 's' for scissors: ")
print("Great choice! Now - cover your answer and ask " + name2 + " to choose. \n\n\n")
choice2 = input(name2 + ": enter 'r' for rock, 'p' for paper, and 's' for scissors: ")

if choice1 == choice2:
    print("It's a Tie!. Both players selected ",choice2)
elif choice1 == 'r':
    if choice2 == 's':
        print("Player1 wins !!!")
    else:
        print("Player2 wins!!!")
elif choice1 == 's':
    if choice2 == 'r':
        print("Player2 wins !!!")
    else:
        print("Player1 wins !!!")
elif choice1 == 'p':
    if choice2 == 'r':
        print("Player1 wins !!!")
    else:
        print("Player2 wins !!!")


print("Thanks for playing Rock, Paper, Scissors")