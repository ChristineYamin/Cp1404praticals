import random


def main():
    score= float(input("Enter score :"))
    determine_score(score)
    print(f"Your score {score} is {determine_score(score)}.")
    random_score=random.randint(0,100)
    print(f"Random score {random_score} is {determine_score(random_score)}.")


def determine_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score > 90:
        return "Excellent"
    else:
        return "Passable"

main()