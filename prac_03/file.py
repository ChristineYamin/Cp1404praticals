# 1
# user_name=input("Name :")
# out_file = open("name.txt","w")
# print(user_name,file=out_file)
# out_file.close()

# 2
# FILENAME="name.txt"
# in_file=open(FILENAME)
# text=in_file.read()
# in_file.close()
# print(f"Your name is {text}.")

# 3
FILE=("numbers.txt")
# in_file=open(FILE)
# text1=int(in_file.readline())
# text2=int(in_file.readline())
# in_file.close()
# print(text1+text2)

# 4
total=0
in_file=open(FILE)
for line in in_file:
    total_value=int(line.strip())
    total+=total_value
print(f"Total value in {FILE} is {total}")
in_file.close()
