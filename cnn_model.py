import tensorflow as tf

def generate_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(filters=32, kernel_size=(3,3), strides=(1,1), activation='relu', padding='same', input_shape=(28, 28, 1)),
        tf.keras.layers.MaxPooling2D(pool_size=(2,2), strides=(2,2)),

        tf.keras.layers.Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), activation='relu', padding='same'),
        tf.keras.layers.MaxPooling2D(pool_size=(2,2), strides=(2,2)),

        tf.keras.layers.Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), activation='relu', padding='same'),
        tf.keras.layers.Flatten(),

        tf.keras.layers.Dense(units=64, activation='relu'),

        tf.keras.layers.Dense(units=10, activation='softmax')
    ])

    return model


