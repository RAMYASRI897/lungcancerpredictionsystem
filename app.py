import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models
from sklearn.metrics import classification_report, confusion_matrix

# Parameters
img_height, img_width = 128, 128
batch_size = 16
epochs = 15
dataset_path = "Dataset"

# Data Generators with Validation Split
datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_gen = datagen.flow_from_directory(
    dataset_path,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='training'
)

val_gen = datagen.flow_from_directory(
    dataset_path,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation',
    shuffle=False
)

# CNN Model Definition
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(img_height, img_width, 3)),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(5, activation='softmax')  # Now 5 classes including 'Unknown'
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Model Training
model.fit(train_gen, epochs=epochs, validation_data=val_gen)

# Evaluation with Confidence Threshold
val_gen.reset()
pred_probs = model.predict(val_gen)

confidence_threshold = 0.7
preds = []

for probs in pred_probs:
    max_prob = np.max(probs)
    if max_prob < confidence_threshold:
        preds.append(4)  # Assuming 'Unknown' is the 5th class (index 4)
    else:
        preds.append(np.argmax(probs))

true_labels = val_gen.classes
class_labels = list(val_gen.class_indices.keys())

print("\nClassification Report:")
print(classification_report(true_labels, preds, target_names=class_labels))

print("\nConfusion Matrix:")
print(confusion_matrix(true_labels, preds))

# Save the Trained Model
model.save("lung_cancer_with_unknown_model.h5")




