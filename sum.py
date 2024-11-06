# Fundamentals of Python

# 1. Identifiers => Unique / Distinct -> variables
# 2. Literals
# 3. Object Reference
# 4. Data Types

# hello = 10
# hEllo = 10
# print(hello + hEllo)

# In Python we have 14 data types they are classified into 6 types.

# 1. Fundamental data types:
#     a. Int => a = 10
#     b. Float
#     c. Bool
#     d. Complex***
# 2. Sequential Category data types:
#     a. Str
#     b. Bytes
#     c. Bytearray
#     d. Range***
# 3. List Category data types:
#     a. List**
#     b. Tuple**
# 4. Set Category data types:
#     a. Set**
#     b. Frozenset
# 5. Dict category data types:
#     a. Dict**
# 6. None type category data types:
#     a. None

#Typecasting


# l1 = ["mango", "grapes", "banana"]
# # l2 = l1.copy()
# l2 = l1
# l2.append("apple")
# print(l2)
# l2.reverse()
# print(l2)

#######################################

# listObj1 = [56, 45, 65, 34, 90, 78, 43, 23, 32] #ascending order & descending order
# listObj1.sort(reverse = True)
# print(listObj1)

# listObj1.clear()
# print(listObj1)

# listObj1 = [56, 45, 90, 34, 90, 78, 43, 90, 32]
# listObj1.sort()
# print(listObj1)
# listObj1.reverse()s
# print(listObj1)
# print(listObj1.count(34))

#nested list

# l1 = [1, 2, [3, 4], [5, 6]]

# Tuple
# ------

# 1. Tuple is one of the pre defined classes
# 2. An object tuple allows us to store multiple values of the same type or different types
# 3. Unique & duplicate values are allowed
# 4. () ---> is used to store Tuple type object
# 5. it maintains insertion order
# 6. indexing and slicing --> allowed
# 7. Tuple object is immutable
# 8. tuple() is used to convert other types into tuple type
# 9. t1 = () => this is how we can create empty tuples

# t1 = ()
# print(t1)
# t2 = 10, 12.34, "Hello"
# print(t2)
# t3 = 10, 45, 12.45, "Hello", [1, 2, 3]
# print(t3)

# l3 = [10, 30, 49, 49, 49, 49, 45, 34]
# t3 = tuple(l3)
# print(t3)
# s
# On a tuple object, we can use index() and count() of list objects but not other functions of list because tuple object is immutable

# t3.count(49)
# print(t3.count(49))


# Set
# ====


# 1. Set is a pre defined class
# 2. homogeneous & heterogeneous values can be stored.
# 3. Only unique elements are allowed.
# 4. Insertion order is never maintained in Set
# 5. Both mutable & immutable
# 6. {} -> is used to define Set
# 7. Indexing & Slicing can't be performed
# 8. set() is used to convert other type object into set type object
# 9. s1 = set() / {}


# l3 = [10, 30, 49, 49, 49, 49, 45, 34]
# s2 = set(l3)
# print(s2)

# 1. add()

# s2.add("Soumyajit")
# print(s2)
# s2.remove(11)
# print(s2)

# s3 = {10, 30, 49, 49, 45, 34}
# # print(s3)
# s4 = {49, 45, 34}
# # print(s4.issubset(s3))
# # print(s3.issuperset(s4))

# s5 = {1, 2, 3}
# s6 = {1, 2, 4}
# # print(s6.isdisjoint(s5))

# # union of set

# resultOfUnion = s5.union(s6)
# # print(resultOfUnion)

# resultOfIntersection = s5.intersection(s6)
# # print(resultOfIntersection)

# resultOfDifference = s6.difference(s5)
# # print(resultOfDifference)

# s7 = {10, 20, 30, 40}
# s8 = {30, 40, 45, 65, 64, 78, 90, 87, 10, 20, 30, 40}

# s7.update(s8) #It is similar to Union but update function doesn't return a new set rather it updates the sourse set with the values of Source set & destination set

# print(s7)


# result_of_symmetic_difference = s7.symmetric_difference(s8)
# # print(result_of_symmetic_difference)

# FrozenSet

# 1. ...
# 2. ...H & H
# 3. Unique
# 4. Immutable
# 5. Insertion order not preserved
# 6. Indexing & slicing not allowed
# 7. frozenset()

# fs = frozenset()
# ========================================================

# Dict

# 1. Data is stored in Key & Value pair
# 2. The keys couldn't be duplicate
# 3. The values could be duplicate
# 4. representation {key : value}
# 5. To convert one type of values in to dict type we use dict()
# 6. Dict object is Mutable

