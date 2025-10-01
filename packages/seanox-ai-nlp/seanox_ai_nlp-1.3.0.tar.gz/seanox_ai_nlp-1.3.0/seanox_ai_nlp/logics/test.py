import spacy

nlp = spacy.load("de_core_news_md")
text = """
Ich glaube, dass er kommt, obwohl er krank ist, und wir gehen trotzdem ins Kino.
Wir werden das so und so tun und im Anschluss ausgehen.
Beschreibung zu X: Das ist ein Buchstabe. 
Wie kann das passieren und wie geht es weiter?
Benötigt werden Äpfel und Birnen.
Erstelle eine Liste von a, b und c und kehre zurück. 
Wir lesen, rechnen und schreiben und dass obwohl wir keine Lust haben. 
Wir lesen, rechnen und schreiben und lassen es uns gut gehen. 
Das betrifft z.B. Äpfel, Birnen usw. Außerdem gilt d.h. folgendes.
Die Zahl ist 3.14. Das Datum ist 12.03.2025. Und: Jetzt geht’s los!
"""
doc = nlp(text.strip())

boundaries = []

for sent in doc.sents:
#    for token in sent:
#        print("-", token, token.dep_, token.pos_)

    print("\nSatz:", sent.text)


    clauses = []
    start = sent.start
    for i, token in enumerate(sent):
        print("-", token, token.dep_, token.pos_)
        # Regel: punct + (cd oder cp) → neuer Teilsatz
   #     if token.dep_ in ("cd", "cp") and i > 0 and sent[i-1].dep_ == "punct":
   #         span = doc[start:sent[i].i]
   #         if span.text.strip():
   #             clauses.append(span.text.strip())
   #         start = sent[i].i
    # Rest anhängen
   # span = doc[start:sent.end]
   # if span.text.strip():
   #     clauses.append(span.text.strip())

   # print("Gefundene Teilsätze:")
   # for c in clauses:
   #     print("-", c)

    # Hauptsatz (ROOT + Subjekt)
#    root = [t for t in sent if t.dep_ == "ROOT"][0]
#    subj = [t for t in root.lefts if t.dep_ in ("nsubj", "nsubj:pass")]#

#    print(root, subj)


 #   if subj:
 #       span = doc[subj[0].i : root.i+1]
 #       boundaries.append((span.start_char, span.end_char, span.text))

    # Teilsätze
#    for token in sent:
#        if token.dep_ in ("ccomp", "advcl", "relcl", "conj"):
#            span = doc[token.left_edge.i : token.right_edge.i+1]
#            boundaries.append((span.start_char, span.end_char, span.text))
#
#print("Gefundene Grenzen:")
#for start, end, text in boundaries:
#    print(f"[{start}:{end}] -> {text}")
