# grammar-check
Check for subject/verb agreement in text with SpaCy

Created in Python 3.7.1

Non-standard dependent libraries: spacy

A simple script that uses SpaCy to check whether subjects and verbs agree in English sentences.
Doesn't work very well for text that is not complete sentences.

Example sentence in code:
"Suitable for repeated use because the products does not damage any members."
"does" is singular while "products" is plural, so the subject and verb disagree, and this will produce an error.
