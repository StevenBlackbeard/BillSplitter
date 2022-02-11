# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())
# test_dict = {"a": 43, "b": 1233, "c": 8}
key_list = list(test_dict.keys())
val_list = list(test_dict.values())
min_val = min(val_list)
max_val = max(val_list)
print("min: " + key_list[val_list.index(min_val)])
print("max: " + key_list[val_list.index(max_val)])

# print("min:", min(test_dict, key=test_dict.get))
# print("max:", max(test_dict, key=test_dict.get))