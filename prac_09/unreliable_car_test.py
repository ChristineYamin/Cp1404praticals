
from unreliable_car import UnreliableCar

def main():
    # Create a new car object
    my_car = UnreliableCar("Unreliable", 100,50)

    # Drive the car 10 km
    distance_driven = my_car.drive(10)
    print(f" Distance driven : {distance_driven} km ")

if __name__ == "__main__":
    main()
