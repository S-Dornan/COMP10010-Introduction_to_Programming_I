print("""
This programme is designed to check if a word is a palindrome.""")

running = "y"


def get_midpoints(word):
    index_length = len(word)
    odd_check = index_length % 2  # If this returns 1 it's an odd number of letters, if this returns 0 it's an even number of letters.
    if odd_check == 1:
        # It's an odd number of letters
        # So there is one middle value, and it doesn't need to be checked against anything'
        midpoint = (((index_length - 1) / 2))
        midpoint = int(midpoint)
        lower_midpoint = midpoint
        upper_midpoint = midpoint + 1
    else:
        # It's an even number of letters
        # So there are two middle values.
        midpoint = (((index_length - 1) / 2))
        lower_midpoint = int(midpoint) + 1
        upper_midpoint = lower_midpoint
    return lower_midpoint, upper_midpoint


def format_string(string):
    string = string.lower()
    return string


def check_if_palindrome(word):
    lower, upper = get_midpoints(word)
    index_start = 0
    index_end = len(word)
    first_half = word[index_start:lower]
    second_half = word[upper:index_end]
    second_half = second_half[::-1]
    if second_half == first_half:
        return True
    else:
        return False


while running == "y" or running == "Y":
    original_word = input("\nPlease enter a word: ")
    word = format_string(original_word)
    is_palindrome = check_if_palindrome(word)
    if is_palindrome == True:
        print("\n\"" + original_word + "\" is a palindrome")
    else:
        print("\n\"" + original_word + "\" is not a palindrome")
    running = input("\nWould you like to try another word? (Y/N): ")

print("\nThank you for using this program.")