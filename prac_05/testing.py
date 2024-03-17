# name_and_age={"Bill":21,"Jane":34,"Sven":56}
# print(name_and_age)

# print(name_and_age["Jane"])
# print(len(name_and_age))

# name_and_age["Lukas"]=20
# print(name_and_age)

# name_and_age["Lukas"]="ten"
# print(name_and_age)
#
# del name_and_age["Lukas"]
# print(name_and_age)
#
# print(name_and_age.pop("Bill"))
# print(name_and_age)

# name_and_age["Jane"]=name_and_age["Sven"]
# print(name_and_age)
#
# for name in name_and_age:
#     print(name)
#
# for i in range(len(name_and_age)):
#     print(i)

# name_and_age={"Bill":61,"Jane":34,"Sven":56}
# #first item "Bill" is key and the second item 61 is value.
#
# print(name_and_age) #Both value are added
# print(name_and_age.keys()) #Only key is printed
# print(name_and_age.values()) #only value is printed
# print(name_and_age.items()) #Both are printed
# print(max(name_and_age.values()))
#
# for key in name_and_age:
#     print(key)
#
# for key in name_and_age:
#     print(f"{key} is {name_and_age[key]}")
#
# for key,value in name_and_age.items():
#     if value==56:
#       print(key,value)
#
# for name,age in name_and_age.items():
#     print(f"{name} is {age}")
#
# for name,age in name_and_age.items():
#     if age== max(name_and_age.values()):
#         print(f"{name} is {age}")
#
# print(list(name_and_age.keys())) #change to list
#
# names = list(name_and_age.keys())
# print(names)
# for name in names:
#     print(f"{name} is {name_and_age[name]}")
#
# print("".join([f"{name} is {name_and_age[name]}\n" for name in names]))

# name_to_age={"Bill":21,"Jane":34,"Sven":56}
# print(name_to_age)
# name = input("Enter Name: ")
# age = int(input("Enter age: "))
#
# name_to_age[name] = age
# print(name_to_age)
#
# for name,age in name_to_age.items():
#     print(f"{name:<6} - {age:>6}")
before = [1, 4, 0, -1]
after = before.sort()
print(after[0])