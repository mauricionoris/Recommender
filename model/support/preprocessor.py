
import textsupport
from sklearn.feature_extraction.text import TfidfVectorizer

parameters = {
    "corpus":[],
}

def run():
    vectorizer = TfidfVectorizer( tokenizer=textsupport.tokenize_and_steem
                                , stop_words=textsupport.stopwords)
    X = vectorizer.fit_transform(parameters["corpus"])
    Z = vectorizer.get_feature_names();
    return X, Z
