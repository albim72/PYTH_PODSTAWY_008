import numpy as np
import pandas as pd

def main():
    df = pd.read_csv("movies_5000.csv")
    print("______________ podgląd danych ________________")
    print(df.head(10),"\n")

    #podstawowe statystyki
    print(f"średnia ocen filmów: {df['rating'].mean()}")
    print(f"średni budżet filmu: {df['budget_usd'].mean()}")

    #NUMPY - operacje wektorowe
    ratings = df['rating'].to_numpy()
    budgets = df['budget_usd'].to_numpy()
    revenues = df['revenue_usd'].to_numpy()
    print("\n______________ NUMPY ________________")
    print(f"np - średnia ocen: {np.mean(ratings)}")
    print(f"np - mediana ocen: {np.median(ratings)}")
    print(f"np - odchylenie standardowe ocen: {np.std(ratings)}")

    print("ROI")

if __name__ == '__main__':
    main()
