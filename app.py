import gradio as gr
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array

# Load model
model = tf.keras.models.load_model("emotion_model.h5")

# Emotion labels (update if your training used different classes)
emotion_labels = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]

def predict_emotion(image):
    # Resize to 48x48 and convert to grayscale
    img = image.resize((48, 48)).convert("L")
    img = img_to_array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    # Predict
    predictions = model.predict(img)[0]
    label = emotion_labels[np.argmax(predictions)]
    confidence = round(100 * np.max(predictions), 2)

    return {label: confidence}

# Gradio interface with webcam option
iface = gr.Interface(
    fn=predict_emotion,
    inputs=[gr.Image(type="pil", sources=["upload", "webcam"], label="Upload or Use Webcam")],
    outputs=gr.Label(num_top_classes=3, label="Predicted Emotion"),
    title="Emotion Classifier",
    description="Upload a face image OR use your webcam to detect emotions in real time."
)

iface.launch()
