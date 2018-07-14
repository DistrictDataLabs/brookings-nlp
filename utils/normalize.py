#!/usr/bin/env python 
# Contains functions for normalizing text 

import unicodedata

from nltk.corpus import stopwords 
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.base import BaseEstimator, TransformerMixin


class TextNormalizer(BaseEstimator, TransformerMixin):

    def __init__(self, language='english'):
        self.stopwords = frozenset(stopwords.words(language))
        self.lemmatizer = WordNetLemmatizer() 

    def is_punct(self, token):
        return all(
            unicodedata.category(char).startswith('P') for char in token 
        )

    def is_stopword(self, token):
        return token.lower() in self.stopwords 

    def lemmatize(self, token, pos_tag):
        tag = {
            'N': wn.NOUN, 
            'V': wn.VERB, 
            'R': wn.ADV,
            'J': wn.ADJ
        }.get(pos_tag[0], wn.NOUN)

        return self.lemmatizer.lemmatize(token, tag) 

    def normalize(self, document):
        return [
            self.lemmatize(token, tag).lower()
            for paragraph in document 
            for sentence in paragraph 
            for (token, tag) in sentence 
            if not self.is_punct(token) and not self.is_stopword(token) 
        ]

    def fit(self, X, y=None):
        return self 

    def transform(self, documents):
        for document in documents:
            yield self.normalize(document)

    def __call__(self, documents):
        return self.transform(documents)


normalize_text = TextNormalizer() 
