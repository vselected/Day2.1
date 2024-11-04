# Tuples
# Tuples are immutable
t = (1, 2, 2, 2, 3)
my_list = [1,2,3]
print(type(t))
print(type(my_list))
print(t.count(2))
print(t.index(3))

# Sets
my_set = set()
print(my_set)
my_set.add(1)
print(my_set)
my_set.add(1)
print(my_set)
# Only unique values
my_set.add(3)
print(my_set)

# Exercise
# Sets
# Write an expression that would turn the string 'Mississippi'  into a set of unique letters.
# For example:
# set('Parallel')
# would return the set {'P', 'a', 'e', 'l', 'r'}

my_set = set("Mississippi")
print(my_set)

# Booleans
print(type(True))
print(1==1)
print(1>2)

# I/O with Basic files in Python
myfile = open("test.txt")
print(myfile.read())
myfile.seek(0)
print(myfile.read())
myfile.seek(0)
print(myfile.readlines())
myfile.close()
with open("test.txt") as my_new_file:
    contents = my_new_file.read()
    print(contents)