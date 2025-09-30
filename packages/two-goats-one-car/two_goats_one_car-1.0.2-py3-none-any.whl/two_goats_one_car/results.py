from dataclasses import dataclass

@dataclass(frozen=True)
class MontyResults:
    """
    Container for a single Monty Hall trial outcome.
    stay: True if staying with the initial pick wins the prize.
    switch: True if switching to the only other closed door wins the prize.
    prize_door: Index of the prize door [0-2].
    opened_door: Door opened by host, always a goat and can't be the player's pick.
    switch_to: The door the contestant has the choice of swapping to.
    """
    stay: bool
    switch: bool
    prize_door: int
    opened_door: int
    switch_to: int
