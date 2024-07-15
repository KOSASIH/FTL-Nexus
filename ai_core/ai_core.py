import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, LSTM

class AICore:
    def __init__(self, num_inputs, num_outputs, hidden_layers):
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs
        self.hidden_layers = hidden_layers

    def create_neural_network(self):
        """
        Create a neural network using Keras.

        Returns:
            Model: The created neural network.
        """
        inputs = Input(shape=(self.num_inputs,))
        x = Dense(self.hidden_layers[0], activation="relu")(inputs)
        for i in range(1, len(self.hidden_layers)):
            x = Dense(self.hidden_layers[i], activation="relu")(x)
        outputs = Dense(self.num_outputs, activation="softmax")(x)
        model = Model(inputs=inputs, outputs=outputs)
        return model

    def train_neural_network(self, model, X_train, y_train, X_test, y_test):
        """
        Train a neural network using Keras.

        Args:
            model (Model): The neural network to train.
            X_train (numpy array): The training input data.
            y_train (numpy array): The training output data.
            X_test (numpy array): The testing input data.
            y_test (numpy array): The testing output data.
        """
        model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
        model.fit(X_train, y_train, epochs=100, batch_size=128, validation_data=(X_test, y_test))

    def use_neural_network(self, model, input_data):
        """
        Use a trained neural network to make predictions.

        Args:
            model (Model): The trained neural network.
            input_data (numpy array): The input data to make predictions on.

        Returns:
            numpy array: The predicted output data.
        """
        predictions = model.predict(input_data)
        return predictions

    def optimize_neural_network(self, model, X_train, y_train, X_test, y_test):
        """
        Optimize a neural network using a genetic algorithm.

        Args:
            model (Model): The neural network to optimize.
            X_train (numpy array): The training input data.
            y_train (numpy array): The training output data.
            X_test (numpy array): The testing input data.
            y_test (numpy array): The testing output data.
        """
        from scipy.optimize import differential_evolution
        def objective_function(params):
            model.set_weights(params)
            loss = model.evaluate(X_test, y_test)
            return loss
        bounds = [(0, 1) for _ in range(model.count_params())]
        result = differential_evolution(objective_function, bounds)
        optimized_weights = result.x
        model.set_weights(optimized_weights)
        return model
