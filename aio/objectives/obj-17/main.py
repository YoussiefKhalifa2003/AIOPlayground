import tensorflow as tf
from tensorflow.keras import layers, models, datasets, callbacks

# 1️⃣ Load and preprocess data
(x_train, y_train), (x_test, y_test) = datasets.cifar10.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# One‑hot encode labels
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test   = tf.keras.utils.to_categorical(y_test, 10)

# 2️⃣ Define a simple CNN
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(32,32,3)),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 3️⃣ Early stopping to avoid over‑fitting
early = callbacks.EarlyStopping(monitor='val_loss', patience=3,
                                restore_best_weights=True)

# 4️⃣ Train the model
history = model.fit(x_train, y_train, epochs=20,
                    validation_split=0.2,
                    batch_size=64,
                    callbacks=[early])

# 5️⃣ Evaluate on test set
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f'Test accuracy: {test_acc:.4f}')
