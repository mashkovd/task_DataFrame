# import 
from sqlalchemy import create_engine
from pandas import DataFrame

# string_connection
STR_CONNECTION_ALCH = 'mssql+pyodbc://{2}:{3}@{0}/{1}?driver=SQL Server'.format(SERVER, DATABASE, UID, PWD)

engine = create_engine(STR_CONNECTION_ALCH, encoding="cp1251")

size = 100 # shape of DataFrame

lst_data = [[randint(0,1), randint(0,1), randint(0,1)] for i in range(size)] # data for DataFrame 
lst_column = ['first', 'second', 'third'] # column of DataFrame

df = DataFrame(data=lst_data, columns=lst_column) # DataFrame 

try:
    df2db.to_sql('TABLE_NAME', engine, if_exists='append', index=False)
finally:
    engine.dispose()
