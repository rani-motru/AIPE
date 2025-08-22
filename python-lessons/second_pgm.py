#create a list(array)

#index is the position on the list
#           0  1  2  3
my_list = ["red", "blue", "green"]

my_list.append("yellow") #add to the end of the list
my_list.insert(1, "orange") #add to a specific position
my_list.remove("blue") #remove an item from the list
print(my_list) #print the entire list   
print(my_list[0]) #print the first item in the list
print(my_list[-1]) #print the last item in the list
print(my_list[1:3]) #print items from index 1 to 2
print(len(my_list)) #print the length of the list
my_list.sort() #sort the list in ascending order
print(my_list) #print the sorted list
my_list.reverse() #reverse the order of the list
print(my_list) #print the reversed list
my_list.pop() #remove the last item from the list
print(my_list) #print the list after popping the last item

print(my_list.index("red"))  # Find the index of an item in the list
print("Is 'green' in the list?", "green" in my_list)  # Check if an item is in the list
print("Is 'blue' in the list?", "blue" in my_list)  # Check if an item is in the list   

#for loop
for color in my_list:
    print("Color:", color)  # Print each color in the list      

for i in range(10):
     print("Number:", i)


#simple chat messages

#store the list of messages
messages = []

#take the user input
user_input = input("Enter a message (type 'exit' to stop): ")

user_message = {
     "role": "user",
     "content": user_input
}
#add the user input to the messages
messages.append(user_message)

#have  the model respond to the user input
messages.append({"Role": "assistant","content": "Here is the Poem..."})
print("Messages:", messages)  # Print the list of messages

# Accessing the first message in the list
message_1 =messages[0]
print("User message:", message_1["content"])  # Print the user's message



#show the messages
for message in messages:
    print(f"{message['role']}: {message['content']}")  # Print each message with its role





#dic/object
my_dict = {
    "name": "Rani",
    "age": 25,
    "city": "New York",
    "is_student": True
}
print(my_dict)  # Print the entire dictionary