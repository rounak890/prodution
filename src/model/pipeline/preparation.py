# here we will preprocess the data by using regex etc
import pandas as pd
import re
from model.pipeline.collection import get_data, load_data_from_db

from loguru import logger

def prepare_data():
    logger.info("start up preprocessing pipeline")
    #1. LOAD THE DATASET
    data = load_data_from_db() # get_data()

    #2. ENCODE COLS LIKE BALCONY ETC
    data_enc = encode_cat_cols(data)

    #3. PARSE THE GARDEN COLUMN
    data_enc = parse_garden_col(data_enc)
    return data_enc

def encode_cat_cols(data):
    cols = ['balcony','parking','furnished','garage','storage']
    logger.info(f"Encoding categorical columns :{cols}")

    data_encoded = pd.get_dummies(data, 
                                columns = cols, 
                                drop_first=True)

    return data_encoded

def parse_garden_col(data):
    logger.info("parsing garden column")
    for i in range(len(data)):
        if data.garden[i]=='Not present':
            data.garden[i]=0
        else: 
            data.garden[i] = int(re.findall(r'\d+', data.garden[i])[0])

    return data

# test
# data = prepare_data()
# print(data.garden)