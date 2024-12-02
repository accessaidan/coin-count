# if this is on a new device run the other code to open the external file before use
import os
from operator import itemgetter

# dictionary of the coin bags data
coin_data = {
    "1p": {"value": 1, "weight": 365, "sing_weight": 3.65},
    "2p": {"value": 1, "weight": 365, "sing_weight": 7.12},
    "5p": {"value": 5, "weight": 235, "sing_weight": 2.35},
    "10": {"value": 5, "weight": 325, "sing_weight": 6.50},
    "20p": {"value": 10, "weight": 125, "sing_weight": 5.00},
    "50p": {"value": 10, "weight": 160, "sing_weight": 8.00},
    "£1": {"value": 20, "weight": 175, "sing_weight": 8.75},
    "£2": {"value": 20, "weight": 120, "sing_weight": 12.00},
}

# print of the coins data
def print_coin_data():
    print("1p: bag value: 1 bag weight: 365g")
    print("2p: bag value: 1 bag weight: 365g")
    print("5p: bag value: 5 bag weight: 235g")
    print("10p: bag value: 5 bag weight: 325g")
    print("20p: bag value: 10 bag weight: 125g")
    print("50p: bag value: 10 bag weight: 160g")
    print("£1: bag value: 20 bag weight: 175g")
    print("£2: bag value: 20 bag weight: 120g")
    print("")
    input("press enter to continue")


# menu system where they choose what to do
def menu_system():
    load_data()

    print("Menu:")
    print("1. Input a coin bag")
    print("2. Display total number of bags and value")
    print("3. Assess voulenteer accuracy and totals")
    print("4. View coin data")
    print("5. Exit")
    print("What would you like to do:")
    decision = input("")
    if decision == "1":  # subroutine that takes name, amount and calculates
        voulenteer_sub()
        print("Thank you, that has been recorded")
        use_again()
    elif (
        decision == "2"
    ):  # subroutine that reads the external file and calculates the total bags and value

        decision_2()
        use_again()
    elif decision == "3":
        decision_3()
        use_again()

    elif decision == "4":
        print_coin_data()
        use_again()

    elif decision == "5":
        print("Thank you")
        print("*** SHUTTING OFF ***")

    else:
        print("That was not a valid option")
        menu_system()


# Loads data from external file

voulenteer_data = []


def load_data(file_name="voulenteer_data.txt"):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            array_names = []
            for line in file:
                name, counted, correct, value, accuracy = line.strip().split(",")
                if name not in array_names:
                    array_names.append(name)

                    voulenteer_data.append(
                        {
                            "name": name,
                            "counted": int(counted),
                            "correct": int(correct),
                            "value": float(value),
                            "accuracy": float(accuracy),
                        }
                    )


# subroutine to decide weather to repeat the programm
def use_again():
    print("Would you like to continue to use the programm?  [Y/N]")
    repeat = input("").lower()
    if repeat == "y":
        voulenteer_data = {}
        menu_system()

    elif repeat == "n":
        print("Thank you")
        print("*** SHUTTING OFF ***")

    else:
        print("Sorry that was not a valid input")
        use_again()


