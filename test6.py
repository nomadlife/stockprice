import tensorflow as tf

tf.enable_eager_execution()

def my_model(x):
  return tf.square(x)  # you'd likely have something more sophisticated

print(my_model(3.0)) 