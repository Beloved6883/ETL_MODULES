ETL_MODULES is a repository for modules containing classes for my extract, transform, and load (ETL) process. The goal is to create modules that can be used for a variety of ETL jobs.

Creator: Natasha P. Wilson, PhD

ETL_Modules
---> data_cleaning_classes (this directory contains classes for data ingestion and loading)
--------> data_ingestion.py (this file contains the class Ingestion, which imports multiple file types into pandas dataframes: CSVs, EXCEL, JSON, TEXT, ZIP)
----> social_security_data
---------> names (this file contains the 144 text files 
containing the first names, sex, and frequency of the name from the Social Security Administration from years 1880 - 2023. Each file name is: yobYYYY.txt)
----------> Other files (not used for the project; just keeping in this directory)
----> test_data (this directory contains any data used to test functionality of the classes or functions)
----------> test_excel.xlsx (a dummy data set for testing)
---> transform_social_security_names.py (this file utilizes the data_ingestion module, Ingestion Class, to ingestion 144 files containing first name, gender, and frequency of the names from the Social Security Administration from the years 1880 - 2023. This is for a particular project.)
---> README.md (this current file, which provides information about this repository)
---> requirements.txt (contains all the python dependencies used in this repo)


Contributions: This repository is not currently taking contributions since this is for personal use. If you are interested in contributing to this repository, reach out to Natasha at natasha@originsconvo.com with your proposed contribution. 
