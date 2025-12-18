#lets practice if else
age = int(input("Enter your age: "))

if age >= 18:
     print("You are eligible to vote.")
else:
     print("You are not eligible to vote.")


#lets practice elif
marks = int(input("Enter your marks: "))

if marks >= 90:
     print("Grade: A")
elif marks >= 80:
     print("Grade: B")
elif marks >= 70:
     print("Grade: C")
else:
     print("Grade: D")
#nested if else
num = int(input("Enter a number: "))
if num > 0:
     print("Positive number")
else:
     print("Negative number")
     if num == 0:
          print("Zero")
     else:
          print("Negative number")


#ternary operator
num = int(input("Enter a number: "))
result = "Even" if num % 2 == 0 else "Odd"
print(result)


