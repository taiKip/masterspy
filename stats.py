# Statistics
# tarvk002
#


def average(number_list):
    sum = 0
    count = 0
    for i in number_list:
        count += 1
        sum += i
    print("=== Custom functions ===")
    print(f"My Average: {round(sum/count,1)}")


def maximum(number_list):
    max = 0
    for i in number_list:
        if i > max:
            max = i
    print(f"My Maximum: {max}")


def offset(number_list, offset_amount):
    for i in range(len(number_list)):
        number_list[i] += offset_amount
    return number_list


def userInput():
    flag = True
    data = []
    temp = []
    while flag:
        user_input = input("Number (0 to stop):").strip()
        if user_input.isnumeric() and user_input != "0":
            data.append(int(user_input))
        elif user_input == "0":
            flag = False
    offset_amount = input("add offset amount: ").strip()
    if offset_amount.isnumeric():
        return offset(data, int(offset_amount)), int(offset_amount)
    else:
        return data, "0"


def printStatistics():
    number_list, offset_amount = userInput()
    if len(number_list) == 0:
        return
    print("=== Basic statistics ===")
    print(f"count: {len(number_list)}")
    print(f"Minimum: {min(number_list)}")
    print(f"Total: {sum(number_list)}")
    print(f"Average: {round((sum(number_list)/len(number_list)),1)}")
    average(number_list)
    maximum(number_list)
    if offset_amount != 0:
        print(f"Offset:{offset_amount}")
        print(f"After offset by {offset_amount} : {number_list}")

printStatistics()