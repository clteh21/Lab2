def display_main_menu():
    print("Enter some numbers seperated by commas")

def get_user_input():
    number = input()
    number_list = number.split(",")
    float_list = [float(a) for a in number_list]
    print(float_list)
    return float_list

def calc_average_temperature(numbersss):
    total = 0
    for number in numbersss:
        total = total + number
    average = total/len(numbersss)
    print("The average is ", average)

def calc_min_max_temperature(numbersss):
    maximum = max(numbersss)
    minimum = min(numbersss)
    print("The maximum is " ,maximum)
    print("The minimum is ", minimum)



def main():
    display_main_menu()
    numbersss = get_user_input()
    calc_average_temperature(numbersss)
    calc_min_max_temperature(numbersss)



main()