# Counter
from collections import Counter

a = "aaaabbbcddeeeefffff"
co = Counter(a)
print(co)

print(co.items())
print(co.keys())
print(co.values())

my_list = [0, 1, 0, 1, 2, 1, 1, 3, 2, 3, 2, 4]
co = Counter(my_list)
print(co)

# most common items
print(co.most_common(1))

# Return an iterator over elements repeating each as many times as its count.
# Elements are returned in arbitrary order.
print(list(co.elements()))
