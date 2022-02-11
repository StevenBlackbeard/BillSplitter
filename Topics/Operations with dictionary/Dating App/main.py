# potential_dates = [{"name": "Julia", "gender": "female", "age": 29,
#                     "hobbies": ["jogging", "music"], "city": "Hamburg"},
#                    {"name": "Sasha", "gender": "male", "age": 18,
#                     "hobbies": ["rock music", "art"], "city": "Berlin"},
#                    {"name": "Maria", "gender": "female", "age": 35,
#                     "hobbies": ["art"], "city": "Berlin"},
#                    {"name": "Daniel", "gender": "non-conforming", "age": 50,
#                     "hobbies": ["boxing", "reading", "art"], "city": "Berlin"},
#                    {"name": "John", "gender": "male", "age": 41,
#                     "hobbies": ["reading", "alpinism", "museums"], "city": "Munich"}]

# def select_dates(potential_dates):
#     potentials = []
#     for i in potential_dates:
#         if i["age"] > 30 and "art" in i["hobbies"] and i["city"] == "Berlin":
#             potentials.append(i["name"])
#     return (", ".join(potentials))

def select_dates(potential_dates):
    potentials = [user["name"] for user in potential_dates if user["age"] > 30
        and "art" in user["hobbies"] and user["city"] == "Berlin"]
    return (", ".join(potentials))
