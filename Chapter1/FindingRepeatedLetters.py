def get_user_input():
    """This function gets the user input"""
    return input("Please Enter a sentence : ").split(' ')

def calculate_maximum_length(words_array):
    """This function calculates the maximum length of a word"""
    max_len = 0
    for word in words_array:
        max_len = max(max_len, len(word))
    return max_len

def get_biggest_words(words_array, max_len):
    """This function gets the biggest words"""
    biggest_words = []
    for word in words_array:
        if len(word) == max_len:
            biggest_words.append(word)
    return biggest_words

def main():
    """
    This function is the main function
    At first it calculates the maximum length words
    """
    while True:
        words_arr = get_user_input()
        max_len = calculate_maximum_length(words_arr)
        biggest_words = get_biggest_words(words_arr, max_len)
        print(f'Longest word(s) : {biggest_words} ({max_len} letters)')
        to_continue = input('Do You want to continue? (y/n)')
        if to_continue.lower() == 'n':
            break

if __name__ == '__main__':
    main()



