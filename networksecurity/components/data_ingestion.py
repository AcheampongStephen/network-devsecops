import os
import sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.artifact_entity import DataIngestionArtifact
import pymongo
import pandas as pd
import numpy as np
from typing import List
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv
load_dotenv()

# Get the MongoDB URL
MONGO_DB_URL = os.getenv("MONGO_URI")
print(f"MONGO_DB_URL: {MONGO_DB_URL}")

# Configuration of the Data Ingestion Conifig
from networksecurity.entity.config_entity import DataIngestionConfig



class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def export_collection_as_dataframe(self):
        """Export the MongoDB collection as a DataFrame"""
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            collection = self.mongo_client[database_name][collection_name]

            # Get the data from the collection
            df = pd.DataFrame(list(collection.find()))

            if "_id" in df.columns.to_list():
                df.drop(columns=["_id"], axis=1)

            df.replace({"na": np.nan}, inplace=True)

            return df
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
            

            
    def export_data_into_feature_store(self, dataframe: pd.DataFrame):
        """Export the data into the feature store"""
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path

            # creating folder
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe
            
        except Exception as e:
            raise NetworkSecurityException(e,sys)
            

    def split_data_into_train_test(self, dataframe: pd.DataFrame):
        """Split the data into train and test"""
        try:
            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio)
            logging.info("Performed train test split on the dataframe")
            logging.info("Exiting the split_data_into_train_test method of DataIngestion class")

            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)

            logging.info("Exporting train and test file path")

            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False, header=True)

            logging.info("Exported train and test file path")

        except Exception as e:
            raise NetworkSecurityException(e,sys)
 
            
    def initiate_data_ingestion(self):
        """Initiate the data ingestion process"""
        try:
            dataframe = self.export_collection_as_dataframe()
            dataframe = self.export_data_into_feature_store(dataframe)
            self.split_data_into_train_test(dataframe)
            dataingestionartifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
                                                              test_file_path=self.data_ingestion_config.testing_file_path)
            return dataingestionartifact 
        except Exception as e:
            raise NetworkSecurityException(e,sys)