# Empty dict

# dictObj = {}
# dict1 = dict()

# dict1["name"] = "Siddhartha"
# dict1["age"] = 20
# dict1["university"] = "BU"
# dict1[10] = 10

#  #if keyname is Str then keyname must be written within single or double quote, If keyname is numeric then we can use it without any quotation

# dict1["university"] = "CU"

# print(dict1)

# name = dict1.get("university")
# # print(name)

# var1 = dict1.keys()
# var2 = dict1.values()

# print(var1, type(var1))
# print(var2, type(var2))

# dict1["place"] = "Burdwan"

# dict1.pop(10)

# print(dict1)

# dict2 = {"favourite_food":"Mutton", "favourite_colour" : "Black"}

# dict1.update(dict2)

# print(dict1)
# print(dict2)

# str = "SOUMYAJIT"
# str1 = str[-1:-8:-3]
# print(str1)

# d1 = dict()
# d1["name"] = "Javed"
# d1["lastName"] = "Akhter"
# d1["Occupation"] = "Writer"
# d1["age"] = 82


# print('age =', d1.get("age"))
# d1Keys = d1.keys()
# print(d1Keys)

# d1Values = d1.values()
# print(d1Values)


# d1 = dict()
# d1["name"] = "Javed"
# d1["lastName"] = "Akhter"
# d1["Occupation"] = "Writer"
# d1["age"] = 82

# # print(d1)

# d2 = dict()
# d2["child"] = "Farhan"
# d2["child_lastname"] = "Akhter"

# d2.update(d1)

# print(d1)
# print(d2)

#clear("age")

# x = None
# print(x, type(x))

# Batch Mode Approach
# Interactive mode Approach

#to read data from the keyboard in python we have 2 pre defined functions
# a. input()
# b. input(message)

# a = int(input())
# print(type(a) , " Welcome to Python " , a) #"7887"


# Write a python program which accepts 3 integer values and adds them.

# s = dict()
# # name, roll, marks, college
# s["name"] = input("Enter the name : ") 
# s["roll"] = input("Enter the roll : ") 
# s["marks"] = input("Enter the marks : ") 
# s["college"] = input("Enter the college : ")

# if(int(s.get("marks")) < 75):
#     s["grade"] = "BAD"
# else:
#     s["grade"] = "VERY GOOD"



# print(f"The name is {s.get("name")}, roll is {s.get("roll")}, marks = {s.get("marks")}, and the college name is {s.get("college")}, your grade is {s.get("grade")}")

#Write a program to convert the temperature from celcius to farenhite
#F = 9/5C + 32
# F = (1.8 * C) + 32


# celciusUI = float(input("Enter the celcius temperature: "))
# print(f"The corresponding farenhite temperature is {(celciusUI * 1.8) + 32} F")

# Write a python program to demonstrate all the arithmatic operations in python

# flag = True

# while flag == True:
#     a = float(input("Enter the first number: "))
#     b = float(input("Enter the Second number: "))
#     operator = input("Enter the operation you want to perform: ")

#     if(operator == "+"):
#         print(f"Addition of the given input is: {a + b}")
#         flag = bool(int(input("Do you want to continue? Press 0 for no 1 for yes.")))
#         print(flag)
#     elif(operator == "-"):
#         print(f"Subtraction of the given input is: {a - b}")
#         flag = bool(int(input("Do you want to continue? Press 0 for no 1 for yes.")))
#     elif(operator == "*"):
#         print(f"Multiplication of the given input is: {a * b}")
#         flag = bool(int(input("Do you want to continue? Press 0 for no 1 for yes.")))
#     elif(operator == "/"):
#         print(f"Division of the given input is: {a / b}")
#         flag = bool(int(input("Do you want to continue? Press 0 for no 1 for yes.")))
#     elif(operator == "//"):
#         print(f"Floor division of the given input is: {a // b}")
#         flag = bool(int(input("Do you want to continue? Press 0 for no 1 for yes.")))
#     elif(operator == "**"):
#         print(f"Exponent of the given inputs is: {a ** b}")
#         flag = bool(int(input("Do you want to continue? Press 0 for no 1 for yes.")))
#     elif(operator == "%"):
#         print(f"Modulus of the given input is: {a + b}")
#         flag = bool(int(input("Do you want to continue? Press 0 for no 1 for yes.")))
#     else:
#         print(f"Enter Correct Arithmatic Operator")
#         flag = bool(int(input("Do you want to continue? Press 0 for no 1 for yes.")))

# bool(0) -> False
# bool("0") -> True

#Swap numbers

# a = 10
# b = 20

