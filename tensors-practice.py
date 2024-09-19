import tensorflow as tf

def getVersion():
  #Prints the current version of TensorFlow
  print(tf.__versions__)
  
def scalar(x):
  #Prints out some details about a Scalar
  print('This is a Scalar. A Scalar is a 0-Dimensional Tensor')
  scalar = tf.constant(x)
  scalar
  print('Notice the number of dimensions of the scalar when we call the "ndim" function against it: ' + scalar.ndim)


