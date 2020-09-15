def convert(number):
    converted_string = ""
    if number % 3 == 0:
        converted_string += "Pling"
    if number % 5 == 0:
        converted_string += "Plang"
    if number % 7 == 0:
        converted_string += "Plong"
    if len(converted_string) < 1:
        converted_string = str(number)
    return converted_string

