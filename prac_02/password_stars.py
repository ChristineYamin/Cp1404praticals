def main():
    minium_length = 5
    password = get_password(minium_length)
    print_stars(password)


def get_password(minium_length):
    password = input("Password :")
    while len(password) < minium_length:
        print(f"Password should be {minium_length} characters.")
        password = input("Password :")
    return password


def print_stars(password):
    print("*" * len(password))


main()


