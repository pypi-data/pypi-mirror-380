import math
from scipy.stats import norm

def d1(S, K, T, r, sigma):
    return (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))

def d2(S, K, T, r, sigma):
    return d1(S, K, T, r, sigma) - sigma * math.sqrt(T)

def delta(option_type, S, K, T, r, sigma):
    d_1 = d1(S, K, T, r, sigma)
    if option_type == "call":
        return norm.cdf(d_1)
    else:
        return norm.cdf(d_1) - 1

def gamma(S, K, T, r, sigma):
    d_1 = d1(S, K, T, r, sigma)
    return norm.pdf(d_1) / (S * sigma * math.sqrt(T))

def vega(S, K, T, r, sigma):
    d_1 = d1(S, K, T, r, sigma)
    return S * norm.pdf(d_1) * math.sqrt(T) / 100

def theta(option_type, S, K, T, r, sigma):
    d_1 = d1(S, K, T, r, sigma)
    d_2 = d2(S, K, T, r, sigma)
    first = -S * norm.pdf(d_1) * sigma / (2 * math.sqrt(T))
    if option_type == "call":
        second = r * K * math.exp(-r * T) * norm.cdf(d_2)
        return (first - second) / 365
    else:
        second = r * K * math.exp(-r * T) * norm.cdf(-d_2)
        return (first + second) / 365

def rho(option_type, S, K, T, r, sigma):
    d_2 = d2(S, K, T, r, sigma)
    if option_type == "call":
        return K * T * math.exp(-r * T) * norm.cdf(d_2) / 100
    else:
        return -K * T * math.exp(-r * T) * norm.cdf(-d_2) / 100