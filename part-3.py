# #lists and its funcitons
# list1=["john",23,"jacobs",33,False]
# list1[2]="trivia"
# print(list1[0],list1[0:3])
# print(list1.index("john"))
# t=list1.append(232)
# list2=[1,4,3,6,13224]
# list2.sort()
# print(list2)

# #tuples
# tup1=(3,4)
# # tup1[0]=2
# tr=[(3,4),(1,2),(2,2)]
# tup1.count(3)

# #dictionaries
# dict={
#     "jan":"january",
#     "feb":"feburary",
#     "mar":"march",
#     "apr":"april",
#     "jun":"june",
#     "dec":"december"
# }
# print(dict["jan"],dict.get("dec"))
# print(dict.get("nov","not available"))
# i=10
# while i:
#     print(i)
#     i-=1
    
# # guess game using while loop

# secret="bruh"
# guess_no=5
# guess=""
# while guess!=secret and guess_no:
#     guess=input("enter a guess:")
#     guess_no-=1
#     if guess_no==0: print("out of guesses!")
#     else: 
#         if guess==secret: print("you won")

# temp=["john","johnny boy","jimmy","pietroo"]
# for i in temp:
#     print(i)
    
# for t in range(len(temp)):
#     print(temp[t])
    
# def to_pow(base,power):
#     t=1
#     for i in range(power):
#         t=t*base
#     return t
# print(to_pow(3,4))


# # 2d lists
# l=[[1,2,3],[5,4,2],[4,6,7]]
# print(l[2][2])
# for row in l:
#     for col in row:
#         print(col)
        

# def reader(phrase):
#     temp=""
#     for  letter in phrase:
#         if letter.lower() in "aeiou":
#             temp=temp+ "/"
#         else: temp=temp + letter
#     return temp

# print(reader(input()))

# #try-except
# try: f=10/0
# except ZeroDivisionError as err: print(err)

set1 = {"abc", 34, True, 40, "male",1}
set2={1,1}
print(set2)
print(type(set1))