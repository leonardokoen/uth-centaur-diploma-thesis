import gpytorch
import pickle
import numpy as np
import torch
import os
class MultitaskGPModel(gpytorch.models.ExactGP):
  def __init__(self, train_x, train_y, likelihood, kernel):
      super(MultitaskGPModel, self).__init__(train_x, train_y, likelihood)
      self.mean_module = gpytorch.means.MultitaskMean(
          gpytorch.means.ConstantMean(), num_tasks=6
      )
      self.covar_module = gpytorch.kernels.MultitaskKernel(
         kernel, num_tasks=6, rank=1
      )


  # def change_kernel(self,kernel):
  #   self.covar_module = gpytorch.kernels.MultitaskKernel(
  #           kernel, num_tasks=6, rank=1
  #       )
  #   return
  def forward(self, x):
    mean_x = self.mean_module(x)
    covar_x = self.covar_module(x)
    return gpytorch.distributions.MultitaskMultivariateNormal(mean_x, covar_x)

class GP_model_for_cv():
    def __init__(self, num_epochs = 200, lr = 0.2, kernel = gpytorch.kernels.PolynomialKernel(power=2) + gpytorch.kernels.RBFKernel(ard_num_dims = 3)):
        # super(GP_model_for_cv, self).__init__()
        self.likelihood = gpytorch.likelihoods.MultitaskGaussianLikelihood(num_tasks=6)
        self.model = 0
        self.num_epochs = num_epochs
        self.lr = lr
        self.kernel = kernel

    def forward(self):
        return self

    def fit(self, train_x, train_y):
      train_x = torch.from_numpy(train_x).type('torch.DoubleTensor')
      train_y = torch.from_numpy(train_y).type('torch.DoubleTensor')


      self.model = MultitaskGPModel(train_x, train_y, self.likelihood, self.kernel).type('torch.DoubleTensor')
      # self.model.change_kernel(self.kernel)
      # if self.kernel != False:
      #   self.model.change_kernel(self.kernel)

      # train_x = torch.from_numpy(train_x).type('torch.DoubleTensor')
      # train_y = torch.from_numpy(train_y).type('torch.DoubleTensor')
      self.model.train()
      self.likelihood.train()

      optimizer = torch.optim.Adam(self.model.parameters(), lr=self.lr)
      mll = gpytorch.mlls.ExactMarginalLogLikelihood(self.likelihood, self.model)

      for i in range(self.num_epochs):
          optimizer.zero_grad()
          output = self.model(train_x)
          loss = -mll(output, train_y)
          loss.backward()
          # print('Iter %d/%d - Loss: %.3f' % (i + 1, self.num_epochs, loss.item()))
          optimizer.step()
      return self

    def predict(self, test_x):
      test_x = torch.from_numpy(test_x).type('torch.DoubleTensor')
      self.model.eval()
      self.likelihood.eval()

      with torch.no_grad():
          predictions = self.model(test_x)
      return predictions.mean.numpy()

    def predict_uncertainty(self, test_x):
      test_x = torch.from_numpy(test_x).type('torch.DoubleTensor')
      self.model.eval()
      self.likelihood.eval()

      with torch.no_grad():
          predictions = self.model(test_x)
          lower, upper = predictions.confidence_region()
      return lower.numpy(), upper.numpy()
    
    def save(self, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(self, file)

def load_model(filename):
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    return model

def load_models(path):
  day_models = []
  num_of_models = len(os.listdir(path))
  for i in range(num_of_models):
    name = path + "model" + str(i).zfill(2) + ".pkl"
    model = load_model(name)
    day_models.append(model)
  return day_models


def prediction_input(input_arguments):
  for i, element in  enumerate(input_arguments):
    element[2] = element[2] * element[3]
    element.pop()
  return np.array(input_arguments)