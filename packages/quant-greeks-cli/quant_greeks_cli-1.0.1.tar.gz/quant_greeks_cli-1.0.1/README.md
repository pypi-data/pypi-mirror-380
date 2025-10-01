![CI](https://github.com/Patience-Fuglo/quant-greeks-cli/actions/workflows/ci.yml/badge.svg)


# Quant Greeks CLI Tool

## Project Description

The Quant Greeks CLI Tool is a lightweight command-line application for calculating the five main Black-Scholes Greeks (Delta, Gamma, Vega, Theta, Rho) for options pricing. Designed for traders, quants, and finance students, this tool helps you analyze options risk and sensitivity from the terminal.

---

## Features

- **Black-Scholes Greeks Calculator:** Computes Delta, Gamma, Vega, Theta, and Rho.
- **Simple CLI:** Run calculations directly from your terminal with easy arguments.
- **100% Test Coverage:** Every calculation is unit tested for accuracy.
- **CI/CD:** Integrated with GitHub Actions for continuous testing and reliability.

---

## Usage

After installation, use the `quant-greeks` command globally from your terminal:

```bash
quant-greeks --option_type call --S 100 --K 100 --T 1 --r 0.05 --sigma 0.2
```

Where:
- `--option_type` is "call" or "put"
- `--S` is the current stock price
- `--K` is the strike price
- `--T` is time to maturity (in years)
- `--r` is the annual risk-free rate (decimal)
- `--sigma` is volatility (decimal)

For help, run:
```bash
quant-greeks --help
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Patience-Fuglo/quant-greeks-cli.git
   cd quant-greeks-cli
   ```

2. **Set up a Python environment (optional but recommended):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install quant-greeks-cli:**
```bash
pip install quant-greeks-cli


You can install the Quant Greeks CLI tool directly from [PyPI](https://pypi.org/project/quant-greeks-cli/):


## Usage

Calculate option Greeks from the CLI:

```bash
python cli.py --option_type call --S 100 --K 100 --T 1 --r 0.05 --sigma 0.2

```
Where:
- `--option_type` is "call" or "put"
- `--S` is the current stock price
- `--K` is the strike price
- `--T` is time to maturity (in years)
- `--r` is the annual risk-free rate (decimal)
- `--sigma` is volatility (standard deviation, decimal)

---

## Example

```bash
python cli.py --option_type put --S 95 --K 100 --T 0.5 --r 0.01 --sigma 0.15
```

---

## Testing

Run all tests with:
```bash
pytest
```
(Requires pytest, included in `requirements.txt`.)

---

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