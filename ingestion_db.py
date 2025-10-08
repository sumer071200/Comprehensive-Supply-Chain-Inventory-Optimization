import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename = "logs/SupplyChain_db.log",
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    filemode = "a"
)

engine = create_engine('sqlite:///SupplyChain.db')

def ingest_db(df, table_name, engine):
    '''This function will ingest the dataframe into database table'''
    df.to_sql(table_name, con = engine, if_exists = 'replace', index = False)

def load_raw_data():
    '''This function will load the CSVs as dataframe and ingest into db'''
    start = time.time()
    for file in os.listdir('supply_chain_data'):
        if '.csv' in file:
            df = pd.read_csv('supply_chain_data/' + file)
            logging.info(f'ingesting {file} in db')
            ingest_db(df, file[:-4], engine)
    end = time.time()
    total_time = (end - start)/60
    logging.info('------------Ingestion Complete------------')
    logging.info(f'\n Total Time Taken: {total_time} minutes')

if __name__ == '__main__':
    load_raw_data()