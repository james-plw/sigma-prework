def max_and_min(list):
    min = list[0]
    max = list[0]
    for num in list:
        if num < min:
            min = num
        elif num > max:
            max = num
        else:
            continue
    return min, max


str_input = input('Enter a list of integers, separated by commas: ')
str_list = str_input.split(',')  # split input into list
int_list = list(map(int, str_list))  # converting list from string to integers
print(max_and_min(int_list))
