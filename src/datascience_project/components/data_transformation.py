import os
import urllib.request as request
from src.datascience_project import logger
import zipfile
from src.datascience_project.entity.config_entity import DataIngestionConfig, DataValidationConfig , DataTransformationConfig
import pandas as pd
from sklearn.model_selection import train_test_split
from src.datascience_project.config.configuration import ConfigurationManager


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        data=pd.read_csv(self.config.unzip_dir)
        train,test = train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        logger.info(f"Train and test data created")

        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
