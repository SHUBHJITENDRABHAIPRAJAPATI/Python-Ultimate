#two ways to define a string

name = "Shubh"
city = 'Kingston'

#2:type of Quotes
a = "Hello"
b = 'World'
c = """This is
a multiline string"""

#3:indexing(acces character using index)
word = "Python"
print(word[0])   # P
print(word[-1])  # n
print(word[2])   # t

#4:slicing (acces multiple characters using index)
text = "Programming"
print(text[0:6])    # Program
print(text[3:])     # gramming
print(text[:5])     # Program
print(text[-7:-1])  # amming

#5:length of string
message = "Hello, World!"
print(len(message))  # 13

#6:string methods
text = " hello world "

text.upper()        # HELLO WORLD
text.lower()        # hello world
text.strip()        # removes spaces
text.replace("world", "Python")
text.split()        # converts to list
text.find("o")     # 4
text.count("l")    # 3
text.startswith(" h")  # True
text.endswith("d!")    # False
text.capitalize()   # Hello world
text.title()        # Hello World
text.isalpha()     # False

#7:string concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # John Doe


#8:string formatting(very important)
name="Shubh"
age=19
print("My name is{name} and I am {age}")



#9:escape characters
print("he said,\"Hello!\"")  # he said,"Hello!"
print('Line\nLine2')

#10:check string
text="python programming"

print("python" in text)      # True
print("java" not in text)    # True
