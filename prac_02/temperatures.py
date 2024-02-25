
# def convert_celsius_to_Fahrennheit():
#     celsius = float(input("Celsius: "))
#     fahrenheit = celsius * 9.0 / 5 + 32
#     print(f"Result: {fahrenheit:.2f} F")
#
# def convert_Fahrenheit_to_celsius():
#     fahrenheit = float(input("Fahrenheit: "))
#     celsius = 5 / 9 * (fahrenheit - 32)
#     print(f"Result : {celsius:.2f} C")
#
# convert_celsius_to_Fahrennheit()
# convert_Fahrenheit_to_celsius()


def main():
    celsius = float(input("Celsius: "))
    convert_celsius_to_Fahrennheit(celsius)
    print(f"Result :{convert_celsius_to_Fahrennheit(celsius)} F" )

    fahrenheit  = float(input("Fahrenheit: "))
    convert_Fahrenheit_to_celsius(fahrenheit)
    print(f"Result :{convert_Fahrenheit_to_celsius(fahrenheit)} C")


def convert_celsius_to_Fahrennheit(celsius):
    return  celsius * 9.0 / 5 + 32

def convert_Fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


main()

