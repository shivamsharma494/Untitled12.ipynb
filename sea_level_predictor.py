import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import data
df = pd.read_csv('epa-sea-level.csv')

# Create scatter plot
def draw_plot():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data')

    # Create first line of best fit (1880 to 2050)
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred1 = pd.Series(range(1880, 2051))
    y_pred1 = res1.intercept + res1.slope * x_pred1
    ax.plot(x_pred1, y_pred1, 'r', label='Best Fit Line (1880-2050)')

    # Create second line of best fit (2000 to 2050)
    df_recent = df[df['Year'] >= 2000]
    res2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred2 = pd.Series(range(2000, 2051))
    y_pred2 = res2.intercept + res2.slope * x_pred2
    ax.plot(x_pred2, y_pred2, 'green', label='Best Fit Line (2000-2050)')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.legend()

    # Save and return plot
    plt.tight_layout()
    fig.savefig('sea_level_plot.png')
    return fig
