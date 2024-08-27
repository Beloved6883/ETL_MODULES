import os
import sys
import pandas as pd
import tkinter as tk
from tkinter import messagebox

# Assuming PROJECT_PATH is set
project_path = os.getenv('PROJECT_PATH')
sys.path.append(project_path)
from data_cleaning_classes.data_ingestion import Ingestion

# Data Ingestion
path = '/Users/beloved683/Desktop/Programming/ETL_MODULES/social_security_data/'
file_names_sex = 'names_ranked_by_sex.csv'
file_names_female_year = 'top_female_names_by_year_sex.csv'
file_names_male_year = 'top_male_names_by_year_sex.csv'

ranked_names_ing = Ingestion(file_path=path + file_names_sex, extension='.csv', header=0, converters={'frequency': int})
ranked_names_df = ranked_names_ing.function_to_use()()

ranked_female_names_year_ing = Ingestion(file_path=path + file_names_female_year, extension='.csv', header=0, converters={'frequency': int})
ranked_female_names_year_df = ranked_female_names_year_ing.function_to_use()()

ranked_male_names_year_ing = Ingestion(file_path=path + file_names_male_year, extension='.csv', header=0, converters={'frequency': int})
ranked_male_names_year_df = ranked_male_names_year_ing.function_to_use()()

def top_female_name(df, sex='F'):
    maxrankF = df[df['sex'] == sex]['percent_rank'].max()
    top_female = df.loc[(df['sex'] == sex) & (df['percent_rank'] == maxrankF)]
    return top_female['first_name'].values[0]

def top_male_name(df, sex='M'):
    maxrankM = df[df['sex'] == sex]['percent_rank'].max()
    top_male = df.loc[(df['sex'] == sex) & (df['percent_rank'] == maxrankM)]
    return top_male['first_name'].values[0]

def top_female_name_year(df2, year):
    top_female_year = df2.loc[df2['year'] == year]
    return top_female_year['first_name'].values[0]

def top_male_name_year(df2, year):
    top_male_year = df2.loc[df2['year'] == year]
    return top_male_year['first_name'].values[0]

def show_result(result):
    messagebox.showinfo("Top Name", f"The top name is: {result}")

def get_top_name():
    if var.get() == "Overall":
        sex = sex_var.get()
        if sex == 'F':
            result = top_female_name(ranked_names_df)
        else:
            result = top_male_name(ranked_names_df)
    elif var.get() == "By Year":
        sex = sex_var.get()
        year = int(year_entry.get())
        if sex == 'F':
            result = top_female_name_year(ranked_female_names_year_df, year)
        else:
            result = top_male_name_year(ranked_male_names_year_df, year)
    show_result(result)

# Create the main window
root = tk.Tk()
root.title("Most Popular Names Finder")

# Create and place the radio buttons for choosing the query type
var = tk.StringVar(value="Overall")
overall_radio = tk.Radiobutton(root, text="Overall", variable=var, value="Overall")
year_radio = tk.Radiobutton(root, text="By Year", variable=var, value="By Year")
overall_radio.grid(row=0, column=0, padx=10, pady=10)
year_radio.grid(row=0, column=1, padx=10, pady=10)

# Create and place the radio buttons for choosing the sex
sex_var = tk.StringVar(value="F")
female_radio = tk.Radiobutton(root, text="Female", variable=sex_var, value="F")
male_radio = tk.Radiobutton(root, text="Male", variable=sex_var, value="M")
female_radio.grid(row=1, column=0, padx=10, pady=10)
male_radio.grid(row=1, column=1, padx=10, pady=10)

# Create and place the entry box for the year
year_label = tk.Label(root, text="Enter Year:")
year_label.grid(row=2, column=0, padx=10, pady=10)
year_entry = tk.Entry(root)
year_entry.grid(row=2, column=1, padx=10, pady=10)

# Create and place the button to get the top name
submit_button = tk.Button(root, text="Get Top Name", command=get_top_name)
submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()
