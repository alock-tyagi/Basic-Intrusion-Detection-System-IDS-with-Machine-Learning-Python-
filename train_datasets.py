import tensorflow as tf
from preprocess import preprocess

def train_dl():
    X = preprocess()
    y = tf.keras.utils.to_categorical(
        [0 if i % 10 else 1 for i in range(len(X))], 2
    )

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dense(2, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(X, y, epochs=10)
    model.save("models/deep_ids_model.h5")

if __name__ == "__main__":
    train_dl()
