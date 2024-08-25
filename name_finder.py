import os
project_path = os.getenv('PROJECT_PATH')
import sys
sys.path.append(project_path) # This is necessary to be able to import a module from a different directory
import pandas as pd
from data_cleaning_classes.data_ingestion import Ingestion

path = '/Users/beloved683/Desktop/Programming/ETL_MODULES/social_security_data/'
file_names_sex ='names_ranked_by_sex.csv'
file_names_female_year = 'top_female_names_by_year_sex.csv'
file_names_male_year = 'top_male_names_by_year_sex.csv'

ranked_names_ing = Ingestion(file_path = path + file_names_sex, extension = '.csv', header = 0, converters = {'frequency': int})
ranked_names_df = ranked_names_ing.function_to_use()()

ranked_female_names_year_ing = Ingestion(file_path= path + file_names_female_year, extension='.csv', header = 0, converters ={'frequency': int})
ranked_female_names_year_df = ranked_female_names_year_ing.function_to_use()()
ranked_male_names_year_ing = Ingestion(file_path= path + file_names_male_year, extension='.csv', header = 0, converters ={'frequency': int})
ranked_male_names_year_df = ranked_male_names_year_ing.function_to_use()()

choose_query_type = input('Enter Y for most popular male or female name. Enter N to find most popular male or female name by year: ')

if choose_query_type == 'Y':
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

if choose_query_type == 'N':

    sex2 = input('Enter F or M to find out the top female or male name: ')
    year = int(input('Enter year of birth (YYYY): '))

    def top_female_name_year(df2, year):
        # maxrankyearF = df2[(df2['sex'] == sex2) & (df2['year']==year)]['percent_rank'].max()

        top_female_year = df2.loc[df2['year'] == year]

        return top_female_year

    def top_male_name_year(df2, year):
        # maxrankyearM = df2[(df2['sex'] == sex2) & (df2['year']==year)]['percent_rank'].max()

        top_male_year = df2.loc[df2['year'] == year]

        return top_male_year

    if sex2 == 'F':

        top_name_year = top_female_name_year(ranked_female_names_year_df, year)

    else:

        top_name_year = top_male_name_year(ranked_male_names_year_df, year)

    print(','.join(map(str,top_name_year['first_name'])))