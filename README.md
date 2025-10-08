# 🎭 Emotion Classifier AI

---

## 🧠 Overview
The **Emotion Classifier AI** is a deep learning project that detects human emotions in real time using facial expressions.  
By leveraging **Convolutional Neural Networks (CNNs)** and **OpenCV**, this model can recognize various emotions such as *Happy, Sad, Angry, Surprise, Neutral,* and more — bridging the gap between artificial intelligence and human empathy.

---

## 🚀 Features
- 🎥 Real-time emotion detection via webcam  
- 🧩 CNN-based deep learning model (`emotion_model.h5`)  
- 📊 Trained on the FER-2013 dataset  
- 🌐 Deployed on Hugging Face for public interaction  
- 💻 Streamlit-ready for local or web deployment  

---

## 🧩 Tech Stack
- **Language:** Python  
- **Libraries:** TensorFlow, Keras, OpenCV, NumPy  
- **Frameworks:** Streamlit / Hugging Face Spaces  
- **Dataset:** FER-2013 (Facial Expression Recognition Dataset)

---

## 🧠 Model Architecture
- Input: 48x48 grayscale facial images  
- Layers: 4 convolutional + pooling layers, followed by dense layers  
- Activation: ReLU + Softmax  
- Output: 7 emotion classes  


---

## 🔴 Live Demo
Try it directly here 👇  
👉 **[Hugging Face Demo](https://huggingface.co/spaces/RayanAIX/emotion-classifier)**  

---

## 📂 Repository Structure
```
Emotion-Classifier/
 ┣ 📁 dataset/
 ┣ 📁 models/
 ┃ ┗ emotion_model.h5
 ┣ 📁 images/
 ┣ 📜 app.py
 ┣ 📜 requirements.txt
 ┣ 📜 README.md
 ┗ 📜 emotion_detector.py
```

---

## ⚙️ Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/RayanAIX/emotion-classifier.git
cd emotion-classifier
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run Locally (Streamlit App)
```bash
streamlit run app.py
```

### 4️⃣ Or Run in Colab
Simply upload the files and run the notebook cell-by-cell.

---

## 📈 Results
| Emotion | Accuracy |
|----------|-----------|
| Happy 😄 | 92% |
| Sad 😢 | 88% |
| Angry 😠 | 87% |
| Surprise 😮 | 91% |
| Neutral 😐 | 90% |

✅ Overall Accuracy: **~90%**

---

## 🔮 Future Improvements
- Add multi-face detection in the same frame  
- Train on more diverse datasets for better generalization  
- Improve lighting & background robustness  
- Add real-time emotion tracking analytics  

---

## 💡 Key Learnings
Building this project taught me that *AI might not “feel” emotions, but it can learn to recognize them — a crucial step toward empathetic human-AI interaction.*

---

## 👨‍💻 Author

**Muhammad Rayan Shahid**  
AI & ML Engineer | Deep Learning Enthusiast  

🌐 **Connect with me:**  
- [🌍 Portfolio](https://rayanai.tech)  
- [💼 LinkedIn](https://www.linkedin.com/in/muhammadrayanshahid/)  
- [🐙 GitHub](https://github.com/RayanAIX)  
- [📊 Kaggle](https://www.kaggle.com/muhammadrayanshahid)  
- [🤗 Hugging Face](https://huggingface.co/RayanAIX)  
- [🎥 YouTube - ByteBrilliance AI](https://www.youtube.com/@ByteBrillianceAI)

---

## 🏷️ License
This project is licensed under the **MIT License** — you’re free to use, modify, and distribute it for educational and personal purposes.

---

⭐ **If you like this project, don’t forget to star the repo!**  
Your support motivates me to build more open-source AI projects 🚀
