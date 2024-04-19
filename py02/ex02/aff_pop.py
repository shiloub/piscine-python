from matplotlib import pyplot as plt
from load_csv import load
import numpy as np



def main():
    """Plot the population expectancy per years for France since 1800 to 2100"""
    pop = load("../datas/population_total.csv")
    if (pop is None):
        exit(1)
    pop.set_index("country", inplace=True)
    pop.columns = [int(year) for year in pop.columns]
    pop = pop.map(lambda x: int(float(x[:-1]) * 1000000) if x.endswith("M") else int(float(x[:-1]) * 1000))
    print(pop.loc["France"])
    plt.figure(figsize=(8,6))
    plt.plot(pop.columns[:-50], pop.loc["France"][:-50], label="France", color="green")
    plt.plot(pop.columns[:-50], pop.loc["Belgium"][:-50], label="Belgium", color='blue')
    plt.yticks([20000000, 40000000, 60000000], ["20M", "40M", "60M"])
    plt.xticks([1800, 1840, 1880, 1920, 1960, 2000, 2040])
    plt.xlim((1780, 2100))
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("Population Projections")   
    plt.legend(loc='lower right')
    plt.show()



if __name__ == "__main__":
    main()
