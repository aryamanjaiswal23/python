# enumerate
list1 = ["john", "jim", "david", "flint"]
t = enumerate(list1)
print(t)
for i in t:
    print(i)

for i, j in t:
    print(str(i) + "\n" + j)


# set and set functions
set1 = {10, 20, 30, "a"}
set2 = {"a", "b", "c"}
set3 = set1.union(set2)
print(set3)
set4 = set1.intersection(set2)
print(set4)
set1.update(set2)
print(set1)
set5 = set1.symmetric_difference(set2)
print(set5)
set1.symmetric_difference_update(set5)
print(set1)

# lambda function
x = lambda a: a + 1
print(x(2))


def func(num):
    return lambda a: a * num


print(func(3)(4))

l2 = [lambda args=x: args * 10 for x in range(1, 5)]
for i in l2:
    print(i())
