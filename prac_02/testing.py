# secret=6
# guess= int(input("Guess :"))
# while guess!= secret:
#     print("incorrect")
#     guess=int(input("Guess :"))
# print("Got it")
import random

# import random
# low= int(input("Low :"))
# high = int(input("High :"))
# secret= random.randint(low,high)
# guess= int(input("Guess :"))
# while guess!= secret:
#     print("incorrect")
#     guess=int(input("Guess :"))
# print("Got it")



# import random
# Do it now exercise from lecture video
# length = int(input("Enter length :"))
# width= random.randint(1,length)
# area = length*width
# print(f"Area is {area}={length}*{width}")


# def main():
#     print_line(20)
#     print("WElcome,shwe")
#     print_line(20)
# def print_line(length):
#     print("-"* length)
#
# main()

# def print_grid(number_of_rows,number_of_column):
#     column="*"*number_of_column
#     for i in range(1,number_of_rows+1,1):
#         print(column)
# print_grid(3,7)


#Version 1
# def print_grid(number_of_rows,number_of_column):
#     for i in range(number_of_rows):
#         print("*"*number_of_column)
# print_grid(2,3)

# version2
# def print_grid(number_of_rows, number_of_column):
#     print(f"{"*"*number_of_column}\n" *number_of_rows)
#
# print_grid(3,7)


# def main():
#     min_length = 8  # Minimum length for the password
#     password = get_password(min_length)
#     print_asterisks(password)
#
# def get_password(min_length):
#         password = input("Enter a password: ")
#         while len(password) < min_length:
#             print("Password is too short. Minimum length is {} characters.".format(min_length))
#             password = input("Enter a password: ")
#         return password
#
# def print_asterisks(word):
#     print('*' * len(word))
#
# main()

# nums1 = [1, -5, 2, 0, 4, 2, -3]
# nums2 = [1, -5, 2, 4, 4, 2, 7]
# result = 0
# j = 0
# print(nums1[j])
# print(nums2[j])
# while j < len(nums1):
#     if nums1[j] != nums2[j]:
#         result = result + 1
#     j = j + 1
# print(result)


def fn(x, y):
    z = x + y


print(fn(1, 2))