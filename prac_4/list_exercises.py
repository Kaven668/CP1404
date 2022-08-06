# 1.Basic list operations
list = []
for i in range(5):
    number = int(input("Number:"))
    list.append(number)

print("The first number is:",list[0])

print("The last number is:",list[-1])

print("The smallest number is:",min(list))

print("The largets number is:",max(list))

print("The average of the number is:",sum(list)/len(list))

# 2.Woefully inadequate security checker

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
name_input = input("Input a name:")
if name_input not in usernames:
    print("Access denied")
else:
    print("Access granted")





