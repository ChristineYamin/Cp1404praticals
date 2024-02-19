#a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

#b
for i in range(20,0,-1):
    print(i, end= ' ')
print()

#c
user_input = int(input("Numbers of stars :"))
print("*" * user_input)


#d
user_input = int(input("Numbers of stars :"))
for i in range(1, user_input + 1):
    print("*" * i)

