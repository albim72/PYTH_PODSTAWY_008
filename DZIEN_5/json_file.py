from __future__ import annotations
from pathlib import Path
from typing import Any
import json

DATA_DIR = Path("data")
FILE_PATH = DATA_DIR / "filmy.json"

def save_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def main():
    #dane przykładowe
    filmy = [
        {"title":"Nosferatu","year":2024,"genres":["horror",],"duration_min":118},
        {"title":"Incepcja","year":2010,"genres":["sci-fi","thriller"],"duration_min":148},
        {"title":"Zimna wojna","year":2018,"genres":["drama","romance"],"duration_min":89},
    ]

    save_json(FILE_PATH, filmy)
    print(f"zapisano {len(filmy)} filmy do pliku {FILE_PATH}")

    #wczytanie danych
    wczytane = load_json(FILE_PATH)
    print(f"wczytano {len(wczytane)} filmy z pliku {FILE_PATH}")

    #prosta analiza
    po_2012 = [f["title"] for f in wczytane if f.get("year",0)>2012]
    print(f"filmy po 2012: {po_2012}")
if __name__ == '__main__':
    main()
