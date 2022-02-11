# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
variable = dict.fromkeys(groups, None)
num_groups = int(input())
for i in range(num_groups):
    variable[groups[i]] = int(input())
print(variable)
