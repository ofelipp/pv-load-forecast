# ! ./venv/bin/python3.8

"""
Script containing linear regression model construction, training and predict
functions.
"""

from logging import debug, info
import numpy as np
from sklearn.linear_model import LinearRegression
from src.data.io import save_artfact


def linear_regression():

    """ Creates a linear regression model """

    return LinearRegression()


def train_linear_regression(
    model: LinearRegression, features: np.ndarray, labels: np.ndarray,
    model_name: str = ""
) -> LinearRegression:

    """ Train Linear Regression model to perform predictions """

    debug(f"Shape of features:\t{features.shape}")
    debug(f"Shape of labels:\t{features.shape}")

    info("Starting training...")

    trained_lr = model.fit(features, labels)

    info("Training complete...")

    debug(f"R_Squared:\t{trained_lr.score(features, labels)}")
    debug(f"Intercept:\t{trained_lr.intercept_}")
    debug(f"Coeficients:\t{trained_lr.coef_}")

    info("Saving Model pickle...")

    save_artfact(trained_lr, f"linear_regression{model_name}")

    return trained_lr


def predict_linear_regression():

    """ Train Linear Regression Model """

    return ...
