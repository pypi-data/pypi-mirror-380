from __future__ import annotations
from dataclasses import asdict
import json
import random
from typing import Any

from two_goats_one_car.results import MontyResults


class Monty:
    """
    Simulate a single Monty Hall game
    """

    def __init__(
        self,
        picked: int | None = None,
        doors: list[bool] | None = None,
        results: MontyResults | None = None,
    ):
        self.doors: list[bool] = doors if doors is not None else self.get_doors()
        self.picked: int = picked if picked is not None else random.randint(0, 2)
        self.results: MontyResults | None = results
        if self.results is None:
            self.analyze()
        super().__init__()

    def __str__(self) -> str:
        return f"doors={self.doors}, picked={self.picked}, results={self.results}"

    def __repr__(self) -> str:
        return (
            f"Monty(doors={self.doors}, picked={self.picked}, results={self.results})"
        )

    @staticmethod
    def get_doors() -> list[bool]:
        """
        Return a 3-element list of booleans where exactly one index is True (the prize) and the others are False (goats).
        """
        prize = random.randint(0, 2)
        return [i == prize for i in range(3)]

    def analyze(self) -> None:
        """
        Compute host behavior and outcomes for stay vs switch.
        Host logic: choose randomly among doors that are not the player's pick and not the prize door.
        When the player picked a goat, the host has exactly one option; when the player picked the prize, the host has two options.
        """
        prize_door = self.doors.index(True)
        host_options = [d for d in range(3) if d != self.picked and d != prize_door]
        opened_door = random.choice(host_options)
        switch_to = next(d for d in range(3) if d not in (self.picked, opened_door))
        self.results = MontyResults(
            stay=(prize_door == self.picked),
            switch=(prize_door == switch_to),
            prize_door=prize_door,
            opened_door=opened_door,
            switch_to=switch_to,
        )

    def to_json(self) -> str:
        """
        Serialize the game to a JSON string.
        """
        payload: dict[str, list[bool] | int | dict[str, bool | int] | None] = {
            "doors": self.doors,
            "picked": self.picked,
            "results": asdict(self.results) if self.results is not None else None,
        }
        return json.dumps(payload)

    @classmethod
    def from_json(
        cls, json_dict: dict[str, list[bool] | int | dict[str, bool | int]] | None = None, json_str: str | None = None
    ) -> "Monty":
        """
        Deserialize a game from a dict or JSON string.
        Exactly one of json_dict or json_str must be provided.
        """
        if (json_dict is None) == (json_str is None):
            raise ValueError(
                "from_json requires exactly one of the following arguments: json_dict, json_str"
            )

        data: dict[str, Any] = json.loads(json_str) if json_str is not None else json_dict  # type: ignore[assignment]
        if not isinstance(data, dict):
            raise TypeError("Decoded JSON must be a dict.")

        doors: list[bool] | None = data.get("doors")
        picked: int | None = data.get("picked")
        res: dict[str, bool | int] | None = data.get("results")

        results = None
        if res is not None:
            results = MontyResults(
                stay=bool(res["stay"]),
                switch=bool(res["switch"]),
                prize_door=int(res["prize_door"]),
                opened_door=int(res["opened_door"]),
                switch_to=int(res["switch_to"]),
            )
        return cls(
            picked=int(picked) if picked is not None else None,
            doors=list(map(bool, doors)) if doors is not None else None,
            results=results,
        )
