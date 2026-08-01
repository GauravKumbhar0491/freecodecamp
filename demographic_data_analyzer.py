import pandas as pd


def calculate_demographic_data(print_data=True):
    people = pd.read_csv("adult.data.csv")

    race_count = people["race"].value_counts()

    average_age_men = round(
        people.loc[people["sex"] == "Male", "age"].mean(),
        1
    )

    percentage_bachelors = round(
        (people["education"] == "Bachelors").mean() * 100,
        1
    )

    advanced = ["Bachelors", "Masters", "Doctorate"]

    advanced_group = people[people["education"].isin(advanced)]
    regular_group = people[~people["education"].isin(advanced)]

    higher_education_rich = round(
        (advanced_group["salary"] == ">50K").mean() * 100,
        1
    )

    lower_education_rich = round(
        (regular_group["salary"] == ">50K").mean() * 100,
        1
    )

    min_work_hours = people["hours-per-week"].min()

    minimum_workers = people[
        people["hours-per-week"] == min_work_hours
    ]

    rich_percentage = round(
        (minimum_workers["salary"] == ">50K").mean() * 100,
        1
    )

    income_by_country = (
        people.groupby("native-country")["salary"]
        .apply(lambda x: (x == ">50K").mean() * 100)
    )

    highest_earning_country = income_by_country.idxmax()
    highest_earning_country_percentage = round(
        income_by_country.max(),
        1
    )

    india_high_income = people[
        (people["native-country"] == "India")
        & (people["salary"] == ">50K")
    ]

    top_IN_occupation = (
        india_high_income["occupation"]
        .mode()[0]
    )

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
        )
        print(
            "Country with highest percentage of rich:",
            highest_earning_country,
        )
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
