import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Read and clean the dataset
forum_data = pd.read_csv(
    "fcc-forum-pageviews.csv",
    index_col="date",
    parse_dates=True
)

low = forum_data["value"].quantile(0.025)
high = forum_data["value"].quantile(0.975)

forum_data = forum_data[
    forum_data["value"].between(low, high)
]

month_order = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]


def draw_line_plot():

    fig, ax = plt.subplots(figsize=(15, 5))

    ax.plot(
        forum_data.index,
        forum_data["value"],
        color="red",
        linewidth=1
    )

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():

    monthly_data = forum_data.copy()

    monthly_data["Year"] = monthly_data.index.year
    monthly_data["Month"] = monthly_data.index.month_name()

    summary = (
        monthly_data
        .groupby(["Year", "Month"])["value"]
        .mean()
        .reset_index()
    )

    fig, ax = plt.subplots(figsize=(15, 6))

    sns.barplot(
        data=summary,
        x="Year",
        y="value",
        hue="Month",
        hue_order=month_order,
        ax=ax
    )

    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")

    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():

    plot_data = forum_data.reset_index()

    plot_data["year"] = plot_data["date"].dt.year
    plot_data["month"] = plot_data["date"].dt.strftime("%b")
    plot_data["month_num"] = plot_data["date"].dt.month

    plot_data = plot_data.sort_values("month_num")

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    sns.boxplot(
        data=plot_data,
        x="year",
        y="value",
        ax=axes[0]
    )

    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(
        data=plot_data,
        x="month",
        y="value",
        ax=axes[1]
    )

    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.savefig("box_plot.png")
    return fig
