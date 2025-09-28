from nillanet.model import NN
from nillanet.activations import Activations
from nillanet.loss import Loss
from nillanet.distributions import Distributions
from nillanet.scheduler import Scheduler

# one hots
print("one hots")

d = Distributions()
x,y = d.summation(10,3,mode="one_hot")
print(x.shape)
print(y.shape)

a = Activations()
activation = a.sigmoid
derivative1 = a.sigmoid_derivative
resolver = a.sigmoid
derivative2 = a.sigmoid_derivative

l = Loss()
loss = l.binary_crossentropy
derivative3 = l.binary_crossentropy_derivative

input = x
output = y
features = x.shape[1]
architecture = [2,4,4]
learning_rate = 0.1
epochs = 1000
scheduler = Scheduler(mode='cosine', lr=learning_rate)

model = NN(features,architecture,activation,derivative1,resolver,derivative2,loss,derivative3,learning_rate,scheduler=scheduler)
model.summary()

for epoch in range(epochs):
    model.train(input,output,epoch,epochs,verbose=True,step=100,autosave=True)

prediction = model.predict(x)

print("prediction")
print(prediction)
print("expected")
print(y)

# summation
print("summation")

x,y = d.summation(10,4,"summation")
print(x.shape)
print(y.shape)

activation = a.sigmoid
derivative1 = a.sigmoid_derivative
resolver = a.linear
derivative2 = a.linear_derivative

loss = l.mse
derivative3 = l.mse_derivative

input = x
output = y
features = x.shape[1]
architecture = [2,4,1]
learning_rate = 0.01
epochs = 10000

model = NN(features,architecture,activation,derivative1,resolver,derivative2,loss,derivative3,learning_rate)
model.summary()

for epoch in range(epochs):
    model.train(input,output,epoch,epochs)

prediction = model.predict(x)

print("prediction")
print(prediction)
print("expected")
print(y)