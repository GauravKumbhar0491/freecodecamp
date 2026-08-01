import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
medical_data = pd.read_csv("medical_examination.csv")

# BMI > 25 -> overweight
bmi = medical_data["weight"] / ((medical_data["height"] / 100) ** 2)
medical_data["overweight"] = (bmi > 25).astype(int)

# Normalize cholesterol and glucose
for feature in ["cholesterol", "gluc"]:
    medical_data[feature] = (medical_data[feature] > 1).astype(int)


def draw_cat_plot():
    plot_data = medical_data.melt(
        id_vars="cardio",
        value_vars=[
            "active",
            "alco",
            "cholesterol",
            "gluc",
            "overweight",
            "smoke",
        ],
        var_name="feature",
        value_name="status",
    )

    chart = sns.catplot(
        data=plot_data,
        x="feature",
        hue="status",
        col="cardio",
        kind="count",
        height=5,
        aspect=1
    )

    chart.set_axis_labels("", "total")

    figure = chart.fig
    figure.savefig("catplot.png")
    return figure


def draw_heat_map():
    cleaned = medical_data[
        (medical_data["ap_lo"] <= medical_data["ap_hi"])
        & medical_data["height"].between(
            medical_data["height"].quantile(0.025),
            medical_data["height"].quantile(0.975)
        )
        & medical_data["weight"].between(
            medical_data["weight"].quantile(0.025),
            medical_data["weight"].quantile(0.975)
        )
    ]

    correlation = cleaned.corr(numeric_only=True)

    upper_triangle = np.triu(np.ones_like(correlation, dtype=bool))

    figure, axis = plt.subplots(figsize=(12, 10))

    sns.heatmap(
        correlation,
        mask=upper_triangle,
        annot=True,
        fmt=".1f",
        square=True,
        ax=axis
    )

    figure.savefig("heatmap.png")
    return figure
