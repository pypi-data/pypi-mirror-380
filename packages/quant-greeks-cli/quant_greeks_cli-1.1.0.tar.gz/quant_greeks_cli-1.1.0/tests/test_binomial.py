from binomial import binomial_option_price

def test_binomial_call_price():
    price = binomial_option_price("call", 100, 100, 1, 0.05, 0.2, 100)
    assert abs(price - 10.45) < 0.2  # Acceptable tolerance

def test_binomial_put_price():
    price = binomial_option_price("put", 100, 100, 1, 0.05, 0.2, 100)
    assert abs(price - 5.57) < 0.2  # Acceptable tolerance