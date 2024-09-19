import tensorflow as tf

def getVersion():
  #Prints the current version of TensorFlow
  print(tf.__versions__)
  
def getScalar() -> None:
  #Prints out some details about a Scalar
  print('This is a Scalar. A Scalar is a 0-Dimensional Tensor')
  scalar = tf.constant(7)
  scalar
  print('Notice the number of dimensions of the scalar when we call the "ndim" function against it: ' + scalar.ndim)

def getVector() -> None:
  #Prints out some details about a Vector
  print('This is a Vector. A Vector is a 1-Dimensional Tensor')
  vector = tf.constant([1, 2])
  vector
  print('Notice the number of dimensions of the vector when we call the "ndim" function against it: ' + vector.ndim)

def getMatrix() -> None:
  #Prints out some details about a Vector
  print('This is a Matrix. A Matrix is a 2-Dimensional Tensor')
  matrix = tf.constant([[1, 2], [3, 4]])
  matrix
  print('Notice the number of dimensions of the matrix when we call the "ndim" function against it: ' + matrix.ndim)

def main() -> None:
  getVersion()
  getScalar()
  getVector()
  
