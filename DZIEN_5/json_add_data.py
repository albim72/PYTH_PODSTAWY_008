import json
from typing import Dict, Any

def add_to_json(file_path: str, new_data: Dict[str, Any]) -> None:
    """
    Dodaje nowe dane do pliku JSON.
    
    :param file_path: ścieżka do pliku JSON
    :param new_data: słownik z danymi do dodania
    """
    try:
        # Odczyt istniejących danych
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        # Jeśli plik nie istnieje, zaczynamy od pustej listy
        data = []

    # Dodajemy nowe dane do listy
    if isinstance(data, list):
        data.append(new_data)
    else:
        raise ValueError("Plik JSON nie zawiera listy jako głównej struktury.")

    # Zapisujemy z powrotem do pliku
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# --- Przykład użycia ---
if __name__ == "__main__":
    add_to_json("dane.json", {"id": 1, "name": "Marcin"})
    add_to_json("dane.json", {"id": 2, "name": "Agnieszka"})
