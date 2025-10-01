import argparse
from greeks import delta, gamma, vega, theta, rho
from binomial import binomial_option_price

def main():
    parser = argparse.ArgumentParser(
        description="Options Greeks and Pricing CLI"
    )
    parser.add_argument("--option_type", choices=["call", "put"], required=True, help="Type of option: call or put")
    parser.add_argument("--S", type=float, required=True, help="Current stock price")
    parser.add_argument("--K", type=float, required=True, help="Strike price")
    parser.add_argument("--T", type=float, required=True, help="Time to expiry in years (e.g., 0.5 for 6 months)")
    parser.add_argument("--r", type=float, required=True, help="Annual risk-free interest rate (decimal, e.g., 0.01)")
    parser.add_argument("--sigma", type=float, required=True, help="Annual volatility (decimal, e.g., 0.2)")
    parser.add_argument(
        "--model",
        type=str,
        choices=["black-scholes", "binomial"],
        default="black-scholes",
        help="Option pricing model to use (default: black-scholes)"
    )
    parser.add_argument(
        "--steps",
        type=int,
        default=100,
        help="Number of steps for the binomial model (default: 100; ignored for Black-Scholes)"
    )
    args = parser.parse_args()

    if args.model == "black-scholes":
        print(f"Delta: {delta(args.option_type, args.S, args.K, args.T, args.r, args.sigma):.5f}")
        print(f"Gamma: {gamma(args.S, args.K, args.T, args.r, args.sigma):.5f}")
        print(f"Vega:  {vega(args.S, args.K, args.T, args.r, args.sigma):.5f}")
        print(f"Theta: {theta(args.option_type, args.S, args.K, args.T, args.r, args.sigma):.5f}")
        print(f"Rho:   {rho(args.option_type, args.S, args.K, args.T, args.r, args.sigma):.5f}")
    elif args.model == "binomial":
        price = binomial_option_price(
            args.option_type, args.S, args.K, args.T, args.r, args.sigma, args.steps
        )
        print(f"Binomial {args.option_type} option price: {price:.5f}")
    else:
        print("Invalid model selected!")

if __name__ == "__main__":
    main()