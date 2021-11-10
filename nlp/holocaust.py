import spacy

nlp = spacy.blank("en")

#ner = nlp.create_pipe("ner")
ner = nlp.add_pipe("ner", name="conc_camp_ner")
ner.add_label("CONC_CAMP")

print(nlp.pipe_names)
#nlp.to_disk("holocaust_ner")