# MontyCarlo

A Monte Carlo simulator for the Monty Hall Problem

A.K.A.
> _"Two goats, one car"_

This project simulates the classic **Monty Hall** problem and estimates the empirical win rates for **staying** vs **switching**. It adheres to the standard rules, and prints clean JSON for easy piping to other tools.


## Rules

1. The prize is hidden uniformly at random behind one of three doors.
2. The contestant picks one door uniformly at random.
3. The host opens one of the other two doors, and reveals a goat. The host always knows where the prize is, and never opens the contestant’s chosen door or the prize door.
4. The contestant may **stay** with the original door or **switch** to the remaining closed door.

The MontyCarlo simulator runs a large number of independent trials conforming to these rules and reports the observed win rates for both strategies.

## Requirements

- Python >=3.10

## Installation

```bash
git clone https://github.com/DJStompZone/MontyCarlo.git
cd MontyCarlo
pip install .
```

Or install directly with pip:

```bash
pip install two-goats-one-car
```

## Project Layout

```plaintext
MontyCarlo/
├── LICENSE
├── pyproject.toml
├── README.md
└── two_goats_one_car/
    ├── __init__.py
    ├── __main__.py     # CLI entrypoint (python -m montycarlo)
    ├── monty.py        # Monty class & simulation logic
    └── results.py      # Dataclasses for trial results
```

## Usage

### Arguments

- `-n, --trials` — Number of trials to run (default: `100000`).
- `-s, --seed` — PRNG seed for reproducibility (default: none).
  
### Reproducibility

- Set `--seed` to fix the RNG stream.
- Larger `-n` reduces sampling noise
- Expect absolute error to shrink roughly with $(O(1/\sqrt{n}))$.

### Example

```bash
# Run 1,000,000 trials with a fixed seed:
montycarlo -n 1000000 -s 69420
```

### Example Output

```jsonc
{
  // Number of trials run
  "trials": 1000000,

  // Empirical probability of winning by staying
  "stay_win_rate": 0.333021,

  // Empirical probability of winning by switching
  "switch_win_rate": 0.666979,

  // Difference between switch and stay win rates
  "delta": 0.333958
}
```

## License

MIT. See the [LICENSE](LICENSE) file for details.

## Disclaimer

Don't come crying to me if you try this on a real game show and still pick the goat. :D
