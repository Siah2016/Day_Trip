introduction = "Hello and welcome to the Day Trip Generator!"
print("")
print(introduction)
print("")
introduction = "Let's get started shall we?"

print(introduction)
# Getting started with random modules and listing.
import random

des_list = ["Las Vegas", "Paris", "Bahamas", "Maui", "Norway"]

def user_random_dest():
    random_des = random.choice(des_list)
    des_trip = input(f"How does {random_des} sound for your destination? (Y/N)")
    if des_trip == "y":
        print(f"{random_des} is a great destionation.")
        return random_des
    while des_trip == "n":
        random_des = random.choice(des_list)
        des_trip = input(f"How does {random_des} sound for your destination? (Y/N)")
        if des_trip == "y":
            print(f"{random_des} is a great destionation.")
            return random_des
      
confirmed_dest = user_random_dest()
# print(confirmed_dest)

rest_list = ["Cheesecake Factory", "The Capital Grille", "Angelines", "Morton's The Steakhouse", "Jerk 48"]

def user_random_rest():
    random_res = random.choice(rest_list)
    res_trip = input(f"How does {random_res} sound for a place to dine? (Y/N)")
    if res_trip == "y":
        print(f"{random_res} is an awesome restaurant to eat at.")
        return random_res
    while res_trip == "n":
        random_res = random.choice(rest_list)
        res_trip = input(f"How does {random_res} sound for a place to dine? (Y/N)")
        if res_trip == "y":
            print(f"{random_res} is an awesome restaurant to eat at.")
            return random_res
      
confirmed_rest = user_random_rest()
# print(confirmed_rest)

trans_list = ["Airplane", "Train", "Ship", "Bus", "Bicycle"]

def user_random_trans():
    random_trans = random.choice(trans_list)
    trans_trip = input(f"How does {random_trans} sound for transporation? (Y/N)")
    if trans_trip == "y":
        print(f"{random_trans} is a wonderful choice.")
        return random_trans
    while trans_trip == "n":
        random_trans = random.choice(trans_list)
        trans_trip = input(f"How does {random_trans} sound for transporation? (Y/N)")
        if trans_trip == "y":
            print(f"{random_trans} is a wonderful choice.")
            return random_trans
      
confirmed_trans = user_random_trans()
# print(confirmed_trans)

ent_list = ["Comedy Show", "Concert", "Escape Room", "Black Ops Paintball", "Rage Room"]

def user_random_ent():
    random_ent = random.choice(ent_list)
    ent_trip = input(f"How does {random_ent} sound for entertainment? (Y/N)")
    if ent_trip == "y":
        print(f"Enjoy the {random_ent} as your main event.")
        return random_ent
    while ent_trip == "n":
        random_ent = random.choice(ent_list)
        ent_trip = input(f"How does {random_ent} sound for entertainment? (Y/N)")
        if ent_trip == "y":
            print(f"Enjoy the {random_ent} as your main event.")
            return random_ent
      
confirmed_ent = user_random_ent()
# print(confirmed_ent)
print("")
print(f"You are going to {confirmed_dest} by the way of {confirmed_trans}, you will be dining at {confirmed_rest} and enjoying {confirmed_ent}.")
# Dictionary with conculsion!!

my_dictionary = {"destination": confirmed_dest, "restaurant": confirmed_rest, "transporation": confirmed_trans, "entertainment": confirmed_ent}

def user_trip_finder(dict):
    don = input("Are you happy with this trip? (Y/N)")
    for _ in dict:
        if don == "y":
            print(f"Congratulation!! Have a great trip.")
            return don
        while don == "n":
            k = input("Which part of the trip are you having problems with?")
            return don
        if k == "destination":
                return confirmed_dest
        elif k == "restaurant":
                return confirmed_rest
        elif k == "transporation":
                return confirmed_trans
        elif k == "entertainment":
               return confirmed_ent   
        else:
            print("That's not a valid option!! Try again!")
        if don == "y":
            print(f"You are going to {confirmed_dest} by the way of {confirmed_trans}, you will be dining at {confirmed_rest} and enjoying {confirmed_ent}.")
            return don
user_trip_finder(my_dictionary)