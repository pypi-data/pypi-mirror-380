import argparse
from greeks import delta, gamma, vega, theta, rho

def main():
    parser = argparse.ArgumentParser(
        description="Black-Scholes Greeks Calculator CLI"
    )
    parser.add_argument("--option_type", choices=["call", "put"], required=True, help="Type of option: call or put")
    parser.add_argument("--S", type=float, required=True, help="Current stock price")
    parser.add_argument("--K", type=float, required=True, help="Strike price")
    parser.add_argument("--T", type=float, required=True, help="Time to expiry in years (e.g., 0.5 for 6 months)")
    parser.add_argument("--r", type=float, required=True, help="Annual risk-free interest rate (decimal, e.g., 0.01)")
    parser.add_argument("--sigma", type=float, required=True, help="Annual volatility (decimal, e.g., 0.2)")
    args = parser.parse_args()

    print(f"Delta: {delta(args.option_type, args.S, args.K, args.T, args.r, args.sigma):.5f}")
    print(f"Gamma: {gamma(args.S, args.K, args.T, args.r, args.sigma):.5f}")
    print(f"Vega:  {vega(args.S, args.K, args.T, args.r, args.sigma):.5f}")
    print(f"Theta: {theta(args.option_type, args.S, args.K, args.T, args.r, args.sigma):.5f}")
    print(f"Rho:   {rho(args.option_type, args.S, args.K, args.T, args.r, args.sigma):.5f}")

if __name__ == "__main__":
    main()