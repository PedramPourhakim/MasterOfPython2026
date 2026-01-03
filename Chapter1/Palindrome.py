
def is_palindrome(s):
    """This function checks if the given string is a palindrome"""
    return s == s[::-1]

def get_user_input():
    """This function gets user input and prints the result"""
    try :
        user_input = input("Enter a string: ")
        if is_palindrome(user_input):
            print("The string is a palindrome.")
        else:
            print("The string is not a palindrome.")
    except ValueError:
        print("Please enter a string")

def main():
    while True:
        get_user_input()
        is_continue = input("Continue? (y/n): ")
        if is_continue.lower() == "n":
            break

if __name__ == "__main__":
    main()
