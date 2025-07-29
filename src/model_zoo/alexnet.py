import tensorflow as tf
from tensorflow.keras import layers, models

def get_model(input_shape=(120, 160, 1), num_outputs=6, learning_rate=0.01):
    model = models.Sequential(name="AlexNet")

    # Input Layer
    model.add(layers.Input(shape=input_shape))

    # Convolutional layers
    model.add(layers.Conv2D(96, kernel_size=11, strides=4, activation='relu'))
    model.add(layers.MaxPooling2D(pool_size=3, strides=2))
    model.add(layers.LayerNormalization())

    model.add(layers.Conv2D(256, kernel_size=5, padding='same', activation='relu'))
    model.add(layers.MaxPooling2D(pool_size=3, strides=2))
    model.add(layers.LayerNormalization())

    model.add(layers.Conv2D(384, kernel_size=3, padding='same', activation='relu'))
    model.add(layers.Conv2D(384, kernel_size=3, padding='same', activation='relu'))
    model.add(layers.Conv2D(256, kernel_size=3, padding='same', activation='relu'))
    model.add(layers.MaxPooling2D(pool_size=3, strides=2))
    model.add(layers.LayerNormalization())

    # Fully Connected layers
    model.add(layers.Flatten())
    model.add(layers.Dense(4096, activation='tanh'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(4096, activation='tanh'))
    model.add(layers.Dropout(0.5))

    # Final Output Layer
    model.add(layers.Dense(num_outputs, activation='softmax'))

    # Compile
    model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate, momentum=0.9),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    return model