# a, b = b, a

# print(a, b)


# c = a
# a= b
# b = c

# print(a, b)

# print(15 >> 1)

# a = 257.67
# b = 257.67

# print( a is b)

# l1 = list(range(10, -1, 3))
# print(l1)

# for i in range(10, -1, -3):
#     print(i, end = ", ")

#Write down the multiplication table for any user given number 




# num = int(input("Enter the Number: "))

# print("*" * 20)

# if(num > 0):

#     for i in range(0, 10):
#         print(f"{num} X {i+1} = {num * (i+1)}")

# else:
#     print("Invalid input.")

# print("*" * 20)


# *
# **
# ***
# ****
# *****

# n = int(input("Enter number of lines you want to print: "))

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print("* ", end = "")
#     print()

# import math

# def sum(a, b):
#     return a + b

# a = float(input("1st: "))
# b = float(input("2nd : "))

# print (f"The total of {a} + {b}  is: {math.floor(sum(a, b))}")


# a = 50
# def f_function():
#     a = 10
#     print(a)


# f_function()

# print(a)



# def power(x, n):
#     result = x ** n
#     l1 = [1, 2, 3, 4, 5]
#     return x, n, result, l1

# value, exponential, res, list1 = power(4, 4)
# print(f"{value} to the power {exponential} equals {res}, the list is {list1}")

# Q. Find the max & min element of a list and return together.

# l1 = [45, 67, 23, 47, 12, 1, 2, 99, 76, 43]

# def findMax(l1):
#     max = -9999999999
#     # min = 99999999999


#     for ele in l1:
#         if(ele > max):
#             max = ele
        # if(ele < min):
        #     min = ele

    # return max

# max, min = findMaxAndMin(l1)

# print(max, " ", min)

# Q. Find the 2nd max element of a list and return together.


# def findSecondMax(l1):
#     l3 = l1

#     for i in range(0, 5):
#         maxim = findMax(l1)
#         l1.remove(maxim)
    
#     nthMax = findMax(l1)

#     l1 = l3

#     return nthMax

# secondLargest = findSecondMax(l1)
# print(secondLargest)

# 1. find max, min
# 2. find 2nd max , 2nd min
# 3. find nth max
# 4. find nth min
# 5. find nth max, mth min


# def findNthMaxAndMthMin(n=1, m=1):
#     for i in range(n):
#         print(m)


# findNthMaxAndMthMin()

# def find_max_min(l1 = [10, -7,45, 89, -2, 10, -10]):
#     max = -999999999999
#     min = 9999999999999
#     for ele in l1:
#         if(ele > max):
#             max = ele
#         if(ele < min):
#             min = ele
#     return max, min, 10, [True, False]


# maximum, minimum, value, array = find_max_min([10, -7,45, 91, -12, 10, -10])

# print(tups)



# Variable length parameters:

# Function Overloading:

# Write a python program that'll display keyword variable number of values:

# def show(** n): #n is called variable length parameter whose type is dictionary
#     # print(n)
#     for ele in n.items():
#         k, v = ele
#         print(f"{k} : {v}")

# show(name = "Ankan", surname = "Layek", age = 18, marks= "80%")


# def tup_show(* n):
#     for ele in n:
#         print(ele)


# tup_show("Falguni", "Sen")

# write single function to calculate variable number of element's addition:

# def sum(*n):
#     sum = 0
#     for ele in n:
#         sum += ele
#     return sum

# print(sum(10, -10, 18, 90, -65, -45, 34, 187, -12))

#W A P P : To find total marks secured by students who are studying different subjects in different classes

# def findTotalMarks(name, clazz, **marks):
#     print("-" * 10)
#     total = 0
#     for k, v in marks.items():
#         total += v

#     print(f"Name : {name}, Class : {clazz}, Total Number: {total} ")



# findTotalMarks("Vidit", "X", Eng = 90, Beng = 55, Geo = 99, Hist = 80, Maths = 100)
# findTotalMarks("Harshita", "XII", Eng = 99, Beng = 80, Maths = 100)
# findTotalMarks("Divyanshu", "MTech", VLSI = 74)


# Local Variable : Corresponding function body -> variable declare -> local variable 

# Global Variable : defined before all the function definitions. the purpose is to place the common values

# global keyword : when we want to modify the value of global variable within the function definition then we must refer to that global variable using a global keyword and modification must take place. Without a global keyword, global variable's valuees can't be modified within the function definition and we will get some error.

#Global Variable
# s = "PYTHON"
# a = 5

# def read_s():
#     #Local Variable
#     s = "java"
#     print(s)

