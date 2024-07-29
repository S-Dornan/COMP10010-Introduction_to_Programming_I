print("""This is a programme designed to do two things: 

First, it is a programme designed to show a list of all the prime numbers between 1 and a user-specified number N.

Second, it is designed to show the sum of all those numbers to the user.""")
running = "y"


def get_primes(lower_bound, upper_bound):
    prime_numbers = []
    new_upper_bound = upper_bound + 1
    for n in range(lower_bound, new_upper_bound):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    break
            else:
                prime_numbers.append(n)
    return prime_numbers


def sum_squares(list):
    squares = []
    for i in list:
        squares.append(i ** 2)
    sum_of_squares = sum(squares)
    return sum_of_squares


def stringify_list(list):
    last_elem = list[-1]  # Get last element of list
    last_elem_str = str(last_elem)  # Stringify last element for safety
    edited_list = list[:-1]  # Delete last element of list
    edited_list_str = str(edited_list).replace('[', '').replace(']', '')
    return edited_list_str, last_elem_str


while running == "y" or running == "Y":
    lower_variable = 1
    upper_variable = int(input("\nPlease enter a positive whole number: "))
    primes = get_primes(lower_variable, upper_variable)
    incorrect_primes = []
    len_primes = len(primes)
    if len_primes >= 1:
        last_elem = primes[-1]
        if upper_variable in primes:
            stringified_primes, last_elem = stringify_list(primes)
            print("\nThe primes between", lower_variable, "and", upper_variable, "are:", stringified_primes, "and",
              last_elem,". It looks like", lower_variable, "isn't a prime number.")
            sum_of_primes = sum_squares(primes)
            print("\nThe sum of the square of these primes is", sum_of_primes)
            primes.insert(1, lower_variable)
            incorrect_sum_of_primes = sum_squares(primes)
            print("\nIf", lower_variable, "was a prime number, the sum of the square of these primes would be", incorrect_sum_of_primes)
        else:
            stringified_primes, last_elem = stringify_list(primes)
            print("\nThe primes between", lower_variable, "and", upper_variable, "are:", stringified_primes, "and "+last_elem+". It looks like 1 and", upper_variable, "aren't prime numbers.")
            sum_of_primes = sum_squares(primes)
            print("\nThe sum of the square of these primes is", sum_of_primes)
            primes.insert(1, lower_variable)
            primes.insert(len(primes), upper_variable)
            incorrect_sum_of_primes = sum_squares(primes)
            print("\nIf", lower_variable, "and", upper_variable, "were prime numbers, the sum of the square of these primes would be",
                  incorrect_sum_of_primes)
    else:
        print("\nIt looks like there aren't any primes for this number.")
        print("\nIf 1 was a prime number the sum of the primes would be 1, as it is the only number in the list, and it only occurs once. It is not possible to add a single number that only occurs once, thus the result is 1.")
    running = input("\nPress Y to try again with a different number, press N to exit the programme: ")