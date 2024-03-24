"""
Name: Sai Saing Kham
Date started: 20/3/2024
GitHub URL (of this assignment):
Remember to NEVER make this assignment repo public
"""

import csv


def main():
    print(f"Movies2See 1.0 - by Sai Saing Kham")
    file_name = "movie.csv"
    movies = load_movies(file_name)
    num_movies = len(movies)
    print(f"{num_movies} movies loaded\n")

    while True:
        print("Menu")
        print("D - Display movies")
        print("A - Add new movie")
        print("W - Watch a movie")
        print("Q - Quit")
        choice = input("~ ").upper()

        if choice == "D":
            display_movies(movies)
        elif choice == "A":
            add_movie(movies)
        elif choice == "W":
            watch_movie(movies)
        elif choice == "Q":
            save_movies(file_name, movies)
            print(f"{len(movies)} movies saved to {file_name}")
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice")


def display_movies(movies):
        print("Title".ljust(30), "Category".ljust(15), "Year".ljust(5), "Status")
        print("-" * 55)
        watched_count = 0
        unwatched_count = 0
        for idx, movie in enumerate(movies):
            title, year, category, status = movie
            watch_status = "*" if status == "u" else " "
            print(f"{watch_status} {idx}. {title.ljust(30)} {category.ljust(15)} {year.ljust(5)} ({status})")
            if status == "w":
                watched_count += 1
            else:
                unwatched_count += 1
        print(f"\n{watched_count} movies watched, {unwatched_count} movies still to watch")


def add_movie(movies):
        title = input("Title: ").strip()
        while not title:
            print("Input can not be blank")
            title = input("Title: ").strip()
        while True:
            try:
                year = int(input("Year: "))
                if year < 0:
                    print("Number must be >= 0")
                else:
                    break
            except ValueError:
                print("Invalid input; enter a valid number")
        category = input("Category: ").strip()
        while not category:
            print("Input can not be blank")
            category = input("Category: ").strip()
        movies.append([title, str(year), category, "u"])
        print(f"{title} ({category} from {year}) added to movie list")


def watch_movie(movies):
        unwatched_movies = [idx for idx, movie in enumerate(movies) if movie[3] == "u"]
        if not unwatched_movies:
            print("No more movies to watch!")
            return
        while True:
            try:
                idx = int(input("Enter the number of a movie to mark as watched ~ "))
                if idx < 0 or idx >= len(movies):
                    print("Invalid movie number")
                elif movies[idx][3] == "w":
                    print(f"You have already watched {movies[idx][0]}")
                else:
                    break
            except ValueError:
                print("Invalid input; enter a valid number")
        movies[idx][3] = "w"
        print(f"{movies[idx][0]} from {movies[idx][1]} watched")


def load_movies(file_name):
        try:
            with open(file_name, "r") as file:
                movies = [line.strip().split(",") for line in file.readlines()]
            return movies
        except FileNotFoundError:
            return []


def save_movies(file_name, movies):
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(movies)

if __name__ == "__main__":
        main()