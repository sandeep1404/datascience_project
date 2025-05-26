import os

import mlflow.sklearn
from src.datascience_project import logger
from src.datascience_project.entity.config_entity import ModelEvaluationConfig
from src.datascience_project.config.configuration import ConfigurationManager
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
import numpy as np
from urllib.parse import urlparse
import pandas as pd
import joblib
import mlflow
from pathlib import Path
from src.datascience_project.utils.common import save_json, read_yaml, create_directories
from dotenv import load_dotenv
load_dotenv()


os.environ["MLFLOW_TRACKING_USERNAME"] = os.getenv("MLFLOW_TRACKING_USERNAME")
os.environ["MLFLOW_TRACKING_PASSWORD"] = os.getenv("MLFLOW_TRACKING_PASSWORD")

os.environ["MLFLOW_TRACKING_URI"]= os.getenv("MLFLOW_TRACKING_URI")



class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        
    def evaluate_metrics(self,actual,pred):
        rmse= np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[self.config.target_column]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_uri_type_store=  urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
           
            predicted_qualities = model.predict(test_x)
            rmse, mae, r2 = self.evaluate_metrics(test_y, predicted_qualities)

            scores ={"rmse": rmse,"mae": mae,"r2": r2
                     }
            
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            if tracking_uri_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.log_model(model, "model")