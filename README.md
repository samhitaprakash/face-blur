# Face Blur Tool 😷📸

A real-time face anonymization app built with **OpenCV** and **Streamlit**, allowing users to blur or pixelate detected faces from webcam input with a toggle switch.

## 🎯 Project Overview

This tool offers a simple interface to protect identity during live video streaming by applying real-time face anonymization. It uses **OpenCV** for face detection and **BytesIO** for efficient in-memory image handling.

The app runs on **Streamlit**, making it easy to deploy and interact with, even without technical experience.

---

## 🔍 Features

- Real-time face detection from webcam feed
- Toggle between **blur** and **pixelation** modes
- In-memory video frame handling with `BytesIO` for smoother performance
- Simple and fast GUI using Streamlit
- Capture and download snapshot of blurred/pixelated frame

---

## 🛠️ Tech Stack

- Python
- OpenCV
- Streamlit
- PIL (Pillow)
- BytesIO
- NumPy

---

## 🚀 How to Run Locally

1. Clone this repo:
   ```bash
   git clone https://github.com/samhitaprakash/face-blur.git
   cd face-blur
   pip install -r requirements.txt
   streamlit run app.py


Project Structure

├── app.py                  # Streamlit frontend and backend logic
├── utils/                  # Helper functions (if any)
├── models/                 # Haarcascade or detection model file
├── requirements.txt        # List of required Python packages
├── README.md               # This file
📸 Sample Use Case
Blur faces in video calls or recordings

Create anonymized content for privacy-conscious users

Educational tool for face detection and real-time processing

🌐 Deployment
Deployed on Streamlit Cloud
🔗 Live Demo

✨ Author
Built by Samhita Prakash


   

