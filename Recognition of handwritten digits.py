import numpy as np 
import random

class NN(object):
   
#Initialise a neural network with random weights and biases.
#sizes = [784, 30, 10] for 784 input, 30 hidden, 10 output neurons.
#num_layers = 3

   def __init__(self,sizes):
      
      self.sizes = sizes
      self.num_layers = len(sizes)

      self.biases = []
      # Initialize biases (for layers 1 to L-1)
      for y in sizes[1:]:
         self.biases.append(np.random.randn(y,1))

      self.weights = []
      # The weight matrix between layer l and l+1 has shape (sizes[l+1], sizes[l])
      for x, y in zip(sizes[:-1], sizes[1:]):
         self.weights.append(np.random.randn(y,x))
         #In neural networks, weights are typically stored as (output_dim, input_dim)
         #  for efficient forward pass computation (Wx + b).
  

   def sigmoid(self,z): # finally i figure out when i should add self into the ( )
        return 1 / (1 + np.exp(-z))
   
   def sigmoid_prime (self,z):
       s = self.sigmoid(z)
       return s * (1-s)

   def cost_derivative(self,output_activation,y):
        return output_activation - y


   def feedforward (self, input):
        a = input
        for b, w in zip(self.biases, self.weights):
            a = self.sigmoid( np.dot(w, a) + b)
        return a
   
   
   def SGD(self, training_data, epochs, mini_batch_size, lr):
       if training_data:
         n = len(training_data)
       for epoch in range(epochs):
           random.shuffle(training_data)
           mini_batches = []
           for x in range(0,n, mini_batch_size):
              mini_batch = training_data[x:x + mini_batch_size]
              mini_batches.append(mini_batch)
            
           for mini_batch in mini_batches:
               self.update_mini_batch(mini_batch, lr)

   
   def update_mini_batch(self, mini_batch, lr):
       # mini_batch is a list of several training samples,
       # whose each sample is a tuple(x,y), where x = input image, y = true label
       nabla_w = [np.zeros(w.shape) for w in self.weights] # nabla_w_sum[i]: the running total of those gradients across the entire mini-batch
       nabla_b = [np.zeros(b.shape) for b in self.weights]
       
       for x, y in mini_batch:
         delta_nabla_w, delta_nabla_b = self.backprop(x,y, self.weights,self.biases)
         for i in range(len(nabla_w)):
              nabla_w[i] += delta_nabla_w[i]
              nabla_b[i] += delta_nabla_b[i]

       
       for i in range(len(self.weights)):
          self.weights[i] =  self.weights[i] - nabla_w[i] * self.lr / len(mini_batch)
          self.biases[i] = self.biases[i] - nabla_b[i] * self.lr / len(mini_batch)
         
       
      #backward
   def backprop(self,x,y, weights,biases): 
   # x : input image ( 784 * 1 column vector)
   # y: expected label (10 * 1 column vector)
   

   #forward loop
      activation = x # current activation(starts with input)
      activations = [x] # store all activations layer by layer
      zs = [] # store all weighted input values before activation,

      for w, b in zip(weights, biases):
         z = np.dot(w,activation) + b
         zs.append(z)
         activation = self.sigmoid(z)
         activations.append(activation)

   # Backprop
      
   #1: error term, whose shape is (nl,1)
      delta = self.cost_derivative(activations[-1] - y) * self.sigmoid_prime(zs[-1])
   
   # store gradients
      nabla_w = [np.zeros(w.shape) for w in weights]
      nabla_b = [np.zeros(b.shape) for b in biases]
   #2: compute the error in the output layer 
      nabla_w[-1] = np.dot(delta, activations[-2].T)
      nabla_b[-1] = delta 
   #3: compute the error in the hidden layer
      for x in range(len(weights)-2,-1,-1):
         delta = np.dot(weights[x+1].T, delta) * self.sigmoid_prime(zs[x])
         nabla_b[x] = delta
         nabla_w[x] = np.dot(activation[x].T,delta)
         return nabla_w, nabla_b
      
   #4: update mini batch
   # now scroll up and find the "def update_mini_batch"


      



     








