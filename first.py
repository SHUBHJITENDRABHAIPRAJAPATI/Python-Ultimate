#Shubh learning python

#in python,not more like c++ you need to write data type you just need to wrie variable name and done

#below is perfect example;

name="Shubh"
age=19
weight=60.00

#now to print these values we use print function

print(name)
print(age)
print(weight)


print("Shubh")#this will print shubh,just regular string

"""
here is output of above code:
Shubh
19
60.0
"""

# datatypes in py:int,float,str,bool,none.
# also there are few reseved keyword you cann't use for variable name;
"""
1. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

Operators:
+ , - , * , / , % , ** , //

Uses:

+ → Addition

- → Subtraction

* → Multiplication

/ → Division

% → Modulus (remainder)

** → Exponent (power)

// → Floor division

2. Assignment Operators

Assignment operators are used to assign values to variables and perform operations at the same time.

Operators:
= , += , -= , *= , /= , %= , //= , **=

Uses:

= → Assigns a value

+= → Adds and assigns

-= → Subtracts and assigns

*= → Multiplies and assigns

/= → Divides and assigns

%= → Modulus and assigns

= → Floor division and assigns

**= → Exponent and assigns

3. Comparison Operators

Comparison operators are used to compare two values and return True or False.

Operators:
== , != , > , < , >= , <=

Uses:

== → Equal to

!= → Not equal to

> → Greater than

< → Less than

>= → Greater than or equal to

<= → Less than or equal to


3. comparison oprator
not:use to reverse the result,true to false and false to true
and:logical and operator,if both the statements are true then only it will return true
or:logical or operator,if any of the statement is true then it will return true

"""




          #type casting & conversion in python

#type conversion
a=2
b=6.25

sum=a+b

print(sum)

#type casting

a=int("2")
b=6.25

sum=a+b

print(type(a))
print(sum)

"""
8.25
<class 'int'>
8.25
"""


#user input in python
name=(input("enter name: " ))
print("welcome",name)

"""
enter name: shubh
welcome shubh
enter age: 21
your age 21
<class 'int'>
"""

#type casting in input
age=int(input("enter age: "))
print("your age",age)
print(type(age))





#let's practice


#question: take user input for square and print area
print("let;s find sequre arear")
a,b
a=int((input("enter a:")))
b=int((input("enter b:")))
sum=a*b
print("sum is: ",sum)

#question: take user input for radius and print area of circle
print("let's find area of circle")
r=float(input("enter radius:"))
area=3.14*r*r
print("area is:",area)

#question:WAP to take user input for name and age and print them in a sentence
name=input("enter name:")
age=int(input("enter age:"))
print("your name is",name,"and your age is",age)  

#question:WAP to take user input for two numbers and print their sum, difference, product and quotient
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
sum=num1+num2
diff=num1-num2
prod=num1*num2
quot=num1/num2 
print("sum is:",sum)
print("difference is:",diff)
print("product is:",prod)
print("quotient is:",quot)


#question:to input 2 floating point numbers & print their average
num1=float(input("enter num1:"))
num2=float(input("enter num2:"))
avg=(num1+num2)/2
print("average is:",avg)

