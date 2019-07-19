# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:58:43 2018

@author: a-whalen
"""

import spacy

#You'll need to run python -m download en_core_web_sm from the console first
nlp = spacy.load('en_core_web_sm') 
#Either paste test data into a txt file of this name, or enter directly below
#file = open('data.txt', encoding='utf8')
#text = file.read()
#file.close()
text ="Suitable for repeated use because the products does not damage any members."

doc = nlp(text)
d = []

#Parse into sentences to break it up a little (sentence tokenizer is iffy)
for idno, sentence in enumerate(doc.sents):
    d.append({'id': idno, 'sentence':str(sentence)})
    print('Sentence {}:'.format(idno + 1), sentence)
    
#Look for subjects and associated verbs in text
for dct in d:
    for sentence in dct.values():
        subject_verb = {}  
        last_subject = ''
        for token in nlp(str(sentence)):
            print(token.text, token.pos_, token.tag_, token.dep_, token.lemma_)
            #Needs more specificity
            if token.dep_ == 'nsubj':
                subject_verb[token] = ''
                last_subject = token
            if token.pos_ == "VERB":
                if token.dep_ == 'aux' or token.dep_ == 'ROOT':
                    subject_verb[last_subject] = token

#These are the bare minimum to see results but needs more thought
singular_subjects = ['NN', 'NNP', 'this', 'it']
plural_subjects = ['NNPS', 'NNS', 'these', 'they', 'you']
singular_verbs = ['VBZ']
plural_verbs = ['VBP']

#check for non-matching case in subjects and verbs
for s, v in subject_verb.items():  
    if s and v:
        print(s.text + ': ' + v.text)
        if s.tag_ in singular_subjects or s.text.lower() in singular_subjects:
            if v.tag_ in plural_verbs:
                print("error: " + s.text + " " + v.text)
        if s.tag_ in plural_subjects or s.text.lower() in plural_subjects:
            if v.tag_ in singular_verbs:
                print("error: " + s.text + " " + v.text)


