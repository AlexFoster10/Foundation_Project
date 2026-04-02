# Equities Market Data Processing Tool
This project allows users to manipulate and carry out operations on market data. All input market data is validated and I/O is through csv files.

## How It's Made:

**Tech used:** Python, Pandas, Sqlite, Pytest, Docker

The project is made of a main.py and seperate .py files for Input, Validation, Processing and Output, with a supplementary .py file for logger definition. There is also a testing file for each .py file. The program passes the data in turn through each file, and outputs a processed data CSV with calculated daily return, price spread, simple moving average and volume change for each csv entry. Before processing, all of the csv data is cleaned and checked for blank fields and nonsensical values (i.e low field higher than high field, 0 open price e.t.c). The data is also flashed to an sqlite DB after processing. A user can run the project from command line, with arguments 1 and 2 corresponding to input and output file paths. If paths are not provided, the program will use sample data instead. When run using fastapi, the endpoint shows the processed financial data as an html table. The project also contains Docker support

## Optimizations
At some point I think optimising the database to store a table of input prices and a table of processed prices would be something I could tackle, as it would allow for large scale data analyis. Also currently the database is very barebones, as it flashes all csv data, regardless of duplicate information. I think using SQlalchemy to improve the database is an obvious next step to take

## Lessons Learned:
This project massively bolstered my Pandas capabilities, as well as furthered my understanding of financial data concepts. I've improved my scripting, data manipulation, logging and testing thanks to this project.  
