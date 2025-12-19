# imports and global variables
import random
USER_CHOICES = ["rock","paper","scissors"]

# create function to get user input
def get_user_input():
    user_choice = input("Pick your choice: [\"rock\",\"paper\",\"scissor\"]: ")
    while user_choice not in USER_CHOICES:
        user_choice = input("Pick your choice: [\"rock\",\"paper\",\"scissor\"]: ")
    return user_choice


# create a function to get pc input
def get_pc_input():
    return random.choice(USER_CHOICES)





# compare and determine which one is the winner





# create a main function as the runner






# make an iteration for doing the game as much as we need