# the list with words from string
# please, do not modify it
some_iterable = input().split()

freq = {x.upper(): x.lower() for x in some_iterable}
print(freq)
