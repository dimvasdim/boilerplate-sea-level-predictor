import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(7,5))
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
    plt.xlim(1850, 2075)
    plt.scatter(x, y, label="original data")

    # Create first line of best fit
    res = linregress(x, y)
    x = x.append(pd.Series(range(2014, 2051)), ignore_index=True)
    y = res.intercept + res.slope * x
    plt.plot(x, y, label="first fit", color="red")

    # Create second line of best fit
    x = df.loc[df["Year"] >= 2000]["Year"]
    y = df.loc[df["Year"] >= 2000]["CSIRO Adjusted Sea Level"]
    res = linregress(x, y)
    x = x.append(pd.Series(range(2014, 2051)), ignore_index=True)
    y = res.intercept + res.slope * x
    plt.plot(x, y, label="second fit", color="green")

    # Add labels and title
    plt.ylabel("Sea Level (inches)")
    plt.xlabel("Year")
    plt.title("Rise in Sea Level")
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
