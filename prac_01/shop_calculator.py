def get_number_of_items():
    number_items = int(input("Number of items: "))
    while number_items < 0:
        print("Invalid number of items!")
        number_items = int(input("Number of items: "))
    return number_items

def main():
    total_price = 0
    number_items = get_number_of_items()

    for i in range(number_items):
        price = float(input(f"Price of item: "))
        total_price += price

    if total_price > 100:
        total_price *= 0.9

    print(f"Total price for {number_items} items is ${total_price:.2f}")

if __name__ == "__main__":
    main()
