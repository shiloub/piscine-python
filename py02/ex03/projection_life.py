from matplotlib import pyplot as plt
import pandas as pd
from load_csv import load


def main():
    """Plot a scatter plot of the gross domestic product by the Life expectancy
for all country in 1900"""
    ipp = load("../datas/income_per_person_gdpper"
               "capita_ppp_inflation_adjusted.csv")
    ley = load("../datas/life_expectancy_years.csv")
    if (ipp is None or ley is None):
        exit(1)
    combined = pd.DataFrame({
        "ipp": ipp["1900"],
        "ley": ley["1900"],
    })
    plt.figure(figsize=(8, 6))
    plt.scatter(x=combined["ipp"],
                y=combined["ley"],)
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.title("1900")
    plt.xscale("log")
    plt.xticks([1000, 10000], ["1k", "10k"])
    plt.show()


if __name__ == "__main__":
    main()
