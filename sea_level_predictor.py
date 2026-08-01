import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Load the dataset
    sea_levels = pd.read_csv("epa-sea-level.csv")

    # Create figure and axis
    figure, axis = plt.subplots(figsize=(10, 6))

    # Scatter plot
    axis.scatter(
        sea_levels["Year"],
        sea_levels["CSIRO Adjusted Sea Level"]
    )

    # Trend line using all available data
    all_fit = linregress(
        sea_levels["Year"],
        sea_levels["CSIRO Adjusted Sea Level"]
    )

    future_years = range(1880, 2051)

    axis.plot(
        future_years,
        all_fit.intercept + all_fit.slope * pd.Series(future_years),
        color="red"
    )

    # Trend line using data from 2000 onward
    recent_data = sea_levels[sea_levels["Year"] >= 2000]

    recent_fit = linregress(
        recent_data["Year"],
        recent_data["CSIRO Adjusted Sea Level"]
    )

    recent_years = range(2000, 2051)

    axis.plot(
        recent_years,
        recent_fit.intercept + recent_fit.slope * pd.Series(recent_years),
        color="green"
    )

    # Labels and title
    axis.set_xlabel("Year")
    axis.set_ylabel("Sea Level (inches)")
    axis.set_title("Rise in Sea Level")

    plt.savefig("sea_level_plot.png")
    return axis
