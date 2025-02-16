import gradio as gr
import tensorflow as tf
import numpy as np
import pickle
import os
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the trained model
model = tf.keras.models.load_model("urdu_poetry_model.h5")

# Load tokenizer from saved file
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# Define max_sequence_length (Same as in Jupyter)
max_sequence_length = 50

# Optimized Poetry Generation Function with Download Feature
def generate_poetry(seed_text, next_words=20, temperature=0.8):
    token_list = tokenizer.texts_to_sequences([seed_text])[0]
    
    for _ in range(next_words):
        token_list = pad_sequences([token_list], maxlen=max_sequence_length - 1, padding="pre")

        predictions = model.predict(token_list, verbose=0)[0]  # Faster prediction
        predictions = np.log(predictions + 1e-7) / temperature
        exp_preds = np.exp(predictions)
        probabilities = exp_preds / np.sum(exp_preds)

        predicted = np.random.choice(len(probabilities), p=probabilities)

        output_word = next((word for word, index in tokenizer.word_index.items() if index == predicted), "")
        if not output_word:
            break  # Stop if no valid word is found

        seed_text += " " + output_word
        token_list = np.append(token_list, predicted)  # Update token list

    # Save poetry to a text file for downloading
    file_path = "generated_poetry.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(seed_text)

    return seed_text, file_path  # Returns both poetry text & downloadable file

# Gradio Interface with Better UI
with gr.Blocks() as app:
    gr.Markdown("# ✨ ShayariGenie 🧞‍♂️ – Roman Urdu Poetry Bot")
    gr.Markdown("### Generate and Download Urdu Shayari ✍️")

    with gr.Row():
        seed_input = gr.Textbox(label="Enter Your Poetry Seed", placeholder="Type a phrase like 'ishq ka dard'...")
        num_words = gr.Slider(5, 20, step=5, label="Words to Generate")
        temp = gr.Slider(0.2, 1.0, step=0.1, label="Creativity (Temperature)")

    poetry_output = gr.Textbox(label="Generated Poetry", lines=4)
    download_button = gr.File(label="Download Poetry")

    generate_button = gr.Button("🔮 Generate Shayari", variant="primary")

    generate_button.click(generate_poetry, inputs=[seed_input, num_words, temp], outputs=[poetry_output, download_button])

# Launch Gradio App with Better Layout
app.launch(share=True, inbrowser=True)
