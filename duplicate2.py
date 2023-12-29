# complex_example.py

def calculate_area_of_rectangle(length, width):
    return length * width

def calculate_area_of_square(side_length):
    return side_length * side_length

def calculate_area_of_rectangle(length, width):  # Duplicated function
    return length * width

def calculate_area_of_square(side_length):  # Duplicated function
    return side_length * side_length

def process_data(data):
    result = 0
    for item in data:
        result += item
    return result

def analyze_data(data):  # Duplicated function
    result = 0
    for item in data:
        result += item
    return result

# Duplicated code block
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# Duplicated code block
values = [10, 20, 30, 40, 50]
for value in values:
    print(value)
