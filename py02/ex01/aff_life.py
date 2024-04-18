from matplotlib import pyplot as plt
from load_csv import load


def main():
    """Plot the life expectancy per years for France since 1800 to 2100"""
    ley = load("../datas/life_expectancy_years.csv")
    if (ley is None):
        exit(1)
    ley.set_index("country", inplace=True)
    print(ley.loc["France"])
    ley.loc["France"].plot(x="years",
                           y="Life Expectancy",
                           xlabel="Year",
                           ylabel="Life expectancy",
                           title="Life expectancy projection")
    plt.show()


if __name__ == "__main__":
    main()
