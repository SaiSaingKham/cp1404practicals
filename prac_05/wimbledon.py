def main():
    filename = "wimbledon.csv"
    champions, countries = read_wimbledon_data(filename)
    display_champions(champions)
    display_countries(countries)
def read_wimbledon_data(filename):
    champions = {}
    countries = set()

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for line in in_file:
            parts = line.strip().split(",")
            name = parts[1]
            country = parts[2]
            champions[name] = champions.get(name, 0) + 1
            countries.add(country)

    return champions, countries


def display_champions(champions):
    print("Wimbledon Champions:")
    for champion, wins in sorted(champions.items()):
        print(f"{champion} {wins}")


def display_countries(countries):
    print("\nThese countries have won Wimbledon:")
    countries_str = ", ".join(sorted(countries))
    print(countries_str)

if __name__ == '__main__':
    main()