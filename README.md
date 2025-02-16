# Shayari-Genie
An AI-powered Roman Urdu Poetry Generator. Trained on deep learning (GRU) and deployed with Gradio for real-time poetry generation!

## Live Demo  
Try it out on Hugging Face Spaces:  
https://huggingface.co/spaces/SidraMalik/shayari-genie

---

## Features
- Generate Roman Urdu Poetry using AI  
- Adjust creativity (Temperature scaling)  
- Download generated poetry as a text file  
- User-friendly interface powered by Gradio  

---

## How It Works
1. Enter a starting phrase (e.g., "ishq ka dard")  
2. Select the number of words to generate  
3. Adjust creativity for randomness  
4. Click "Generate" to see AI-generated poetry  
5. Download the poetry as a `.txt` file  

---
## Here's how the interface looks like 

![image](https://github.com/user-attachments/assets/d917c12c-b06c-4773-b072-d5702d6ec3f3)

## Installation & Setup  

### 1. Clone the following Repository

git clone https://github.com/SidrahMalik/Shayari-Genie.git

### Install dependencies

pip install -r requirements.txt

### Download the Trained Model & Tokenizer

Since GitHub does not support large files, download the trained model separately

tokenizer.pkl (Saved Tokenizer) → Already included in this repo

Once downloaded, place urdu_poetry_model.h5 inside the project folder.

### Run the App

python app.py


