# put your python code here
list_in = input().lower().split()
# list_in = [x.lower() for x in list_in]
freq = {}
# freq = {x: list_in.count(x) for x in list_in}
for item in list_in:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

for key, value in freq.items():
    print(key, value)
