from setuptools import setup, find_packages

setup(
    name="quant-greeks-cli",
    version="1.0.0",
    description="A CLI tool to calculate Black-Scholes Greeks for options pricing.",
    author="Patience Fuglo",
    packages=find_packages(),
    py_modules=["greeks", "cli"],
    install_requires=[
        "scipy",
    ],
    entry_points={
        "console_scripts": [
            "quant-greeks=cli:main",
        ],
    },
    python_requires=">=3.7",
)