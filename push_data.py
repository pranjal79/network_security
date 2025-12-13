import os
import json
from dotenv import load_dotenv
import certifi
import pandas as pd
import pymongo

from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging

# Load environment variables
load_dotenv()
mongodb_url = os.getenv("MONGODB_URL")

# SSL certificate
ca = certifi.where()


class NetworkDataExtract:
    def __init__(self):
        try:
            self.mongo_client = pymongo.MongoClient(
                mongodb_url,
                tlsCAFile=ca
            )
        except Exception as e:
            raise NetworkSecurityException(e)

    def csv_to_json_converter(self, file_path):
        try:
            logging.info("Reading CSV file")
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)

            records = json.loads(data.T.to_json()).values()
            records = list(records)

            logging.info("CSV successfully converted to JSON")
            return records

        except Exception as e:
            raise NetworkSecurityException(e)

    def insert_data_mongodb(self, records, database, collection):
        try:
            logging.info("Inserting data into MongoDB")

            db = self.mongo_client[database]
            col = db[collection]

            col.insert_many(records)

            logging.info("Data inserted successfully")
            return len(records)

        except Exception as e:
            raise NetworkSecurityException(e)


if __name__ == "__main__":
    file_path = "./network_data/fishing_data.csv"
    database = "crash_i"
    collection = "network_data"

    network_obj = NetworkDataExtract()

    records = network_obj.csv_to_json_converter(file_path)
    count = network_obj.insert_data_mongodb(records, database, collection)

    print(f"Number of records inserted: {count}")
