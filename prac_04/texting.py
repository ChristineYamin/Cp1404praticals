# names=["Dior","Chanel"]
# print(names)
# print(names[1])
# print(names[-1])

# for name in names:
#     print(name)
# index error
# print(names[9])
#
# try:
#     print(names[9])
# except IndexError:
#     print("No Such Index")
#
# # if "Dior" in names:
# #     print("Dior is in the list")
# # if "Gucci" not in names:
# #     print("Gucci is not in the list")
#
# numbers = [2,90,45,78,34]
# numbers.reverse()
# print(numbers)
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# print(len(numbers))
#
# numbers.append(100)
# print(numbers)
#
# del numbers[1]
# print(numbers)
#
# numbers.remove(100)
# print(numbers)
#
# numbers.sort()
# print(numbers)

# from operator import itemgetter
#
# data= [["Eileen",25],["kelly",29],["Edward",18],["Lea",16]]
# print(data[0])
# print(data[0][1])
#
# data.sort()
# print(data)
#
# data.sort(key=itemgetter(1))
# print(data)

# ages=(2,56,78,23,78)
# print(max(ages))
# print(min(ages))
# print(sum(ages))
# print(len(ages))

# def format_date(day,month,year):
#     return f"{day}/{month}/{year}"
# date=(22,12,1990)
# date=format_date(*date)
# print(date)

words="This is python"
# words=words.split()
# print(words)

# for word in words:
#     print(word)

# print([word for word in words])

text = "Enjoy the test"
result = text.strip().split()[0]
