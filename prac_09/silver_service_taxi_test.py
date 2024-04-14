
from silver_service_taxi import SilverServiceTaxi

def main():
    my_taxi = SilverServiceTaxi("Taxi", 100, 50)
    my_taxi.start_fare()
    my_taxi.drive(18)
    print(my_taxi)
    print(f"New result = $ {my_taxi.get_fare():.2f}")

if __name__ == '__main__':
    main()
