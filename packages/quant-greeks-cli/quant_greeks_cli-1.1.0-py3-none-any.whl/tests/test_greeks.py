import math
from greeks import delta, gamma, vega, theta, rho

params_call = {
    "option_type": "call",
    "S": 100,
    "K": 100,
    "T": 1,
    "r": 0.05,
    "sigma": 0.2,
}

params_put = {
    "option_type": "put",
    "S": 100,
    "K": 100,
    "T": 1,
    "r": 0.05,
    "sigma": 0.2,
}

def test_delta_call():
    result = delta(**params_call)
    assert math.isclose(result, 0.63683, rel_tol=1e-4, abs_tol=1e-6)

def test_delta_put():
    result = delta(**params_put)
    assert math.isclose(result, -0.36317, rel_tol=1e-4, abs_tol=1e-6)

def test_gamma():
    result = gamma(params_call["S"], params_call["K"], params_call["T"], params_call["r"], params_call["sigma"])
    assert math.isclose(result, 0.018762017345846895, rel_tol=1e-4, abs_tol=1e-6)

def test_vega():
    result = vega(params_call["S"], params_call["K"], params_call["T"], params_call["r"], params_call["sigma"])
    assert math.isclose(result, 0.37524, rel_tol=1e-4, abs_tol=1e-6)

def test_theta_call():
    result = theta(**params_call)
    assert math.isclose(result, -0.01757267820941972, rel_tol=1e-4, abs_tol=1e-6)

def test_theta_put():
    result = theta(**params_put)
    assert math.isclose(result, -0.004542138147766099, rel_tol=1e-4, abs_tol=1e-6)

def test_rho_call():
    result = rho(**params_call)
    assert math.isclose(result, 0.53232, rel_tol=1e-4, abs_tol=1e-6)

def test_rho_put():
    result = rho(**params_put)
    assert math.isclose(result, -0.41890, rel_tol=1e-4, abs_tol=1e-6)