tup1 = ("john", 23, True)
tup2 = "john", 23, False  # can be done in either way

tup = (25,)  # have to add comma for a single valued tuple
print(tup1[1], tup2[-1])
# tup1[0] = "change" #gives error
del tup  # deletes the tuple

my_tuple = (
    "a",
    "p",
    "p",
    "l",
    "e",
)

# len() : get the number of elements in a tuple
print(len(my_tuple))

# count(x) : Return the number of items that is equal to x
print(my_tuple.count("p"))

# index(x) : Return index of first item that is equal to x
print(my_tuple.index("l"))

# repetition
my_tuple = ("a", "b") * 5
print(my_tuple)

# concatenation
my_tuple = (1, 2, 3) + (4, 5, 6)
print(my_tuple)

# convert list to a tuple and vice versa
my_list = ["a", "b", "c", "d"]
list_to_tuple = tuple(my_list)
print(list_to_tuple)

tuple_to_list = list(list_to_tuple)
print(tuple_to_list)

# convert string to tuple
string_to_tuple = tuple("Hello")
print(string_to_tuple)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[1:3]  # first to the second
print(b)
b = a[2:]  # until the end
print(b)
b = a[:3]  # from beginning
print(b)
b = a[::2]  # start to end with every second item
print(b)
b = a[::-1]  # reverse tuple
print(b)

# number of variables have to match number of tuple elements
tuple_1 = ("Max", 28, "New York")
name, age, city = tuple_1
print(name)
print(age)
print(city)

# tip: unpack multiple elements to a list with *
my_tuple = (0, 1, 2, 3, 4, 5)
x, *y, z = my_tuple
print(x)
print(y)  # gives a list of elements
print(z)

# nested tuple
a = ((0, 1), ("age", "height"))
print(a)
print(a[0])

# compare the size: tuple is smaller
import sys

my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

# compare the execution time of a list vs. tuple creation statement: we find out that a tuple is faster
import timeit

print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
