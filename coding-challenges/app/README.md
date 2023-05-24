## Problem Statement - 1 (Anonymize customer information)
Imagine you are working on a project where you have to process customer data and generate insights. Considering this data has customer information and to generate insights, multiple teams will be using this data. To ensure we handle customer information with care, and not make it visible to everyone on the team one requirement is to anonymize customer information before it's loaded into the warehouse for insights generation.

- You will get this data in CSV files which will have customer personal information like first_name, last_name, address, date_of_birth
- Write code to generate a CSV file containing first_name, last_name, address, date_of_birth
- Load generated CSV in the previous step, anonymize data, and output anonymized data to a different file
- Columns to anonymise are first_name, last_name and address


Step 1:- Build the Docker image by running the following command:

cd ./coding-challenges/app
docker build -t data-anonymizer .


Step 2:- Run a Docker container from the built image with the following command:


cd ./coding-challenges/app
docker run --rm -v $(pwd):/app data-anonymizer


Step 3:- generate_anonymized_data.py uses faker library to generate the fake date for first_name,last_name, address and date_of_birth


Step 4:- Create the below config file as "config.json"

{
    "columns_list": {"first_name" : "first_name", "last_name" : "last_name", "address" : "address", "date_of_birth" : "date_of_birth"},
    "generated_output_file": "customer_data.csv",
    "anonymize_columns_list": ["first_name", "last_name", "address"],
    "anonymized_output_file": "anonymized_customer_data.csv",
    "N": 1000
}

where 
columns_list:- 
columns_list provides the list of columns for the given given file & type of fake data needs to generate. For example, 

For example :- first_name will use the faker.first_name() to generate the fake data for first_name

generated_output_file:- is the file generated using faker library

anonymize_columns_list :- is the list of columns needs to anonymized

anonymized_output_file :- is the file name which needs generate as output file.

N is the number of records needs to generate using faker library.

