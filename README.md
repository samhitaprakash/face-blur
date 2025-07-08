# 🛡️ FaceGuard – Real-Time Face Blur & Pixelation

Live privacy protection for your webcam feed. Blur or pixelate faces in real time using OpenCV + Streamlit. Take a screenshot, download it instantly, and switch modes on the fly.

---

## ⚡ Features

- 🔍 Face detection using Haar cascades
- 🌀 Live face blur
- 🟦 Pixelation toggle
- 📸 Screenshot capture + download
- 🖥️ Streamlit UI with real-time webcam processing

---

## 📁 Folder Structure

face-blur/
│
├── app.py # Main Streamlit app
├── requirements.txt # Python dependencies
├── README.md # You're reading it
└── models/
└── haarcascade_frontalface_default.xml # Face detection model



---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 
- Webcam
- pip

---

### 🔧 1. Clone this repo

```bash
git clone https://github.com/samhitaprakash/face-blur.git
cd face-blur

📦 2. Install requirements
bash
Copy
Edit
pip install -r requirements.txt
🧠 3. Run the app
bash
Copy
Edit
streamlit run app.py
