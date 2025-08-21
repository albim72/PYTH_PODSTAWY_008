import numpy as np
import pandas as pd

def main():
    df = pd.read_csv("movies_5000.csv")
    print("______________ podgląd danych ________________")
    print(df.head(10),"\n")

if __name__ == '__main__':
    main()
