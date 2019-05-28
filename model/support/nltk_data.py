import nltk
#nltk.download('punkt')



#print(nltk.corpus.stopwords.words('portuguese'))

#
# import nltk
# stemmer = nltk.stem.RSLPStemmer();
# input = ['Eu','tu','Eles','caminhando','caminhar']
#
# for i in input:
#     output = stemmer.stem(i);
#     print(output)
#
#
# import nltk
# import string
# import os
#
# from sklearn.feature_extraction.text import TfidfVectorizer
# from nltk.stem.porter import PorterStemmer
#
# path = './tf-idf'
# token_dict = {}
#
#
# def tokenize(text):
#     tokens = nltk.word_tokenize(text)
#     stems = []
#     for item in tokens:
#         stems.append(PorterStemmer().stem(item))
#     return stems
#
# for dirpath, dirs, files in os.walk(path):
#     for f in files:
#         fname = os.path.join(dirpath, f)
#         print "fname=", fname
#         with open(fname) as pearl:
#             text = pearl.read()
#             token_dict[f] = text.lower().translate(None, string.punctuation)
#
# tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
# tfs = tfidf.fit_transform(token_dict.values())
#
# str = 'all great and precious things are lonely.'
# response = tfidf.transform([str])
# print response
#
# feature_names = tfidf.get_feature_names()
# for col in response.nonzero()[1]:
#     print feature_names[col], ' - ', response[0, col]
