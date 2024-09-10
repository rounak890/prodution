"""
This module provide functionality for running a ML module

It contains ModelService class which loads and  predicts on model
using pre trained pickle file.
"""
# for msking the preds

import pickle as pk
from pathlib import Path

from loguru import logger

from config.config import settings
from model.pipeline.models import build_model
# VIMP SINCE I USED MODEL.PIPELINE INSTEAD OF ONLY PIPELINE


class ModelService:
    """
    a service class for managing ML module

    This class provide functionality for loading a model
    from a specified path, build it if it don't exsists
    and perform predctions on it

    Attributes:
        Model : ML model made up by this module initially None

    Methods:
        __init__ : constructor that initializes the Model Service class

        load_model : This module loads the ML model and builds it if it 
                    dont exists

        predict : This module perform predictions on the loaded module 
                    by taking inputs
    """

    def __init__(self) -> None:
        """constructor that initializes the Model Service class"""
        self.model = None

    def load_model(self) -> None:
        # select the model if not exsist then make one
        """This module loads the ML model and builds it if it dont exists"""
        logger.info(f"Checking if the model exsists at {settings.model_path}/{settings.model_name}")
        model_path = Path(f"{settings.model_path}/{settings.model_name}")

        if not model_path.exists():
            logger.warning(
                f"Modle at {settings.model_path}/{settings.model_name}"
                f" was not found -> building {settings.model_name}",
            )

            build_model()

        logger.info("model exsist -> loading" 
                    "model config file")

        with open(f'{settings.model_path}/{settings.model_name}', 'rb') as file:
            self.model = pk.load(file)

    def predict(self, input: list) -> list:  # make preds
        """this perform predictions on our ML model

        It takes input and uses our loaded ML model from 
        pickle files to perform pred on it

        Args:
            input (list): input data to make predictions

        Returns:
            list: prediction result from the model
        """
        logger.info("predicting")
        return self.model.predict([input])


# test
# ml_svc = ModelService()
# ml_svc.load_model('rf_v1')
# pred = ml_svc.predict( [85, 2015, 2, 20, 1, 1, 0, 0, 1])
# print(pred)
