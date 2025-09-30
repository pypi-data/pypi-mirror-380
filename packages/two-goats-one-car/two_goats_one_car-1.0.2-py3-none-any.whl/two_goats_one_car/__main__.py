#!/usr/bin/env python3
"""
Monty Hall Problem Simulator

Rules:
    - Prize is behind one of three doors, the other two doors are goats.
    - Contestant picks one door at random.
    - Host opens one of the doors the player didn't choose, revealing a goat.
    - Player is offered the choice to switch doors or keep their original choice.

Notes:
    One might assume that swapping or staying would not influence the chances of winning,
    as each door initially has a 33.33% chance of being the winning door. This tool aims to
    test this hypothesis experimentally and objectively.

Author: DJ Stomp <85457381+DJStompZone@users.noreply.github.com>
License: MIT
"""
from __future__ import annotations
import json
import random
import argparse

from two_goats_one_car.monty import Monty


def simulate(trials: int, seed: int | None = None) -> dict[str, float]:
    """
    Run `trials` independent games and return empirical probabilities for staying vs switching.
    """
    if seed is not None:
        random.seed(seed)
    stay_wins = 0
    switch_wins = 0
    for _ in range(trials):
        game = Monty()
        if game.results is None:
            raise RuntimeError("Analysis not performed.")
        stay_wins += 1 if game.results.stay else 0
        switch_wins += 1 if game.results.switch else 0
    return {"stay_win_rate": stay_wins / trials, "switch_win_rate": switch_wins / trials}

def main() -> None:
    """
    CLI runner to estimate Monty Hall win rates.
    Example:
      python monty.py -n 1000000
      python monty.py -n 1000000 -s 1337
    """
    parser = argparse.ArgumentParser(description="Monte Carlo simulation of the Monty Hall problem (yes, switching still kicks ass).")
    parser.add_argument("-n", "--trials", type=int, default=100000, help="Number of trials to run (default: 100000).")
    parser.add_argument("-s", "--seed", type=int, default=None, help="PRNG seed for reproducibility (default: none).")
    args: argparse.Namespace = parser.parse_args()

    results: dict[str, float] = simulate(trials=args.trials, seed=args.seed)
    stay: float = results["stay_win_rate"]
    switch: float = results["switch_win_rate"]
    print(json.dumps({"trials": args.trials, "stay_win_rate": stay, "switch_win_rate": switch, "delta": switch - stay}, indent=2))

if __name__ == "__main__":
    main()
