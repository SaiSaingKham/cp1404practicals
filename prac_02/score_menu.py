def main():
    """A menu-driven program to manage and display score status."""
    score = get_valid_score()
    while True:
        print_menu()
        choice = input(">>>").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_score_status(score))
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

def determine_score_status(score):
    """Determine the status of the score given."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"

def show_stars(score):
    """Print as many stars as the score."""
    print("*" * int(score))

def get_valid_score():
    """Get the score and make sure it is valid."""
    while True:
        try:
            score = float(input("Enter a valid score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score. Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def print_menu():
    """Display the main menu."""
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")

if __name__ == "__main__":
    main()
