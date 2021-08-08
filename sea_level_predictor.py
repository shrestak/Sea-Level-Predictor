import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
  
    plt.clf()

    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    slope, intercept, r, p, se = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = pd.Series(range(df['Year'].min(),2051))
    y1 = intercept + slope * x1
    plt.plot(x1, y1, label = 'First Line of Best Fit', color = 'green')
    

    # Create second line of best fit
    df_recent2000 = df[df['Year'] >= 2000]
    slope, intercept, r, p, se = linregress(df_recent2000['Year'], df_recent2000['CSIRO Adjusted Sea Level'])
    x2 = pd.Series(range(2000,2051))
    y2 = intercept + slope * x2
    plt.plot(x2, y2, label = 'Second Line of Best Fit', color = 'red')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()