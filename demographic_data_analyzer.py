import pandas as pd

def demographic_data_analyzer():
    # Load the dataset
    df = pd.read_csv("adult.data.csv")

    # 1. How many of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == 'Bachelors').sum() / len(df) * 100, 1)

    # 4. Percentage with advanced education that earn >50K
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    higher_education_rich = round((higher_education['salary'] == '>50K').sum() / len(higher_education) * 100, 1)
    lower_education_rich = round((lower_education['salary'] == '>50K').sum() / len(lower_education) * 100, 1)

    # 5. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # 6. What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage_min_hours = round((min_workers['salary'] == '>50K').sum() / len(min_workers) * 100, 1)

    # 7. What country has the highest percentage of people that earn >50K?
    country_group = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()
    country_group['>50K'] = country_group['>50K'].fillna(0)
    highest_earning_country = country_group['>50K'].idxmax()
    highest_earning_country_percentage = round(country_group['>50K'].max() * 100, 1)

    # 8. Identify the most popular occupation for those who earn >50K in India.
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage_min_hours': rich_percentage_min_hours,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
