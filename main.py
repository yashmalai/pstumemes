import re
import random
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer, pipeline
tokenizer = T5Tokenizer.from_pretrained("cointegrated/rut5-base-multitask")
model = T5ForConditionalGeneration.from_pretrained("cointegrated/rut5-base-multitask")

qa_model = pipeline("question-answering", "timpal0l/mdeberta-v3-base-squad2")
arr = []

def generate(text, **kwargs):
    inputs = tokenizer(text, return_tensors='pt')
    with torch.no_grad():
        hypotheses = model.generate(**inputs, num_beams=5, **kwargs)  # type: ignore
    return tokenizer.decode(hypotheses[0], skip_special_tokens=True)


def split_text_into_sentences(text):
    sentence_enders = re.compile(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s')
    sentences = sentence_enders.split(text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences

text = """
Кабели и держатели электрода и массы влияют на производительность, удобство и безопасность вашей работы. """#Как правило, они поставляются в комплекте со сварочником, но выбрав более качественные аксессуары вы получите лучший результат, даже с аппаратом начального уровня. Профессионалы рекомендуют сварочный кабель с медной токопроводящей жилой, оплеткой высокой гибкости и надежной изоляцией. Электрододержатель должен иметь качественную изоляцию, не нагреваться при использовании, работать без больших усилий, удобно крепиться под разными углами. Зажим на массу или клемму заземления нужно выбирать с учетом максимального рабочего тока сварочного аппарата. При этом угла раскрытия должно хватать для крепления к деталям различной толщины, а усилия сжатия – для надежного контакта с заготовкой.
#"""

sentences = split_text_into_sentences(text)
for sentence in sentences:
    #modified = sentence + "" + str(random.random()) + ""
    ask = generate(" ask | " + sentence, max_length=64)
    print(ask)
    #print(qa_model(question = ask, context = sentence)) # type: ignore

    arr.append(qa_model(question = ask, context = sentence)) # type: ignore
    #print(generate(" comprehend | " + sentence + "Вопрос: " + text, max_length=32), "\n")
    #print("\n")
    print(arr[0])
    
