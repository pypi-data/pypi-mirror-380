import re
from spacy.language import Language, Doc
import spacy

UPPER_START = re.compile(r"^[A-ZÄÖÜ]")

from spacy.symbols import ORTH

ABBREVS = ["z.B.", "u.a.", "d.h.", "bzw.", "usw.", "Nr.", "Dr.", "Prof.", "etc."]

import spacy
from spacy.tokens import Doc

nlp = spacy.load("de_core_news_md")

# Rule-based Sentencizer mit harten Boundaries
if "sentencizer" not in nlp.pipe_names:
    nlp.add_pipe("sentencizer", first=True, config={
        "punct_chars": [".", "!", "?", "…"],  # Ellipse einschließen
    })


for abbr in ABBREVS:
    nlp.tokenizer.add_special_case(abbr, [{ORTH: abbr}])


@Language.component("de_sentence_refiner")
def de_sentence_refiner(doc: Doc) -> Doc:
    # Wir arbeiten auf vorhandenen .is_sent_start-Flags und ergänzen/korregieren
    for i, token in enumerate(doc[:-1]):
        # Candidate: ":" oder ";" → möglicher neuer Satz
        if token.text in {":", ";"}:
            j = i + 1
            # Überspringe nachfolgende Satzzeichen/Leerstellen
            while j < len(doc) and (doc[j].is_punct and doc[j].text not in {'"', "„", "“", "‚", "’"}):
                j += 1
            if j >= len(doc):
                continue

            nxt = doc[j]
            # Qualifikation: Großbuchstabe, öffnendes Anführungszeichen, oder Pron/Det als Start
            qualifies = (
                    UPPER_START.match(nxt.text)
                    or nxt.text in {'"', "„", "‚"}
                    or nxt.pos_ in {"PRON", "DET"}
            )
            if qualifies:
                doc[j].is_sent_start = True

        # Keine Satzgrenze nach typischen Abkürzungen
        if token.text.endswith(".") and token.whitespace_ and i > 0:
            prev_text = doc[i-1].text
            window_text = (prev_text + token.text).lower()
            if any(window_text.endswith(ab.lower()) for ab in ABBREVS):
                # Nächster Token darf nicht als Satzstart markiert sein
                if i + 1 < len(doc):
                    doc[i+1].is_sent_start = False

        # Keine Grenze bei Dezimalzahlen/Datumsformaten (einfacher Heuristik-Check)
        if token.text == "." and i > 0 and i + 1 < len(doc):
            if doc[i-1].like_num and doc[i+1].like_num:
                doc[i+1].is_sent_start = False

        # Zitatanfang nach Punkt/Fragezeichen/Ausrufezeichen
        if token.text in {".", "!", "?", "…"} and i + 1 < len(doc):
            if doc[i+1].text in {'"', "„", "‚"} and i + 2 < len(doc):
                doc[i+2].is_sent_start = True

    return doc



nlp.add_pipe("de_sentence_refiner", after="sentencizer")


examples = [
    "Ich glaube, dass er kommt, obwohl er krank ist, und wir gehen trotzdem ins Kino.",
    "Wir werden das so tun und im Anschluss ausgehen.",
    "Beschreibung zu X: Das ist ein Buchstabe.",
    "Wie kann das passieren und wie geht es weiter?",
    "Benötigt werden Äpfel und Birnen.",
    "Erstelle eine Liste von a, b und c und kehre zurück.",
    "Das betrifft z.B. Äpfel, Birnen usw. Außerdem gilt d.h. folgendes.",
    "Die Zahl ist 3.14. Das Datum ist 12.03.2025. Und: Jetzt geht’s los!",
    "Wir lesen, rechnen und schreiben und dass obwohl wir keine Lust haben.",
    "Wir lesen, rechnen und schreiben und lassen es uns gut gehen."

]

for text in examples:
    doc = nlp(text)
    print("\nText:", text)
    print("Sätze:")
    for sent in doc.sents:
        print("-", sent.text.strip())
