
import random
from re import A
from game_data import data
from art import logo, vs
print(logo)

#Compare A:...

new_data = data
random.shuffle(new_data)

def take_data(data):
    return data.pop(-1)
a = []
a.append(take_data(new_data))


b = []
b.append(take_data(new_data))


def choose(choise):
    if choise == "A":
        return "A"
    elif choise == "B":
        return "B"
    else:
        return False


current_score = 0
def compare_follower(list_a,list_b):
    if list_a[0]["follower_count"] > list_b[0]["follower_count"]:
        return "A"
    else:
        list_a[0]["follower_count"] <= list_b[0]["follower_count"]
        return "B"
def check_result(choose, compare_score):
    if choose == compare_score:
        
        return True
    else:
        return False

game_on = True

while game_on:
    print(f"Compare A: {a[0]['name']}, {a[0]['description']}, {a[0]['country']} ")
    print(vs)
    print(f"Against B: {b[0]['name']}, {b[0]['description']}, {b[0]['country']} ")
    choise = input("Who has more followers? Type 'A' or 'B': ").upper()
    game_on = check_result(choose(choise),compare_follower(a,b))
    if game_on == True:
        current_score +=1
        print(f"You're right! Current score: {current_score}")
    else:
        print(f"Sorry, that's wrong. Final score: {current_score}")
    a = b
    b = []
    b.append(take_data(new_data))


    









#Compare B:...



    
    

