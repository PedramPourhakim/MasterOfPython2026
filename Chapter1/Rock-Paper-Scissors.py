# imports and global variables
import random
USER_CHOICES = ("rock","paper","scissor")

# create function to get user input
def get_user_input():
    choices_str = ", ".join(USER_CHOICES)
    while True:
        user_choice = input(f"Pick your choice : {choices_str} : ")
        if user_choice in USER_CHOICES:
            return user_choice
        else:
            print("Please enter a valid choice")
            continue


# create a function to get pc input
def get_pc_input():
    pc_choice = random.choice(USER_CHOICES)
    print(f"PC choice : {pc_choice}")
    return pc_choice





# compare and determine which one is the winner
def determine_winner(user_input,pc_input):
    if user_input == pc_input:
        print("Drawn !")
    elif (user_input == "rock" and pc_input == "scissor") \
        or (user_input == "scissor" and pc_input == "paper") \
        or (user_input == "paper" and pc_input == "rock"):
        print("User Won!")
    else:
        print("Computer Won!")


# create a main function as the runner
def main():
    determine_winner(get_user_input(),get_pc_input())
    print("Thank you for playing!")


# make an iteration for doing the game as much as we need
answer = 'y'
while answer == "y":
    main()
    answer = input("Do you want to play again? (y/n) : ")
