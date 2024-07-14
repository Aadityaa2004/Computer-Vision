import tensorflow as tf
import numpy as np
from tensorflow.keras.layers import Normalization

# tensor_zero_d = tf.constant(4) # 0D array

# tensor_one_d = tf.constant([4, 5, 1], dtype=tf.float32) # 1D array
# casted_tensor_one_d = tf.cast(tensor_one_d, dtype=tf.int16) # Cast tensor to int16
# array = np.array([4, 5, 1], dtype=np.float32) # Numpy array
# converted_tensor = tf.convert_to_tensor(array, dtype=tf.float32) # Convert numpy array to tensor

# tensor_two_d = tf.constant([[4, 5, 1], [3, 2, 7]]) # 2D array
# tensor_three_d = tf.constant([[[4, 5, 1], [3, 2, 7]], [[4, 5, 1], [3, 2, 7]]]) # 3D array
# tensor_four_d = tf.constant([[[[4, 5, 1], [3, 2, 7]], [[4, 5, 1], [3, 2, 7]]], [[[4, 5, 1], [3, 2, 7]], [[4, 5, 1], [3, 2, 7]]]]) # 4D array

# tensor_bool = tf.constant([True, False, True]) # Boolean tensor
# tensor_string = tf.constant("Hello, TensorFlow!") # String tensor

# eye_tensor = tf.eye(
#     num_rows=3,
#       num_columns=3, 
#         dtype=tf.float32 # Identity matrix
# )
 
# print(eye_tensor)

normalization = Normalization() # Normalization layer