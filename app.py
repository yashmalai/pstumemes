import re
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
from flask import Flask, render_template, request

app = Flask(__name__)

tokenizer = T5Tokenizer.from_pretrained("cointegrated/rut5-base-multitask")
model = T5ForConditionalGeneration.from_pretrained("cointegrated/rut5-base-multitask")

def generate(text, **kwargs):
    inputs = tokenizer(text, return_tensors='pt')
    with torch.no_grad():
        hypotheses = model.generate(**inputs, num_beams=5, **kwargs)
    return tokenizer.decode(hypotheses[0], skip_special_tokens=True)


def split_text_into_sentences(text):
    sentence_enders = re.compile(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s')
    sentences = sentence_enders.split(text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_text', methods=['POST'])
def process_text():
    if request.method == 'POST':
        input_text = request.form['input_text']
        sentences = split_text_into_sentences(input_text)
        questions = []
        for sentence in sentences:
            ask = generate(" ask | " + sentence, max_length=32)
            questions.append(ask)
        return render_template('index.html', input_text=input_text, sentences=sentences, questions=questions)

if __name__ == '__main__':
    app.run(debug=True)