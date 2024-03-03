# FILENAME = "file_question.txt"
# in_file= open(FILENAME)
# for line in in_file:
#     parts = line.strip().split(",")
#     print(parts[0])
# in_file.close()

with open("file_question.txt") as in_file:
    for line in in_file:
        parts = line.strip().split(",")
        name= parts[0].strip()
        year= parts[1].strip()
        price= parts[2].strip()
        print(f"{name} {year} ${price[0:-2]}")
