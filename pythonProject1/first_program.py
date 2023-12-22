# This is a sample Python script.
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
print("hello world")
#this is a comment
#python identation excercise
if 5>2:
    print("five is greater than two")
    if 5>2:
        print("five is greater")
        print("five is greater than two")


#Python variable
x=5
y="hello world"
print(x)
print(y)

#indentation
if 5>2:
    print("yes")
#assigning a variable
carname="volvo"
print (carname)

x=5
y=10
print(x+y)

#getting the char from index 2:4
txt="hello world"
x=txt[2:4]

#type of variables
x=5
y="jhon"
print(type(x))
print(type(y))

#Many values of multiple variables
x,y,z="orange","banana","cherry"
print(x)
print(y)
print(z)

#unpacking a List
x,y,z=["apples","banana","oragne"]
print(x)
print(y)
print(z)
"""global variables
declear variable outside and call in function"""
x="awesome"
def myfunc():
    print("my python is "+x)
myfunc()

"""creating variable inside function 
as global variable"""
x="awesome"
def myfunc():
    x="fantastic"
    print("python is "+x)
myfunc()
print("python is very "+x)
#global keyword
def myfunc():
    global x
    x="good"
myfunc()
print("python is "+x)
#print randon range
import random
print(random.randrange(1,10))
#multiline string
a="""this is 
a miltiline string"""
print(a)
a="hello world"
print(a[2])
#Looping through array
for x in "banana":
    print(x)
#string Length
a="hello world"
print(len(a))
#check string
a="the best in life is free"
print("free" in a)
if "free" in a:
    print("yes free is present")

#slicing
a="hello world"
print(a[-5:-2])
#upper and lowe case methods
a="hello world"
print(a.upper())
b="i am zahra"
print(b.lower())
#replacing a string
a="Hello world!"
print(a.replace("H","j"))
#split string
a="Hello, World"
print(a.split(","))
#string concat
a="hello"
b="world"
c=a+b
print(c)
#string formatting
age=36
txt="my name is jhon and i am {}"
print(txt.format(age))
#format argument
quantity=3
itemno=555
price=50
my_order="i want {} pieces of item{} for {} dollers"
print(my_order.format(quantity,itemno,price))
#boolean operator
print (9<10)

def func():
    return True
if func():
    print("yes")
else:
    print("no")
