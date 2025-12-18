from datetime import datetime
import os

# Import constants directly from training_pipeline package
from network_security.constants.training_pipeline import (
    PIPELINE_NAME,
    ARTIFACT_DIR,
    DATA_INGESTION_DIR_NAME,
    DATA_INGESTION_FEATURE_STORE_DIR,
    DATA_INGESTION_INGESTED_DIR,
    FILE_NAME,
    TRAIN_FILE_NAME,
    TEST_FILE_NAME,
    DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO,
    DATA_INGESTION_COLLECTION_NAME,
    DATA_INGESTION_DATABASE_NAME
)


class TrainingPipelineConfig:
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        self.pipeline_name = PIPELINE_NAME
        self.artifact_dir = ARTIFACT_DIR

        self.artifact_dir_with_timestamp = os.path.join(
            self.artifact_dir,
            self.timestamp
        )


class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):

        self.data_ingestion_dir = os.path.join(
            training_pipeline_config.artifact_dir_with_timestamp,
            DATA_INGESTION_DIR_NAME
        )

        self.feature_store_file_path = os.path.join(
            self.data_ingestion_dir,
            DATA_INGESTION_FEATURE_STORE_DIR,
            FILE_NAME
        )

        self.train_file_path = os.path.join(
            self.data_ingestion_dir,
            DATA_INGESTION_INGESTED_DIR,
            TRAIN_FILE_NAME
        )

        self.test_file_path = os.path.join(
            self.data_ingestion_dir,
            DATA_INGESTION_INGESTED_DIR,
            TEST_FILE_NAME
        )

        self.train_test_split_ratio = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name = DATA_INGESTION_COLLECTION_NAME
        self.database_name = DATA_INGESTION_DATABASE_NAME
