import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', sep=',' )  

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    fig, ax = plt.subplots(figsize=(12, 7))
    plt.scatter(x, y)

    # Create first line of best fit
    first_fitted_line = linregress(x, y)
    start_year = 1880
    end_year = 2050
    x_fitted_data = pd.Series([i for i in range(start_year, end_year+1)])
    y_fitted_data = first_fitted_line.slope * x_fitted_data + first_fitted_line.intercept
    plt.plot(x_fitted_data, y_fitted_data, ':r')

    # Create second line of best fit
    start_year = 2000
    end_year = 2050
    second_df = df.loc[df['Year'] >= start_year]
    x2 = second_df['Year']
    y2 = second_df['CSIRO Adjusted Sea Level']
    second_fitted_line = linregress(x2, y2)
    x2_fitted_data = pd.Series([i for i in range(start_year, end_year+1)])
    y2_fitted_data = second_fitted_line.slope * x2_fitted_data + second_fitted_line.intercept
    plt.plot(x2_fitted_data, y2_fitted_data, ':g')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