# def modify_a():
#     global a 
#     a = a*2
#     return a

# # print(s)

# # print(a) 
# b = modify_a()

# print(a + 10)

# print(a) 
# print(b)

# read_s()

# globals()

# whenever the local variable & global variable names are same there might be a chance of ambiguity then to do the operations on both local and global variables directly we need to use globals() concept
# globals() returns all the global variables in the form of dictionary
# To differentiate between global variables and local variables in functions the global variables must be retrieved by using globals() function.


# sauvik = 10
# siddhartha = 20 
# arju = 30
# falguni = 40

# def perform_modification():

#     print(sauvik, siddhartha, arju, falguni, gsauvik, gsiddhartha) #10 20 30 40 ? ? 

#     global arju, falguni
#     arju += 10
#     falguni -= 20

#     gsauvik = globals()['sauvik'] + 20 #gsauvik = 10
#     gsiddhartha = globals()['siddhartha'] + 20 #gsiddhartha = 20

#     print(sauvik, siddhartha, arju, falguni, gsauvik, gsiddhartha) #10 20 40 20 30 40

# print(sauvik, siddhartha, arju, falguni) #10 20 30 40 step 1 

# perform_modification()

# print(sauvik, siddhartha, arju, falguni) #10 20 40 20

# def sum_of_two_nums(a, b):
#     c = a + b
#     return c

# add_op = lambda x,y : x + y #Returns addition of two numbers

# print(sum_of_two_nums(10, 20))

# print(add_op(10, 60))

#Write a lambda function to return the biggest of three numbers:

# biggest_of_three = lambda x, y, z : x if (x > y and x > z) else (y if(y>z) else z)
# biggest_of_two = lambda x, y : x if x > y else y

# print(biggest_of_three(322, 177, 76))

# def b_o_t(x = 55, y = 10, z = 50):
#     if(x > y and x > z):
#         return x
#     elif(y > z):
#         return y
#     return z

# def even(x):
#     if(x % 2 == 0):
#         return True
#     else:
#         return False

# def odd(a):
#     if(a % 2 != 0):
#         return True
#     else:
#         return False


# lst = [10, 76, -77, 54, -34, 31, 71, -83, 98, 99, 55]

# r1 =list(filter(lambda x : x % 2 == 0, lst))

# print(r1)

#Make a list with the elements of s1 so that all elements on that list is lesser than 10
# s1 = {1, 3, 6, 10, 11, 13, 4, 7}

# print(list(filter(lambda a : a >= 10, s1)))

# square all the element of s:

# t1 = list(map(lambda a : a*a, s1))

# print(t1)
# import functools as ft

# s1 = {187, -70, 6, 109, 11, 19, 40, 7, -67, -56}

# max, min = ft.reduce(lambda x,y : x if x > y else y, s1) , ft.reduce(lambda x,y : x if x < y else y, s1)

# print(max, min)


# class Student:

#     """This is the Student Class that describes all the details about Students"""
#     #Properties
#     def __init__(self, name, age, roll, addr):
#         self.name = name
#         self.age = age
#         self.roll = roll
#         self.addr = addr

#     #Behaviour
#     def printDetails(self):
#         print(f" Hello My name is : {self.name}, my age is {self.age}, my addres is : {self.addr}, roll : {self.roll}" )


# sid = Student("Siddhartha", "21", "567854", "Kolkata")
# ank = Student("Ankan", "22", "567855", "Burdwan")
# print(Student.__doc__)
# help(Student)
# sid.printDetails()
# ank.printDetails()


# class Node:

#     def __init__(self, data, next):
#         self.data = data
#         self.next = next
    
#     def __init__(self, next):
#         self.next = next


# n3 = Node(15, None)
# n2 = Node(10, n3)
# n1 = Node(5, n2)
# head = Node(n1)

class Student:
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age

# s1 = Student("Soumyajit", 21)
# ctrl + / to commemt & uncomment

s2 = Student()
s2.setName("Sohona")
s2.setAge(20)

print(s2.getAge(), s2.getName())


# HomeWork: Create an Employee Class & create parameterized constructor & getters and setter with atleast 5 instance and 2 static variables.

# class Outer:
#     def __init__(self):
#         print("This is Outer Class")
    
#     class Inner:
#         def __init__(self):
#             print("This is Inner Class")
#         def m1(self):
#             print("This is Inner Class's Function m1()")

#         class Inner2:
#             def __init__(self):
#                 print("This is Inner to Inner")

        

# o1 = Outer()
# i1 = o1.Inner()
# i2 = i1.Inner2()
# i1.m1()

# i2 = Outer().Inner().Inner2()







