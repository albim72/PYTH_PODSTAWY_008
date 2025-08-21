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
    print("___________________________________________")
    print("ROI(Return on Investment) = revenue/budget")
    roi = np.divide(revenues,budgets,out=np.zeros_like(revenues,dtype=float),where=budgets>0)
    df['ROI'] = roi
    #top 10 filmów wg ROI
    top10 = df.sort_values(by='ROI',ascending=False)[:10]
    print("\n______________ NUMPY ________________")
    print(top10[['title','year','revenue_usd','budget_usd','ROI']])

    #Grupowanie
    genre_groups = df.groupby('genre')["rating"].apply(lambda x: np.mean(x.to_numpy()))
    print("\n______________ średnia ocena wg gatunku ________________")
    print(genre_groups)

if __name__ == '__main__':
    main()
