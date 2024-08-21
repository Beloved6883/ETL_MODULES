# Write a class for ingesting data from different types of files

import pandas as pd

class Ingestion():
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
            
    def read_csv(self):
        csv_kwargs = {key: getattr(self, key) for key in self.__dict__ if key !='file_path' and key != 'extension'}
        df = pd.read_csv(self.file_path, **csv_kwargs)
        return df
        
    def read_excel(self):
        excel_kwargs = {key: getattr(self, key) for key in self.__dict__ if key !='file_path' and key != 'extension'}
        df = pd.read_excel(self.file_path, **excel_kwargs)
        return df
        # print("This is running read_excel.")

    def read_json(self):
        json_kwargs = {key: getattr(self, key) for key in self.__dict__ if key !='file_path' and key != 'extension'}
        df = pd.read_json(self.file_path, **json_kwargs)
        return df
        # print("This is running read_json.")

    def read_parquet(self):
        parquet_kwargs = {key: getattr(self, key) for key in self.__dict__ if key !='file_path' and key != 'extension'}
        df = pd.read_parquet(self.file_path, **parquet_kwargs)
        return df
        # print("This is running read_parquet.")

    def read_text(self):
        # TODO: Check this!
        text_kwargs = {key: getattr(self, key) for key in self.__dict__ if key !='file_path' and key != 'extension'}
        df = pd.read_csv(self.file_path, **text_kwargs)
        return df
        # print("This is running read_text.")

    def read_sql(self):
        sql_kwargs = {key: getattr(self, key) for key in self.__dict__ if key !='file_path' and key != 'extension'}
        df = pd.read_sql(self.file_path, **sql_kwargs)
        return df
        # print("This is running read_sql.")

    def open_zip(self):
        # TODO: Need to use a context manager
        print("This is running open_zip.")

    def function_to_use(self):
        ext_dict = {'.csv': self.read_csv,
                '.xlsx' : self.read_excel,
                '.json': self.read_json,
                '.parquet': self.read_parquet,
                '.txt': self.read_text,
                '.sql': self.read_sql,
                '.zip': self.open_zip}

        return ext_dict[self.extension]

# path = '/Users/beloved683/Desktop/Programming/ETL_MODULES/social_security_data/names/'

# file_names = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

# temp_df_list = []

# for file in file_names:
#     file_base, file_ext = os.path.splitext(file)
#     temp = Ingestion(file_path = path + file, extension = file_ext, header = 0, converters={'score':int})
#     temp_df = temp.function_to_use()()
#     temp_df_list.append(temp_df)
# col = temp_df_list[0].columns
# final_df = pd.concat([df.set_axis(col, axis=1) for df in temp_df_list], sort=False)
    
# # test = Ingestion(file_path = path + file_name, extension ='.xlsx', header = 0, converters={'score':int})

# # test_df = test.function_to_use()()

# print(final_df.shape)

# # print(file_names)
