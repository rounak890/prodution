import pandas as pd
from config.config import settings
from loguru import logger

from config.config import engine
from db.db_model import RentApartments
from sqlalchemy import select

def get_data(path = settings.data_file_name):
    logger.info(f"loading csv file at place : {path}")
    return pd.read_csv(path)

# lets make  a function to load data from database
def load_data_from_db():
    logger.info("extracting the table from databse")
    # now we will need 1. ENGINE 2.Table Schema 3. Select obj from sqlalchemy needed for databse request

    query = select(RentApartments)
    return pd.read_sql(query, engine)

# now change the data loading method everywhere & change ml model name for more

## TESTING
# data = get_data()
# print(data)
