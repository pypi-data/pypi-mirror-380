# python -m pip install transformers accelerate torch
# python -m pip install hf_xet
# python -m pip install huggingface_hub[hf_xet]

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from huggingface_hub import login
login("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")   # dein Token

model_name = "mistralai/Mistral-7B-Instruct-v0.2"

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_name = "mistralai/Mistral-7B-Instruct-v0.2"

tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype="auto",
    use_auth_token=True
)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

#prompt = "Markiere logische Operatoren im Satz: 'Wenn es regnet, dann bleibe ich zu Hause.'"
prompt = """
Analysiere den folgenden Satz und finde alle Wörter mit logischer Bedeutung.
Die logischen Bedeutungen sind: IF, THEN, ELSE, AND, OR, NOT.

Gib die Antwort als Liste im Format <Wort>: <Bedeutung> zurück.

Beispiel:
- Falls: IF
- oder: OR
- kein: NOT

Satz: "Wenn es regnet, dann bleibe ich zu Hause und gehe nicht raus."

"""

#prompt = "Erstelle eine Liste mit Wörter, die einem logischen Operatoren entsprechen: 'Wenn es regnet, dann bleibe ich zu Hause.'"
with open("output.txt", "w", encoding="utf-8") as f:
    result = generator(prompt, max_new_tokens=500, do_sample=False)
    f.write(result[0]["generated_text"])
