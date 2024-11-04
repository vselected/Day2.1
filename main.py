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
#myfile = open("test.txt")
#print(myfile.read())
#myfile.seek(0)
#print(myfile.read())
#myfile.seek(0)
#print(myfile.readlines())
#myfile.close()

with open("test.txt", mode="r") as f:
    print(f.read())

with open("test.txt", mode="a") as f:
    print(f.write("\nNew Line"))

with open("test.txt", mode="r") as f:
    print(f.read())

with open("dadjidwada.txt", mode="w") as f:
    print(f.write("New file"))

with open("dadjidwada.txt", mode="r") as f:
    print(f.read())

# Exercise
# File I/O
# This exercise will require several lines of code.
# Write a script that opens a file named 'test.txt' , writes 'Hello World'  to the file, then closes it.
# For example, the following code opens a file called 'myfile.txt' , writes 'This is my file' , and closes it:
# x = open('myfile.txt', 'w')
# x.write('This is my file')
# x.close()

with open("test.txt", mode="w") as f:
    f.write("Hello World")
    f.close()


