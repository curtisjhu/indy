import tensorflow as tf
from tensorflow.keras import layers, Model
import numpy as np

class RealNVP(layers.Layer):
    def __init__(self, num_coupling_layers, input_dim, condition_dim):
        super(RealNVP, self).__init__()
        self.num_coupling_layers = num_coupling_layers
        self.input_dim = input_dim
        self.condition_dim = condition_dim
        self.coupling_layers = [self._build_coupling_layer() for _ in range(num_coupling_layers)]

    def _build_coupling_layer(self):
        # Build a single coupling layer
        input_layer = layers.Input(shape=(self.input_dim,))
        condition_layer = layers.Input(shape=(self.condition_dim,))
        x = layers.Concatenate()([input_layer, condition_layer])
        x = layers.Dense(128, activation='relu')(x)
        x = layers.Dense(128, activation='relu')(x)
        shift = layers.Dense(self.input_dim, activation=None)(x)
        scale = layers.Dense(self.input_dim, activation='tanh')(x)
        return Model([input_layer, condition_layer], [shift, scale])

    def call(self, inputs, condition, reverse=False):
        x = inputs
        log_det_jacobian = 0
        for i, coupling_layer in enumerate(self.coupling_layers):
            shift, scale = coupling_layer([x, condition])
            if reverse:
                x = (x - shift) * tf.exp(-scale)
                log_det_jacobian -= tf.reduce_sum(scale, axis=1)
            else:
                x = x * tf.exp(scale) + shift
                log_det_jacobian += tf.reduce_sum(scale, axis=1)
        return x, log_det_jacobian

class CNFModel(tf.keras.Model):
    def __init__(self, num_coupling_layers, input_dim, condition_dim):
        super(CNFModel, self).__init__()
        self.real_nvp = RealNVP(num_coupling_layers, input_dim, condition_dim)

    def call(self, inputs, condition, reverse=False):
        return self.real_nvp(inputs, condition, reverse)

# Example usage
if __name__ == "__main__":
    # Define dimensions
    input_dim = 2  # Dimension of the data
    condition_dim = 1  # Dimension of the conditional input
    num_coupling_layers = 4

    # Create the CNF model
    cnf_model = CNFModel(num_coupling_layers, input_dim, condition_dim)

    # Generate some random data
    x = tf.random.normal((100, input_dim))  # Data
    condition = tf.random.normal((100, condition_dim))  # Conditional input

    # Forward pass (data -> latent space)
    z, log_det_jacobian = cnf_model(x, condition, reverse=False)

    # Reverse pass (latent space -> data)
    x_reconstructed, _ = cnf_model(z, condition, reverse=True)

    print("Original Data:", x[:5])
    print("Latent Representation:", z[:5])
    print("Reconstructed Data:", x_reconstructed[:5])