# subroutine where voulenteer inputs bag
def voulenteer_sub():
    print("Enter your first name:")
    voulenteer_name = input("").lower()
    if voulenteer_name == "" or " " in voulenteer_name or voulenteer_name.isalpha() == False:
        print("That is not a valid name")
        voulenteer_sub()
    
    

    else:
    

        print("Double check your name")
        check_name = input ("Is the name correct, if not press [N], else press [enter]").lower()
        if check_name == "n":
            voulenteer_sub()
        
        else:
            index = 0
            if voulenteer_name in voulenteer_data:

                for i in range(len(voulenteer_data)):
                    if voulenteer_data[index]["name"] == voulenteer_name:
                        counted = voulenteer_data[index]["counted"]
                        correct = voulenteer_data[index]["correct"]
                        value = voulenteer_data[index]["value"]

                    else:
                        index = index + 1

            else:
                voulenteer_data.append(
                    {
                        "name": str(voulenteer_name),
                        "counted": int(0),
                        "correct": int(0),
                        "value": float(0.00),
                        "accuracy": float(0.00),
                    }
                )

                for i in range(len(voulenteer_data)):
                    if voulenteer_data[index]["name"] == voulenteer_name:
                        counted = voulenteer_data[index]["counted"]
                        correct = voulenteer_data[index]["correct"]
                        value = voulenteer_data[index]["value"]

                    else:
                        index = index + 1
            print("Enter the type of coin you have collected:")
            coin_type = input("")
            if coin_type not in coin_data:
                print("That is not a valid coin type, try again")
                voulenteer_sub()

            print("Enter the weight of your bag (xxxg)")
            
            try:
            # add another tab to all lines in the rest of subroutine
                weight = float(input(""))


                if weight != coin_data[coin_type]["weight"]:
                    print("That is not the correct weight of your bag")

                    add_or_remove(weight, coin_type)
                    counted = counted + 1
                    value = value + coin_data[coin_type]["value"]

                else:
                    counted = counted + 1
                    correct = correct + 1
                    value = value + coin_data[coin_type]["value"]

                voulenteer_data[index]["counted"] = counted
                voulenteer_data[index]["correct"] = correct
                voulenteer_data[index]["value"] = value
                accuracy = correct / counted * 100
                voulenteer_data[index]["accuracy"] = accuracy

                data_sorted = sorted(voulenteer_data, key=itemgetter("accuracy"), reverse=True)

                file = open("voulenteer_data.txt", "w")
                index_2 = 0
                for i in range(len(voulenteer_data)):
                    string_name = str(data_sorted[index_2]["name"])
                    string_counted = str(data_sorted[index_2]["counted"])
                    string_correct = str(data_sorted[index_2]["correct"])
                    string_value = str(data_sorted[index_2]["value"])
                    string_accuracy = str(data_sorted[index_2]["accuracy"])
                    if (
                        string_counted != "0"
                    ):  # fixes the problem of a new line of the dictionary with 0 everything
                        file.write(string_name)
                        file.write(", ")
                        file.write(string_counted)
                        file.write(", ")
                        file.write(string_correct)
                        file.write(", ")
                        file.write(string_value)
                        file.write(", ")
                        file.write(string_accuracy)
                        file.write("\n")
                    index_2 = index_2 + 1

            except:
                print("That is not a valid input, enter details again")
                voulenteer_sub()       


def add_or_remove(weight, coin_type):
    index_3 = 0
    arr_coin_types = ["1p", "2p", "5p", "10p", "20p", "50p", "£1", "£2"]
    arr_sing_weight = [3.65, 7.12, 2.35, 6.50, 5.00, 8.00, 8.75, 12.00]
    for i in range(len(arr_coin_types)):
        coin_type_needed = arr_coin_types[index_3]
        if arr_coin_types[index_3] != coin_type:

            index_3 = index_3 + 1

    needed_weight = coin_data[coin_type]["weight"]
    difference = needed_weight - weight
    if difference > 0:
        amount = difference / arr_sing_weight[index_3]
        print("You need to add", amount, "more coins to the bag")
    else:
        amount = (difference * -1) / arr_sing_weight[index_3]
        print("You need to remove", amount, "coins from the bag")


def decision_2():  # total bags inputted and value
    index_4 = 0
    total_counted = 0
    total_value = 0
    arr_names_done = [""]
    for i in range(len(voulenteer_data)):
        name_of_current = voulenteer_data[index_4]["name"]
        if name_of_current not in arr_names_done:
            arr_names_done.append(name_of_current)
            total_counted = total_counted + voulenteer_data[index_4]["counted"]
            total_value = total_value + voulenteer_data[index_4]["value"]
        index_4 = index_4 + 1
    print("A total of", total_counted, "bags have been counted")
    print("With a whopping total of", total_value, "great british pounds")

def decision_3(): # prints all voulenteers sorted by accuracy
    index_5 = 0
    for i in range(len(voulenteer_data)):
        name = voulenteer_data[index_5]["name"]
        counted = voulenteer_data[index_5]["counted"]
        accuracy = voulenteer_data[index_5]["accuracy"]

        print(name, "has counted", counted ,"bags with an accuracy of", accuracy ,"%")

        index_5 = index_5 + 1

menu_system()

