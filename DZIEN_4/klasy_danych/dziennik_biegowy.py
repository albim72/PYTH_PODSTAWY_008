from dataclasses import dataclass
from typing import List

@dataclass
class RunRecord:
    date: str
    distance_km: float
    duration_min: float

class RunLog:
    def __init__(self):
        self.runs: List[RunRecord] = []

    def add_run(self, run: RunRecord):
        self.runs.append(run)

    def total_distance(self) -> float:
        return sum(r.distance_km for r in self.runs)

    @staticmethod
    def _pace_min_per_km(run: RunRecord) -> float:
        return run.duration_min / run.distance_km if run.distance_km > 0 else 0

    def export_txt(self,path: str):
        with open(path, 'w', encoding='utf-8') as f:
            for r in self.runs:
                pace = self._pace_min_per_km(r)
                line = f"{r.date} | {r.distance_km:.1f}km | {r.duration_min}min | {pace}min/km\n"
                f.write(line)
            f.write(f"SUMA: {self.total_distance():.1f}km\n")
