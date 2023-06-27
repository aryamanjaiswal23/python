num=int(input("Enter a number:"))
if num%5==0 and num%4==0:
    print("multiple 20")
elif num%2==0 and num%3==0: print("multiple of 6")
else: print("not a multiple")

if num%10==0:
    if num%6==0:
        if num%3==0:
            print("multiple of 3")

# functions

# built-in function
temp=min(1,2,456,7,67,3.42)
print(temp)
print(pow(3.42,3))

# user defined
n1=int(input("enter a number: "))
def func():
    if n1%4==0: return True
    else: return False
    
print(func())

# altering data
def func1(n):
    n*=100
    n1=n
    print("new number",n)
    return n

func1(n1)

# string built in funcitons
s1="Welcome to home! Help yourself with some chunkies."
print(s1.find("Help"))
print(s1.find("Help",18,24))
s2=s1.replace("Welcome","Good")
print(s2)
print(".".join(s1))

s3="hello how are you {name}".format(name="yunu")
print(s3)