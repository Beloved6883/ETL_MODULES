import os
project_path = os.getenv('PROJECT_PATH')
import sys
sys.path.append(project_path) # This is necessary to be able to import a module from a different directory
import pandas as pd
from data_cleaning_classes.data_ingestion import Ingestion

path = '/Users/beloved683/Desktop/Programming/ETL_MODULES/social_security_data/names/'

file_names = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

temp_df_list = []

for file in file_names:
    file_base, file_ext = os.path.splitext(file)
    temp = Ingestion(file_path = path + file, extension = file_ext, header = 0, converters={'score':int})
    temp_df = temp.function_to_use()()
    temp_df_list.append(temp_df)
col = temp_df_list[0].columns
final_df = pd.concat([df.set_axis(col, axis=1) for df in temp_df_list], sort=False)
    
# test = Ingestion(file_path = path + file_name, extension ='.xlsx', header = 0, converters={'score':int})

# test_df = test.function_to_use()()

print(final_df.head(10))

# print(file_names)