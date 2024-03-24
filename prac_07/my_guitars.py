




from guitar import Guitar
def main():
    "Read data from the file and results the datas"
    FILENAME = "guitars.csv"
    guitars = read_data_from_file(FILENAME)
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
main()
