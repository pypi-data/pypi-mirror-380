# Quant Greeks CLI Tool

![CI](https://github.com/Patience-Fuglo/quant-greeks-cli/actions/workflows/ci.yml/badge.svg)

A lightweight command-line tool for calculating the five main Black-Scholes Greeks (Delta, Gamma, Vega, Theta, Rho). Designed for traders, quants, and finance students, this tool helps you analyze options risk and sensitivity directly from your terminal.

---

## Features

- **Black-Scholes Greeks Calculator:** Computes Delta, Gamma, Vega, Theta, and Rho
- **Simple CLI:** Run calculations from your terminal with intuitive arguments
- **100% Test Coverage:** Every calculation is unit tested for accuracy
- **CI/CD:** Integrated with GitHub Actions for continuous testing and reliability

---

## Installation

Install directly from PyPI:

```bash
pip install quant-greeks-cli
```

Or clone the repository:

```bash
git clone https://github.com/Patience-Fuglo/quant-greeks-cli.git
cd quant-greeks-cli
python3 -m venv .venv       # optional but recommended
source .venv/bin/activate
pip install -r requirements.txt
pip install .
```

---

## Usage

Calculate option Greeks from the CLI:

```bash
quant-greeks --option_type call --S 100 --K 100 --T 1 --r 0.05 --sigma 0.2
```

Where:

- `--option_type` is `"call"` or `"put"`
- `--S` is the current stock price
- `--K` is the strike price
- `--T` is time to maturity (in years)
- `--r` is the annual risk-free rate (decimal)
- `--sigma` is volatility (decimal)

For help:
```bash
quant-greeks --help
```

### Example

```bash
quant-greeks --option_type put --S 95 --K 100 --T 0.5 --r 0.01 --sigma 0.15
```

---

## Testing

Run all tests with:

```bash
pytest
```
(Requires pytest, included in `requirements.txt`.)

---
## Binomial Option Pricing Model (New Feature!)

This CLI now supports option pricing using both the Black-Scholes and Binomial models.

### Usage Examples

**Black-Scholes (default):**
```bash
python cli.py --option_type call --S 100 --K 100 --T 1 --r 0.05 --sigma 0.2
```

**Binomial model (with steps):**
```bash
python cli.py --model binomial --option_type call --S 100 --K 100 --T 1 --r 0.05 --sigma 0.2 --steps 100
```

- `--model`: Choose `binomial` or `black-scholes` (default is `black-scholes`)
- `--steps`: Number of steps for the binomial tree (only used for binomial model; default = 100)

### What’s New

- Add binomial model for European option pricing
- New CLI arguments: `--model` and `--steps`
- All previous Black-Scholes functionality remains unchanged

## Contributing

1. Fork the repo and create your feature branch:
    ```bash
    git checkout -b feature/YourFeature
    ```
2. Commit your changes and push:
    ```bash
    git commit -m "Describe your feature"
    git push origin feature/YourFeature
    ```
3. Open a Pull Request.

---

## License

MIT License

---

## Author

Patience Fuglo