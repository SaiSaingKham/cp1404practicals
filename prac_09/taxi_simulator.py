from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi
def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
def main():
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0.0
    while True:
        print("q)uit, c)hoose taxi, d)rive")
        user_choice = input(">>> ").lower()
        if user_choice == 'q':
            print(f"Total trip cost: ${bill_to_date:.2f}")
            print("Taxis are now:")
            display_taxis(taxis)
            break
        elif user_choice == 'c':
            display_taxis(taxis)
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice]
                print(f"Bill to date: ${bill_to_date:.2f}")
            except (ValueError, IndexError):
                print("Invalid taxi choice")
        elif user_choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? "))
                    cost = current_taxi.drive(distance)
                    bill_to_date += cost
                    print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
                    print(f"Bill to date: ${bill_to_date:.2f}")
                except ValueError:
                    print("Invalid distance")
        else:
            print("Invalid option")
            print(f"Bill to date: ${bill_to_date:.2f}")
if __name__ == "__main__":
    main()