# 🎭 Emotion Classifier

An AI-powered emotion recognition system that classifies human emotions from images using deep learning (CNN).  
This project was trained on a facial expression dataset and deployed both locally and on **Hugging Face Spaces**.

---

## 🚀 Live Demo
🔗 Hugging Face Spaces: https://huggingface.co/spaces/RayNetic/Emotion-Classifier

---

## 📂 Project Structure

emotion-classifier/
│
├── model/
│ └── emotion_model.h5 # Trained CNN model
│
├── notebook/
│ └── Emotion_Classifier.ipynb # Jupyter/Colab notebook (training & evaluation)
│
├── hf_app/
│ ├── app.py # Hugging Face Streamlit app
│ ├── requirements.txt # Dependencies for Hugging Face
│ └── README.md # (Optional) app-specific readme
│
├── screenshots/ # Result screenshots
│
├── README.md # Main project readme
---

## 🧠 Model Details
- **Architecture:** Convolutional Neural Network (CNN)  
- **Frameworks:** TensorFlow / Keras  
- **Input:** Facial images  
- **Output:** One of several emotion categories (e.g., Happy, Sad, Angry, Surprise, Neutral)  

---

## 📊 Results

| Emotion | Example Prediction      |
|---------|-------------------------|
| Happy   | 😄 Detected correctly   |
| Sad     | 😢 Detected correctly   |
| Angry   | 😡 Detected correctly   |
| Neutral | 😐 Detected correctly   |

📷 **Screenshots:**  

![Training Accuracy](screenshots/training_accuracy.png)  
![Confusion Matrix](screenshots/confusion_matrix.png)  
![Sample Prediction](screenshots/sample_prediction.png)

---

## 🛠️ Installation (Local)

1. Clone the repo:
   ```bash
   git clone https://github.com/RayanAIX/emotion-classifier.git
   cd emotion-classifier
Install dependencies:

pip install -r requirements.txt


Run the app locally:

streamlit run hf_app/app.py

🌐 Deployment

GitHub Repo: https://github.com/RayanAIX/emotion-classifier

Hugging Face Spaces: https://huggingface.co/spaces/RayNetic/Emotion-Classifier

👤 Author

Muhammad Rayan Shahid

YouTube: https://www.youtube.com/@ByteBrillianceAI

LinkedIn: https://www.linkedin.com/in/muhammad-rayan-shahid

Kaggle: https://www.kaggle.com/rayanaix

GitHub: https://github.com/RayanAIX

Hugging Face: https://huggingface.co/RayNetic

Twitter/X: https://twitter.com/RayanAIX

⭐ If you like this project, don’t forget to star the repo and share!
