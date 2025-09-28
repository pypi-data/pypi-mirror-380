if __name__ != "__main__":
    import cupy as cp
else:
    import numpy as cp
    import random


class Loss(object):
    """Loss functions for NN class"""

    def __init__(self):
        pass

    def mae(self, y, yhat):
        """
        Mean Absolute Error (MAE) between predicted values and actual values.

        Parameters
        -----------
        yhat: tensor
            The predicted values.
        y: tensor
            The actual values.

        Returns
        -------------
        float:
            The Mean Absolute Error between the predicted and actual values.
        """
        if yhat.shape == y.shape:
            return cp.mean(cp.abs(y - yhat))
        return cp.mean(cp.abs(cp.reshape(y, yhat.shape) - yhat))

    def mae_derivative(self, y, yhat, epsilon=1e-15):
        """
        Derivative of the Mean Absolute Error (MAE) loss function.

        Parameters
        ----------
        yhat: tensor
            The predicted values.
        y: tensor
            The actual values.

        Returns
        -------
        tensor
            The derivative of the MAE loss function with respect to the inputs.
        """
        if yhat.shape == y.shape:
            return (yhat - y) / (cp.abs(yhat - y) + epsilon)
        return (yhat - cp.reshape(y, yhat.shape)) / (cp.abs(yhat - cp.reshape(y, yhat.shape)) + epsilon)

    def mse(self, y, yhat):
        """
        Mean Squared Error (MSE) between predicted values and actual values.

        Parameters
        -----------
        yhat: tensor
            The predicted values.
        y: tensor
            The actual values.

        Returns
        -------------
        float:
            The Mean Squared Error between the predicted and actual values.
        """
        if yhat.shape == y.shape:
            return cp.mean((y - yhat) ** 2)
        return cp.mean((cp.reshape(y, yhat.shape) - yhat) ** 2)

    def mse_derivative(self, y, yhat):
        """
        Derivative of the Mean Squared Error (MSE) loss function.

        Parameters
        ----------
        yhat: tensor
            The predicted values.
        y: tensor
            The actual values.

        Returns
        -------
        tensor
            The derivative of the MSE loss function with respect to the inputs.
        """
        if yhat.shape == y.shape:
            return 2 * (yhat - y)
        return 2 * (yhat - cp.reshape(y, yhat.shape))

    def binary_crossentropy(self, y, yhat, epsilon=1e-15):
        """
        Evaluates the distance between the true labels and the predicted probabilities
        by evaluating the logarithmic loss.

        Parameters
        -----------
        y: tensor
            The true labels.
        yhat: tensor
            The predicted probabilities.

        Returns
        --------
        float:
            The logarithmic loss between the true labels and the predicted probabilities.
        """
        return cp.mean(-(y * cp.log(cp.maximum(yhat, epsilon)) + (1 - y) * cp.log(cp.maximum(1 - yhat, epsilon))))

    def binary_crossentropy_derivative(self, y, yhat, epsilon=1e-15):
        """
        Derivative of the binary cross-entropy loss function.

        Parameters
        -----------
        y: tensor
            The true labels.
        yhat: tensor
            The predicted probabilities.

        Returns
        --------
        tensor:
            The derivative of the binary cross-entropy loss function with respect to the inputs.

        Raises
        --------
        RuntimeWarning: divide by zero or invalid value encountered in divide.
            Fix afterward.
        """
        return ((1 - y) / (1 - yhat)) - (y / yhat)


if __name__ == "__main__":
    l = Loss()
    y = cp.array(random.sample(range(10), 10))
    yhat = cp.array(random.sample(range(10), 10))
    print("Y")
    print(y)
    print("Yhat")
    print(yhat)
    print("mae")
    print(l.mae(y, yhat))
    print(l.mae_derivative(y, yhat))
    print("mse")
    print(l.mse(y, yhat))
    print(l.mse_derivative(y, yhat))
    print("binary crossentropy")
    y = cp.array(random.sample(range(2), 2))
    yhat = cp.array(cp.random.uniform(0, 1, 2))
    print("Y")
    print(y)
    print("Yhat")
    print(yhat)
    print(l.binary_crossentropy(y, yhat))
    print(l.binary_crossentropy_derivative(y, yhat))
