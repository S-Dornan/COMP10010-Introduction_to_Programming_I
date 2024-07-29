filepath = "floats.txt"


def get_floats_file():
    filepath = None
    while filepath == None:
        try:
            filepath = input("Could not find required file, \"floats.txt\". Please enter the file path: ")
            file = open(filepath, "r")
            print("file found successfully")
            file.close()
        except FileNotFoundError:
            print("Could not find file or directory \""+filepath+"\" Did you enter the file path correctly?")
            filepath = None
    return filepath


def open_floats_file(filepath):
    try:
        file = open(filepath, "r")
    except FileNotFoundError:
        filepath = get_floats_file()
        file = open(filepath, "r")
    return file


def add_all_nums_to_list(file):
    numbers = []
    for line in file:
        line = line.strip()
        numbers.append(float(line))
    return numbers


def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j = j - 1
        numbers[j + 1] = key
    return numbers

def save_list_to_file(numbers, filename):
    file = open(filename, "w")
    file.write(numbers)
    file.close()
    return file

def stringify_list(list):
    list_str = str(list).replace('[', '').replace(']', '')
    list_str = list_str.replace('\'', '')
    list_str = list_str.replace(' ', '')
    list_str = list_str.replace(',', '\n')
    return list_str

def main():
    file = open_floats_file(filepath)
    numbers_list = add_all_nums_to_list(file)
    sorted_numbers = insertion_sort(numbers_list)
    print(sorted_numbers)
    sorted_numbers_str = stringify_list(sorted_numbers)
    save_list_to_file(sorted_numbers_str, "sorted_floats.txt")

main()