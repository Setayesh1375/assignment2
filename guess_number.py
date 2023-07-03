import random

computer_number = random.randint(10,40)

tedad_hads=0

for i in range(10):

    user_number = int (input())

    if computer_number == user_number:
        print("barikala")
        print("tedad_hads : ", tedad_hads+1)
        break

    elif computer_number > user_number:
        tedad_hads=tedad_hads+1
        print("boro bala")

    elif computer_number < user_number:
        tedad_hads=tedad_hads+1
        print("bia paeen")    