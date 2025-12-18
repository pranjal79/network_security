from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.entity.config_entity import DataIngestionConfig
from network_security.entity.artifact_entity import DataIngestionArtifact

import os
import sys
import pymongo
import pandas as pd
import numpy as np

from dotenv import load_dotenv
from sklearn.model_selection import train_test_split

# Load environment variables
load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def export_collection_as_dataframe(self) -> pd.DataFrame:
        """
        Read MongoDB collection and convert to pandas DataFrame
        """
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name

            logging.info(
                f"Reading data from MongoDB database: {database_name}, collection: {collection_name}"
            )

            mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            collection = mongo_client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))

            # Drop MongoDB internal id
            if "_id" in df.columns:
                df.drop(columns=["_id"], inplace=True)

            # Replace string 'na' with NaN
            df.replace("na", np.nan, inplace=True)

            logging.info("Successfully exported MongoDB data to DataFrame")
            return df

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def export_data_to_feature_store(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Save raw data to feature store
        """
        try:
            feature_store_path = self.data_ingestion_config.feature_store_file_path
            os.makedirs(os.path.dirname(feature_store_path), exist_ok=True)

            df.to_csv(feature_store_path, index=False, header=True)
            logging.info(f"Feature store saved at: {feature_store_path}")

            return df

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def split_data_as_train_test(self, df: pd.DataFrame):
        """
        Split data into train and test and save them
        """
        try:
            train_df, test_df = train_test_split(
                df,
                test_size=self.data_ingestion_config.train_test_split_ratio,
                random_state=42
            )

            train_path = self.data_ingestion_config.train_file_path
            test_path = self.data_ingestion_config.test_file_path

            os.makedirs(os.path.dirname(train_path), exist_ok=True)

            train_df.to_csv(train_path, index=False, header=True)
            test_df.to_csv(test_path, index=False, header=True)

            logging.info("Train and test data saved successfully")
            return train_path, test_path

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        """
        Main method to run data ingestion pipeline
        """
        try:
            df = self.export_collection_as_dataframe()
            df = self.export_data_to_feature_store(df)

            train_path, test_path = self.split_data_as_train_test(df)

            return DataIngestionArtifact(
                train_file_path=train_path,
                test_file_path=test_path
            )

        except Exception as e:
            raise NetworkSecurityException(e, sys)
