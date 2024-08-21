
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

df = pd.read_csv('final_final_csv.csv')
df_NY = df[df['State'] == 'NY']
df_MD = df[df['State'] == 'MD']



def aggassault_vs_housing():
    # agg assault rates vs avg house price in MD and NY

    plt.figure(figsize=(8, 5))
    plt.scatter(df_MD['Average Value'], df_MD['Agg Assault Rate'], color='blue', alpha=0.7, label='Maryland')
    plt.scatter(df_NY['Average Value'], df_NY['Agg Assault Rate'], color='red', alpha=0.7, label='New York')

    plt.xlabel('Avg Value')
    plt.ylabel('Agg Assault Rate')
    plt.title('Agg Assault Rate vs. Average Value (MD and NY)')
    plt.grid(True)
    plt.legend()
    plt.show()


def correlate_mat():
    # correlation matrices 

    rate_columns = [
        'Index Total Rate', 'Violent Total Rate', 'Murder Rate', 'Rape Rate', 
        'Robbery Rate', 'Agg Assault Rate', 'Property Total Rate', 'Burglary Rate', 
        'Larceny Rate', 'MV Theft Rate', 'Average Value', 'Unemployment_rate'
    ]

    df_rate_NY = df_NY[rate_columns]
    df_rate_MD = df_MD[rate_columns]

    # correlation matrices for selected columns
    selected_corr_matrix_NY = df_rate_NY.corr()
    selected_corr_matrix_MD = df_rate_MD.corr()


    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(24, 10))

    # heatmap for New York
    sns.heatmap(selected_corr_matrix_NY, annot=True, fmt=".2f", cmap='coolwarm', cbar=True, ax=axes[0])
    axes[0].set_title('Correlation Matrix for New York')

    # heatmap for Maryland
    sns.heatmap(selected_corr_matrix_MD, annot=True, fmt=".2f", cmap='coolwarm', cbar=True, ax=axes[1])
    axes[1].set_title('Correlation Matrix for Maryland')
    plt.show()

def unemp_vs_housing():
    # unemployment rate vs housing 
    fig, ax1 = plt.subplots(figsize=(12, 8))
    years = sorted(df_MD['Year'].unique()) 

    # Plotting Unemployment Rate
    color = 'tab:red'
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Unemployment Rate', color=color)
    ax1.plot(df_MD['Year'], df_MD['Unemployment_rate'], color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax1.set_xticks(years)
    ax1.set_xlim([min(years), max(years)])  


    ax2 = ax1.twinx()  
    color = 'tab:blue'
    ax2.set_ylabel('Average Home Value ($)', color=color)  
    ax2.plot(df_MD['Year'], df_MD['Average Value'], color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title('Unemployment Rate and Average Home Value per Year (MD)')
    fig.tight_layout()
    plt.grid(True)
    plt.show()


aggassault_vs_housing()
correlate_mat()
unemp_vs_housing()