import os
import cv2
import numpy as np

IMG_SIZE = 64
DATASET_DIR = "Dataset"

X = []
y = []

for category in ["cats", "dogs"]:
    folder_path = os.path.join(DATASET_DIR, category)
    label = 0 if category == "cats" else 1

    for img in os.listdir(folder_path):
        img_path = os.path.join(folder_path, img)

        try:
            image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
            image = image.flatten()
            X.append(image)
            y.append(label)
        except:
            pass

X = np.array(X) / 255.0
y = np.array(y)

np.save("X.npy", X)
np.save("y.npy", y)

print("Dataset created successfully")
print("X shape:", X.shape)
print("y:", y)
