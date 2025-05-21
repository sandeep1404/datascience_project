import os
import urllib.request as request
from src.datascience_project import logger
import zipfile
from src.datascience_project.entity.config_entity import DataIngestionConfig, DataValidationConfig
import pandas as pd
from src.datascience_project.config.configuration import ConfigurationManager

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self)->bool:
        try:
            validation_status = None
            data= pd.read_csv(self.config.unzip_dir)
            all_columns = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_columns:
                if col not in all_schema:
                    validation_status = False
                    logger.info(f"Column {col} is not in schema")
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation Status: {validation_status}\n")
                    break
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation Status: {validation_status}\n")

        except Exception as e:
            raise e