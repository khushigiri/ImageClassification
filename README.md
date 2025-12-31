# Cats vs Dogs Image Classification using SVM

This project demonstrates image classification using a Support Vector Machine (SVM)
on a custom-built dataset of cat and dog images.

## Dataset
- Custom dataset with manually collected images
- 3 cat images and 3 dog images

## Techniques Used
- Image preprocessing (grayscale, resize, normalization)
- Feature extraction using pixel flattening
- Classification using SVM (Scikit-learn)

## How to Run
1. Install dependencies  
   pip install -r requirements.txt

2. Create dataset  
   python create_dataset.py

3. Train model  
   python svm_model.py
