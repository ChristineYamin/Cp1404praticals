numbers=[]
for i in range(5):
    user_input= int(input("Number :"))
    numbers.append(user_input)
print(numbers)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[4]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of numbers is {sum(numbers)/len(numbers)}")

list_of_usernames=   usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user_name=input("Name :")
if user_name in list_of_usernames:
    print("Access granted")
else:
    print("Access Denied")
