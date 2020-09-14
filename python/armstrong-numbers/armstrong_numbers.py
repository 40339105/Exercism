def is_armstrong_number(number):
    number_list = [int(d) ** len(str(number)) for d in str(number)]
    return sum(number_list) == number
