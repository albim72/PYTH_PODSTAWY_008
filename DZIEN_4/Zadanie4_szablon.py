from dataclasses import dataclass
from typing import List
import csv

@dataclass
class Movie:
    title: str
    year: int
    genre: str
    budget: int
    revenue: int
    rating: float

class MovieManager:
    def __init__(self) -> None:
        self.movies: List[Movie] = []

    def add_movie(self, movie: Movie) -> None:
        ...

    def save_to_csv(self, path: str) -> None:
        ...

    def load_from_csv(self, path: str) -> None:
        ...

    def summary(self) -> None:
        ...

def main():
    manager = MovieManager()
    # Dodaj przykładowe filmy ręcznie
    manager.add_movie(Movie("Inception", 2010, "Sci-Fi", 160_000_000, 829_000_000, 8.8))
    manager.add_movie(Movie("Titanic", 1997, "Drama", 200_000_000, 2_195_000_000, 7.8))
    manager.add_movie(Movie("The Godfather", 1972, "Crime", 6_000_000, 250_000_000, 9.2))

    # Zapisz do CSV
    manager.save_to_csv("movies.csv")

    # Wczytaj ponownie z pliku
    manager2 = MovieManager()
    manager2.load_from_csv("movies.csv")
    manager2.summary()

    # Analiza
    # TODO: największy przychód, najlepszy rating, liczba filmów wg gatunku

if __name__ == "__main__":
    main()
