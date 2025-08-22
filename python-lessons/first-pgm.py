# This is my first program!
print("Hello, World!")
# This program prints a greeting message to the console.
print("33 + 44 =", 33 + 44)
print("subtraction: ", 100 - 55)
print("multiplication: ", 7 * 6)
print("division: ", 100 / 5) 
print("modulus: ", 100 % 3)
print("exponentiation: ", 2 ** 3)  # 2 raised to the power of 3
print("floor division: ", 100 // 3)  # Division that rounds down to the nearest whole number
print("This is my first Python program!")

# variables
my_name = "Rani"
age = 25

# 100 lines later
print(f"hello my name is {my_name} and I am {age} years old.")
name_and_age =  my_name + str(age)
print("My name and age combined: ", name_and_age)
# Using f-strings for formatted output
print(f"My name is {my_name} and I am {age} years old.")

# boolean (true, false)
is_student = True
is_verified = False
# Using a boolean variable  to check if the person is a student
if is_student:
    print("I am a student.")
else:
    print("I am not a student.")        
# Printing the boolean variable     
# This will print the value of is_student 
print("Is student:", is_student)

# Using a boolean variable to check if the person is verified
if is_verified:
    print("I am verified.") 
else:
    print("I am not verified.")

# Printing the boolean variable
if age > 18:
    print("You are an adult.")  
elif age>=18 and age < 1:
    print("You are a minor.")
else:
    print("You are a child.")

message = "Practice makes perfect!"
print(message)
print(message.upper())  # Convert to uppercase
print(message.lower())  # Convert to lowercase
print(message.replace("perfect", "better"))  # Replace a word in the string
print(message.split())  # Split the string into a list of words 
print(message.find("makes"))  # Find the index of a substring
print(message.count("e"))  # Count occurrences of a character
print(len(message))  # Get the length of the string
print(message[0])  # Access the first character of the string       
print(message[-1])  # Access the last character of the string
print(message[0:8])  # Access a substring from index 0 to 7 
print(message[9:])  # Access a substring from index 9 to the end
print(message[:8])  # Access a substring from the start to index 7  

