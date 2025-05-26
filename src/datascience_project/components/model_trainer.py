from src.datascience_project import logger
from src.datascience_project.entity.config_entity import ModelTrainerConfig
from src.datascience_project.config.configuration import ConfigurationManager
import pandas as pd
from sklearn.linear_model import ElasticNet
import joblib
import os


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    def train(self):
        train_df = pd.read_csv(self.config.train_data_path)
        test_df = pd.read_csv(self.config.test_data_path)

        train_x= train_df.drop(columns=[self.config.target_column], axis=1)
        train_y= train_df[self.config.target_column]
        test_x= test_df.drop(columns=[self.config.target_column], axis=1)
        test_y= test_df[self.config.target_column]

        lr =ElasticNet(alpha=self.config.alpha,l1_ratio=self.config.l1_ratio,random_state=42)
        lr.fit(train_x,train_y)

        joblib.dump(lr,os.path.join(self.config.root_dir,self.config.model_name))
        logger.info(f"Model trained and saved at {self.config.root_dir}")