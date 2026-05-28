# 🫁 LungVision -ML-Based Lung Disease Detection System

## 📌 Project Overview

LungVision is a deep learning-based medical imaging system designed to detect and classify lung diseases from chest X-ray/CT scan images. The system uses a trained CNN model to predict the stage of lung disease and assist in early diagnosis.

It classifies images into:

* Normal
* Stage 1 Lung Cancer
* Stage 2 Lung Cancer
* Stage 3 Lung Cancer
* Unknown Cases

---

## 🎯 Objective

The main objective of LungVision is to support early detection of lung diseases using Machine Learning, reducing diagnosis time and improving healthcare assistance.

---

## 🚀 Features

* 🧠 ML-Based lung disease prediction using CNN model
* 📊 Multi-class classification system (5 categories)
* 📷 Image upload and real-time prediction
* ⚡ Fast Flask-based API backend
* 💡 Confidence score output for predictions
* 🏥 Medical insight-based classification system
* 🌐 Web interface for easy user interaction

---

## 🛠️ Tech Stack

* Python 🐍
* Flask 🌐
* TensorFlow / Keras 🤖
* NumPy
* Pillow (PIL)
* HTML, CSS, JavaScript
* Machine Learning / Deep Learning

---

## 📂 Project Structure

```
LUNGVISION_FINAL/
│
├── app.py / predict.py
├── lung_cancer_with_unknown_model.h5
├── templates/
│     ├── index.html
│     ├── predict.html
│
├── static/
│     ├── style.css
│     ├── script.js
│
├── Dataset/
├── diseases/
├── uploads/
├── temp/
├── binary_dataset/
├── pages/
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/RAMYASRI897/lungcancerpredictionsystem.git
cd lungcancerpredictionsystem
```

---

### 2️⃣ Install Dependencies

```bash
pip install flask tensorflow numpy pillow flask-cors
```

---

### 3️⃣ Run Application

```bash
python app.py
```

OR

```bash
python predict.py
```

---
 start debugging Index.html
### 4️⃣ Open in Browser

```
http://127.0.0.1:5000/
```


### 🔹 POST `/predict`

**Request:**

* Image file (X-ray/CT scan)

**Response:**

```json
{
  "label": "Stage 2",
  "confidence": 0.92
}
```

---
## 📈 Future Improvements

* Deploy model on cloud (AWS / Render / Azure)
* Improve accuracy with larger datasets
* Add real-time camera scan support
* Add user authentication system
* Mobile application integration

---

## 👨‍💻 Author

**Ramya Sri**
Computer science Engineer
