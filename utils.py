# Import packages
import pandas as pd
import matplotlib.pyplot as plt


# Read csv file
def read_file():
    df = pd.read_csv('data.csv')
    return df

# Ask user to write country name
def get_country(df):
    while True:
        country_name = input("Write country name: ")

        # Check if country is in data frame
        if country_name in df["Country"].values:
            break 
        else:
            print("Please write a valid country.")
    return country_name

# Sort data columns
desired_order = [
        '1970 Population', 
        '1980 Population', 
        '1990 Population', 
        '2000 Population', 
        '2010 Population', 
        '2015 Population', 
        '2020 Population', 
        '2022 Population'
    ]
def sort_df(df, country_name):
    data = df.loc[df["Country"] == country_name, desired_order]
    return data

# Crete a bar char with the data
labels = ['1970', '1980', '1990', '2000', '2010', '2015', '2020', '2022']
def plot_barchart(data, country_name):
    plt.bar(data.columns, data.values[0], width=0.6)  
    plt.rcParams['figure.figsize'] = (5, 4) 
    plt.xticks(data.columns, labels, rotation=45)
    for col, population in zip(data.columns, data.values[0]):
        plt.axhline(
            y=population, 
            color='gray', 
            linestyle='--', 
            linewidth=0.8)
        
        plt.text(
            col, 
            population, 
            f'{population:,}', 
            va='bottom', ha='right', 
            fontsize=8, color='black'
        )

    plt.text(
        0.5, 
        1.1, 
        f'País: {country_name}', 
        transform=plt.gca().transAxes, 
        ha='center', 
        va='center', 
        fontsize=20, 
        color='black'
    )

    return plt.show()