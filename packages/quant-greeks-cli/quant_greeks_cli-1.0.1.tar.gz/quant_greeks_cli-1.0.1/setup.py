from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="quant-greeks-cli",
    version="1.0.1",
    description="A CLI tool to calculate Black-Scholes Greeks for options pricing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
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