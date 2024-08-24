import os
project_path = os.getenv('PROJECT_PATH')
import sys
sys.path.append(project_path) # This is necessary to be able to import a module from a different directory
import pandas as pd
from data_cleaning_classes.data_ingestion import Ingestion

path = '/Users/beloved683/Desktop/Programming/ETL_MODULES/social_security_data/'
file ='names_ranked_by_sex.csv'
ranked_names_ing = Ingestion(file_path = path + file, extension = '.csv', header = 0, converters = {'frequency': int})
ranked_names_df = ranked_names_ing.function_to_use()()

sex = input('Enter F or M to find out the top female or male name: ')

def top_female_name(df, sex = 'F'):
    maxrankF = df[df['sex'] == sex]['percent_rank'].max()

    top_female = df.loc[(df['sex'] == sex) & (df['percent_rank'] == maxrankF)]

    return top_female

def top_male_name(df, sex = 'M'):
    maxrankM = df[df['sex'] == sex]['percent_rank'].max()

    top_male = df.loc[(df['sex'] == sex) & (df['percent_rank'] == maxrankM)]

    return top_male

if sex == 'F':

    top_name = top_female_name(ranked_names_df, sex)

else:

    top_name = top_male_name(ranked_names_df, sex)

print(','.join(map(str,top_name['first_name'].values)))
