from guitar import Guitar

def main():
    guitars = load_guitars()
    print("Guitars loaded:")
    for guitar in guitars:
        print(guitar)

    print("\nSorting guitars by year (oldest to newest)...")
    guitars.sort(key=lambda x: x.year)  # Sort guitars by year
    for guitar in guitars:
        print(guitar)

    new_guitars = get_new_guitars()
    guitars.extend(new_guitars)

    print("\nAll guitars (including new ones):")
    for guitar in guitars:
        print(guitar)

    save_guitars(guitars)
    print("Guitars saved to guitars.csv")

def load_guitars():
    guitars = []
    try:
        with open("guitars.csv", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                name = parts[0]
                year = int(parts[1])
                cost = float(parts[2])
                guitar = Guitar(name, year, cost)
                guitars.append(guitar)
    except FileNotFoundError:
        print("No existing guitars found.")
    return guitars

def get_new_guitars():
    new_guitars = []
    print("Enter new guitars (blank name to finish):")
    while True:
        name = input("Name: ").strip()
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        new_guitars.append(guitar)
    return new_guitars

def save_guitars(guitars):
    with open("guitars.csv", "w") as file:
        for guitar in guitars:
            line = f"{guitar.name},{guitar.year},{guitar.cost}"
            file.write(line + "\n")

if __name__ == "__main__":
 main()