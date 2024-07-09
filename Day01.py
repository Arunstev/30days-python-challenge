#Exercise: 1

print("Addition:",3+4)
print("Subtraction:",3-4)
print("Multiplication:",3*4)
print("Division:",3/4)
print("Floor division:",3//4)
print("Exponential:",3**4)
print("Modulus:",3%4)

#Exercise: 2
name = 'Arunkumar'
country = 'India'
str3 = f"My name is {name}, From {India}"
print(str3)

#Exercise: 3
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4i-4j))
print(type(['Arun','India', 'python']))
print(type(Arun))
print(type(India))
print(type(python))

#Exercise 4
#Write an example for different data types.

num1 = int(input("enter a number:"))
num2 = float(input("enter a number:"))
print("Add:",num1+num2)
print("Sub:",num1-num2)
print("Mul:",num1*num2)
print("Div:",num1/num2)
print("Floor Div:",num1//num2)
print("Exp:",num1**num2)
print("Mod:",num1%num2)


#string
str1 = 'Hello'
str2 = 'world'
print(str1+ "" +str2)

#Boolean
print(28>67)
print(67<26)
print(77==77)
print(77!=44)


product_list = ['milk','bread','eggs','sugar']
print(product_list)

user_id = ('arun04','maxy7','Rigby')
print(user_id)

acc_no = {1001,1002,1003,1004,1005}
print(acc_no[4])

student_details = {'name':'Arun','age':22,'city':'Bangalore'}
print(student_details)


print(type(str1+""+str2))
print(type(67<26))
print(type(product_list))
print(type(user_id))
print(type(acc_no))
print(type(student_details))

#Find the Eucliadian distance between (2,3) & (10,8)

import math

x1,y1 = 2,3
x2,y2 = 10,8

dx = x2-x1
dy = y2-y1

distance = math.sqrt(dx**2 + dy**2)

print(f"The Eucliadian distance between ({x1},{y1}) and ({x2},{y2}) is {distance}")

