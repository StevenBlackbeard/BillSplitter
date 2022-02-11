import random

num_in = int(input("Enter the number of friends joining (including you):"))
print()
if num_in <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends_list = []
    for i in range(num_in):
        friends_list.append(input())
    print()
    bill = float(input("Enter the total bill value:"))
    print()
    pay = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    print()
    if pay == "Yes":
        lucky = friends_list[random.randint(0, num_in - 1)]
        print(f'{lucky} is the lucky one!')
        dict_out = dict.fromkeys(friends_list, round(bill / (num_in - 1), 2))
        dict_out[lucky] = 0.0
    else:
        print("No one is going to be lucky")
        dict_out = dict.fromkeys(friends_list, round(bill/num_in, 2))
    print()
    print(dict_out)
