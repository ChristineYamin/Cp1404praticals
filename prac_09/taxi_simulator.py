from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "(q)uit, (c)hoose taxi, (d)rive"

def main():
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0
    current_taxi = None
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "C":
            print("Taxis avaliable")
            display_taxis(taxis)
            value = int(input("Choose Taxi: "))
            if value >= 0 and value <3 :
                print(f"Bill to date: ${bill_to_date:.2f}")
                current_taxi = taxis[value]

            else:
                print(f"Invalid taxi choice")
                print(f"Bill to date: ${bill_to_date:.2f}")
        elif choice == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
                print(f"Bill to date: ${bill_to_date:.2f}")
            else:
                distance = int(input("Drive how far? "))
                current_taxi.drive(distance)
                fare = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                bill_to_date += fare
                current_taxi.start_fare()
                print(f"Bill to date: ${bill_to_date:.2f}")

        else:
            print("Invalid option")
            print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>>").upper()

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == '__main__':
    main()