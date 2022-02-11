# the list "meals" is already defined
# meals = [
#         {"title": "Oatmeal pancakes with apple and cinnamon", "kcal": 370},
#         {"title": "Italian salad with fusilli and ham", "kcal": 320},
#         {"title": "Bulgur with vegetables", "kcal": 350},
#         {"title": "Curd souffle with lingonberries and ginger", "kcal": 225},
#         {"title": "Oatmeal with honey and peanuts", "kcal": 440}]

cum_sum = 0
for i in range(len(meals)):
    cum_sum += meals[i].get("kcal")
print(cum_sum)

# print(sum(i.get('kcal') for i in meals))

# total = 0
# for meal in meals:
#     total += meal['kcal']
# print(total)
