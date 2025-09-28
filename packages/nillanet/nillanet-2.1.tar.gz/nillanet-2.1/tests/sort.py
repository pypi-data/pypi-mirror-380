from nillanet.model import NN
from nillanet.activations import Activations
from nillanet.loss import Loss
from nillanet.distributions import Distributions
from nillanet.scheduler import Scheduler

d = Distributions()
x,y = d.sort(10,5)
print(x.shape)
print(y.shape)

a = Activations()
activation = a.sigmoid
derivative1 = a.sigmoid_derivative
resolver = a.linear
derivative2 = a.linear_derivative

l = Loss()
loss = l.mse
derivative3 = l.mse_derivative

input = x
output = y
features = x.shape[1]
architecture = [32,16,8,5]
learning_rate = 0.01
epochs = 10000
scheduler = Scheduler(mode='cosine', lr=learning_rate)

model = NN(features,architecture,activation,derivative1,resolver,derivative2,loss,derivative3,learning_rate,scheduler=scheduler)
model.summary()

for epoch in range(epochs):
    model.train(input,output,epoch,epochs,verbose=True,step=1000,autosave=True)

prediction = model.predict(x)

print("prediction")
print(prediction)
print("expected")
print(y)
