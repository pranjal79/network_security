# Pipeline constants

PIPELINE_NAME = "network_security"
ARTIFACT_DIR = "artifacts"

DATA_INGESTION_DIR_NAME = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"
DATA_INGESTION_INGESTED_DIR = "ingested"

FILE_NAME = "phishing_data.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO = 0.2

# 🔴 MUST MATCH MONGODB ATLAS EXACTLY
DATA_INGESTION_DATABASE_NAME = "Network_Security"
DATA_INGESTION_COLLECTION_NAME = "NetworkData"

TARGET_COLUMN = "result"
