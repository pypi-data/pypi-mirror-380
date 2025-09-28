import cupy as cp
import numpy as np
import os
import math
import random
import re
import pickle
from nillanet.io import IO
import tempfile
import logging
import sys

logging.basicConfig(level=logging.INFO, force=True, format="%(message)s")

cp.random.seed()
cp.set_printoptions(precision=2,floatmode='fixed',suppress=True)

class NN(object):

  """Minimal feedforward neural network using CuPy.

    This class implements batched SGD with configurable activation,
    resolver, and loss functions. Inputs/targets are kept on device
    to avoid host↔device copies.

    Args:
        features (int): Columnar shape of inputs.
        architecture (list[int]): Units per layer, including output layer.
        activation (Callable[[cupy.ndarray], cupy.ndarray]): Hidden-layer
            activation function.
        derivative1 (Callable[[cupy.ndarray], cupy.ndarray]): Derivative of
            ``activation`` evaluated at pre-activations.
        resolver (Callable[[cupy.ndarray], cupy.ndarray]): Output-layer
            transfer function (e.g., identity, sigmoid, softmax).
        derivative2 (Callable[[cupy.ndarray], cupy.ndarray]): Derivative of
            ``resolver`` evaluated at pre-activations.
        loss (Callable[..., cupy.ndarray]): Loss function that accepts
            named arguments (e.g., ``yhat``, ``y``) and returns per-sample
            losses or their average.
        derivative3 (Callable[..., cupy.ndarray]): Derivative of ``loss``
            with respect to predictions (same signature as ``loss``).
        learning_rate (float): SGD step size.
        scheduler (Scheduler): Learning rate scheduler.
        dtype (cupy.dtype, optional): Floating point dtype for parameters and data.
            Defaults to ``cupy.float32``.
        backup (str): Path for saving the highest performing model during training.
        initializer (Initializer): Function for initializing weights.

    Attributes:
        W (list[cupy.ndarray]): Layer weight matrices; ``W[i]`` has shape
            (in_features_i, out_features_i).
  """

  def __init__(self, features, architecture, activation, derivative1,
               resolver, derivative2, loss, derivative3, learning_rate, scheduler=None,
               dtype=cp.float32, backup="/tmp/nn.pkl", initializer=None):
    self.architecture = architecture
    self.activation = activation
    self.activation_derivative = derivative1
    self.resolver = resolver
    self.resolver_derivative = derivative2
    self.loss = loss
    self.loss_derivative = derivative3
    self.lr = learning_rate
    self.dtype = dtype
    self.backup = backup
    self.scheduler = scheduler
    self.initializer = initializer

    self.W = []
    features += 1 # bias
    for i in range(len(self.architecture)):
      nodes = self.architecture[i]
      if self.initializer is None:
          # weights initialized from [-1, 1]
          w = 2 * cp.random.random((features, nodes), dtype=self.dtype) - 1
      else:
          w = cp.asarray(self.initializer((features, nodes)))
      self.W.append(w)
      features = nodes

  def train(self, input, output, epoch=1, epochs=1, batch=0, verbose=False, step=1000, autosave=False, minloss=[999999999]):
    """Train the model for one epoch using simple SGD.

        Each epoch is a full pass over the training data.
        Note that your own external training loop is expected.

        Args:
            input (cupy.ndarray | numpy.ndarray): Training inputs of shape
              (n_samples, n_features). If NumPy, it will be moved to device.
            output (cupy.ndarray | numpy.ndarray): Training targets of shape
              (n_samples, n_outputs). If NumPy, it will be moved to device.
            epoch: Step number of epoch.
            epochs: Expected number of SGD steps that will be run.
            batch: One of:
                - ``1``: sample a single example per step (pure SGD)
                - ``0``: use all samples per step (full batch)
                - ``>1`` and ``< len(Y)``: use that mini-batch size per step
            verbose (bool): Print progress to stdout.
            step (int): Print progress every ``step`` epochs.
            autosave (bool): Save the model with the highest loss to disk.
            minloss (list[float]): Internal use only.

        Raises:
            SystemExit: If ``batch`` is invalid.
    """
    # keep data on device and in a consistent dtype
    X = cp.array(input, dtype=self.dtype)
    Y = cp.array(output, dtype=self.dtype)

    # device-side bias column (avoid NumPy)
    bias = cp.ones((X.shape[0], 1), dtype=self.dtype)
    X = cp.concatenate((bias, X), axis=1)

    io = IO()
    def progress(yhat, y):
        nonlocal minloss
        loss = self.loss(y=y, yhat=yhat)
        loss = cp.mean(loss)
        if loss < minloss[0]:
            minloss[0] = loss
            if autosave:
                io.save(self, self.backup)
        return loss

    n = X.shape[0]
    if batch == 0:
        yhat = self.batch(X, Y)
    elif batch == 1:
      indices = list(range(n))
      random.shuffle(indices)
      yhat = cp.zeros(Y.shape)
      for index in indices:
        h = self.batch(X[index], Y[index])
        yhat[index] = h.ravel()
    elif 1 < batch < n:
      indices = list(range(0,n,batch))
      random.shuffle(indices)
      yhat = cp.zeros(Y.shape)
      for index in indices:
        if index + batch > n:
            continue
        x = X[index:index + batch]
        y = Y[index:index + batch]
        h = self.batch(x, y)
        yhat[index:index + batch] = h.ravel()
    else:
      sys.exit(f"improper batch size {batch}")

    if epoch % step == 0:
        prog = progress(yhat, Y)
        if verbose:
            logging.info("epoch %d loss %.8f" % (epoch, prog))

    if self.scheduler is not None:
      self.lr = self.scheduler.step(epoch, epochs)

  def batch(self, x, y):
    """Run a single forward/backward/update step.

        Args:
            x (cupy.ndarray | numpy.ndarray): Inputs, shape (B, D) or (D,).
            y (cupy.ndarray | numpy.ndarray): Targets, shape (B, K) or (K,).

        Returns:
            q: the predictions as a tensor
    """
    # ensure inputs reside on device & 2D
    x = cp.nan_to_num(cp.atleast_2d(cp.asarray(x)), nan=0.0)
    y = cp.nan_to_num(cp.atleast_2d(cp.asarray(y)), nan=0.0)

    inputs = []
    raw_outputs = []

    # forward
    q = x
    for i in range(len(self.architecture)):
      inputs.append(q)
      z = cp.nan_to_num(q @ self.W[i], nan=0.0)
      raw_outputs.append(z)
      if i == len(self.architecture) - 1:
        q = cp.nan_to_num(self.resolver(z), nan=0.0)
      else:
        q = cp.nan_to_num(self.activation(z), nan=0.0)

    # backward
    prev_grad = None
    for i in range(len(self.architecture) - 1, -1, -1):
      if i == len(self.architecture) - 1:
        loss_grad = cp.nan_to_num(self.loss_derivative(y=y, yhat=q), nan=0.0)
        grad = cp.nan_to_num(loss_grad * self.resolver_derivative(raw_outputs[i]), nan=0.0)
      else:
        grad = cp.nan_to_num((prev_grad @ self.W[i + 1].T) * self.activation_derivative(raw_outputs[i]), nan=0.0)

      # in-place weight update
      self.W[i] -= self.lr * (inputs[i].T @ grad)
      self.W[i] = cp.nan_to_num(self.W[i], nan=0.0)
      prev_grad = grad

    return q

  def predict(self, input):
    """Run a forward pass to produce predictions.

        Args:
            input (cupy.ndarray | numpy.ndarray): Inputs of shape
                (n_samples, n_features). If NumPy, it will be moved to device.

        Returns:
            cupy.ndarray: Model outputs of shape (n_samples, n_outputs).
    """
    yhat = cp.atleast_2d(cp.asarray(input))
    bias = cp.ones((yhat.shape[0], 1), dtype=yhat.dtype)
    yhat = cp.concatenate((bias, yhat), axis=1)

    for i in range(len(self.architecture)):
      h = cp.nan_to_num(yhat @ self.W[i], nan=0.0)
      if i == len(self.architecture) - 1:
        yhat = cp.nan_to_num(self.resolver(h), nan=0.0)
      else:
        yhat = cp.nan_to_num(self.activation(h), nan=0.0)
    return yhat

  def summary(self):
    """Print layer shapes and total parameter count."""
    total = 0
    for idx, w in enumerate(self.W):
      params = w.shape[0] * w.shape[1]
      total += params
      logging.info(f"layer {idx} weights {tuple(w.shape)} parameters {params}")
    logging.info(f"total parameters {total}")

