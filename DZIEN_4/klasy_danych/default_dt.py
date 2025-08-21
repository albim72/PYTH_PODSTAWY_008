from dataclasses import dataclass, field


@dataclass
class Runner:
    name: str
    distance: float = 0.0
    trainings: list[float] = field(default_factory=list)

    def add_training(self,km: float) -> None:
        self.trainings.append(km)
        self.distance += km

r = Runner("Marek")
print(r)
r.add_training(10)
r.add_training(20)
r.add_training(30)
print(r.distance)
print(r.trainings)

print(r)
