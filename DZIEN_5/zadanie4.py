#!/usr/bin/env python3
from dataclasses import dataclass
from typing import List, Optional, Dict
from collections import Counter
from statistics import fmean
import pandas as pd


@dataclass
class Movie:
    title: str
    year: int
    genre: str
    budget: int
    revenue: int
    rating: float


class MovieManager:
    def __init__(self, movies: Optional[List[Movie]] = None) -> None:
        self.movies: List[Movie] = movies or []

    def load_from_csv(self, path: str) -> int:
        """Wczytuje dane z pliku CSV (separator ,)."""
        df = pd.read_csv(path, sep=",", encoding="utf-8")
        for _, row in df.iterrows():
            self.movies.append(
                Movie(
                    title=row["title"],
                    year=int(row["year"]),
                    genre=row["genre"],
                    budget=int(row["budget"]),
                    revenue=int(row["revenue"]),
                    rating=float(row["rating"]),
                )
            )
        return len(self.movies)

    def summary(self) -> str:
        """Podsumowanie: liczba filmów, średnie wartości."""
        n = len(self.movies)
        if n == 0:
            return "Brak danych."
        avg_rating = fmean(m.rating for m in self.movies)
        avg_budget = fmean(m.budget for m in self.movies)
        avg_revenue = fmean(m.revenue for m in self.movies)
        return (
            f"Liczba filmów: {n}\n"
            f"Średnia ocena: {avg_rating:.2f}\n"
            f"Średni budżet: {avg_budget:,.0f}\n"
            f"Średni przychód: {avg_revenue:,.0f}"
        )

    def top_by_revenue(self) -> Optional[Movie]:
        return max(self.movies, key=lambda m: m.revenue, default=None)

    def top_by_rating(self) -> Optional[Movie]:
        return max(self.movies, key=lambda m: m.rating, default=None)

    def genre_counts(self) -> Dict[str, int]:
        return dict(Counter(m.genre for m in self.movies))

    def save_summary_to_txt(self, path: str) -> None:
        """Zapisuje raport (podsumowanie + analiza) do pliku txt."""
        with open(path, "w", encoding="utf-8") as f:
            f.write("=== PODSUMOWANIE FILMÓW ===\n")
            f.write(self.summary() + "\n\n")

            f.write("=== ANALIZA ===\n")
            top_rev = self.top_by_revenue()
            if top_rev:
                f.write(
                    f"Największy przychód: {top_rev.title} ({top_rev.year}, {top_rev.genre}) — {top_rev.revenue:,}\n"
                )
            top_rat = self.top_by_rating()
            if top_rat:
                f.write(
                    f"Najlepszy rating: {top_rat.title} ({top_rat.year}, {top_rat.genre}) — {top_rat.rating}\n"
                )
            f.write("\n")

            f.write("=== LICZBA FILMÓW WG GATUNKU ===\n")
            for g, c in self.genre_counts().items():
                f.write(f"{g}: {c}\n")


if __name__ == "__main__":
    mgr = MovieManager()
    mgr.load_from_csv("movies.csv")

    print("=== Podsumowanie ===")
    print(mgr.summary())

    print("\n=== Analiza ===")
    print(f"Największy przychód: {mgr.top_by_revenue()}")
    print(f"Najlepszy rating: {mgr.top_by_rating()}")
    print("Liczba filmów wg gatunku:", mgr.genre_counts())

    # zapis wyników do pliku
    mgr.save_summary_to_txt("movies_summary.txt")
    print("\nRaport zapisany do movies_summary.txt")
