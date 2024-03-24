
FILENAME = "guitars.csv"
from guitar import Guitar
def main():
    "Read data from the file and results the datas"

    guitars = read_data_from_file(FILENAME)
    get_userinput(guitars)
    write_new_data(guitars)
    results_guitars(guitars)


def read_data_from_file(FILENAME):
    """Read the data from the file """
    guitars = []
    in_file = open(FILENAME, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], parts[2])
        guitars.append(guitar)
        guitars.sort()
    in_file.close()
    return guitars

def results_guitars(guitars):
    for guitar in guitars:
        print(guitar)
def get_userinput(guitars):
    """ Getting input from the user"""
    name = input("Name : ")
    year = int(input("Year : "))
    cost = float(input("Cost : "))
    print(f"{name} {year} {cost}")
    guitars.append(Guitar(name,year,cost))

def write_new_data(guitars):
    "Write new data to the file"
    with open(FILENAME,"w") as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year} {guitar.cost}")






main()
