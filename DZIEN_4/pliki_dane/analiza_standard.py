import csv

def read_movie(path: str):
    movies = []
    with open(path,'r', newline='',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            #zamiana pól numerycznych na liczby
            row["year"] = int(row["year"])
            row["rating"] = float(row["rating"])
            row["budget_usd"] = float(row["budget_usd"])
            movies.append(row)
    return movies

def main():
    movies = read_movie("movies_5000.csv")

    #pierwsze 5 filmów
    print("pierwsze 5 filmów")
    for m in movies[:5]:
        print(m["title"], m["year"],m["genre"], m["rating"])
        
    

if __name__ == '__main__':
    main()
