
MENU= "(G)et a valid score \n(P)rint result\n(S)how stars\n(Q)uit"
def main():
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            user_score = get_valid_score()
            print(f"Your score is {user_score}.")

        elif choice == "P":
            determine_score(user_score)
            print(f"Your score {user_score} is {determine_score(user_score)}.")

        elif choice == "S":
            print("*" * user_score)

        else:
            print("Invalid message")
        print(MENU)
        choice = input(">>>").upper()

    print("Fare well.")


def get_valid_score():
    user_score=int(input("Score :"))
    while user_score < 0 or user_score > 100:
        print("Invalid Score")
        user_score = int(input("Score :"))
    return user_score

def determine_score(user_score):
    if user_score < 50:
        return "Bad"
    elif user_score > 90:
        return "Excellent"
    else:
        return "Passable"



main()

