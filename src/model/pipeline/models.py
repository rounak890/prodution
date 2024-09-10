from model.pipeline.preparation import prepare_data
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import pickle as pk

from loguru import logger

from config.config import settings
    
def build_model():
    logger.info("starting up model building pipeline")
    data = prepare_data()
    
    X,y = get_xy(data)
    
    # they had made function for splitting but i have n't
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    rf = train_model(X_train, y_train)

    score = evaluate_model(rf, X_test, y_test)
    # print(score)

    save_model(rf)


def get_xy(data, colx = ['area', 
                'constraction_year', 
                'bedrooms', 
                'garden', 
                'balcony_yes', 
                'parking_yes', 
                'furnished_yes', 
                'garage_yes', 
                'storage_yes'], 
                coly = 'rent'):

    logger.info(f"defining X and y variables.\n X vars : {colx} || y vars : {coly}")
    return data[colx], data[coly]

def train_model(X_train, y_train):
    logger.info("Training the model with hyperparameter tunning")
    # for hyper param tunning we are modifying here only
    grid_space = {'n_estimators': [100, 200, 300], 'max_depth': [3, 6, 9, 12]}
    logger.debug(f"GRID SPACE : {grid_space}")

    grid = GridSearchCV(RandomForestRegressor(), param_grid=grid_space, cv=5, scoring = 'r2')
    model_grid = grid.fit(X_train, y_train) # return the best model

    # rf = RandomForestRegressor()
    # rf.fit(X_train, y_train) 
    
    return model_grid # returning the trained model

def evaluate_model(rf, X_test, y_test):
    score = rf.score(X_test, y_test)
    logger.info(f"Evaluating the model's performance SCORE : {score}")
    return score


def save_model(model):
    logger.info(f"Saving a model to directory : {settings.model_path}/{settings.model_name}")
    # pk.dump(model, open('models/rf_v1', 'wb')) # we shall create models folder before hand
    pk.dump(model, open(f'{settings.model_path}/{settings.model_name}', 'wb')) 

    print("SUCCESSFULLY SAVED!")

# test
build_model()