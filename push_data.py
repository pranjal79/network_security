import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo

from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging


class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_converter(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)

            records = json.loads(data.T.to_json()).values()
            records = list(records)

            return records

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            self.mongo_client = pymongo.MongoClient(
                MONGO_DB_URL,
                tlsCAFile=ca
            )

            self.database = self.mongo_client[database]
            self.collection = self.database[collection]

            self.collection.insert_many(records)
            return len(records)

        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == '__main__':
    FILE_PATH = r"D:\network_security\Network_Data\PhishingData.csv"
    DATABASE = "Network_Security"
    COLLECTION = "NetworkData"

    network_obj = NetworkDataExtract()

    records = network_obj.csv_to_json_converter(FILE_PATH)
    number_of_records = network_obj.insert_data_mongodb(
        records,
        DATABASE,
        COLLECTION
    )

    print(f"Number of records inserted: {number_of_records}")
