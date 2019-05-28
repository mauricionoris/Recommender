import nltk
import collections
import string

table = collections.defaultdict(lambda: None)
table.update({
    ord('é'):'e',
    ord('ô'):'o',
    ord(' '):' ',
    ord('\N{NO-BREAK SPACE}'): ' ',
    ord('\N{EN SPACE}'): ' ',
    ord('\N{EM SPACE}'): ' ',
    ord('\N{THREE-PER-EM SPACE}'): ' ',
    ord('\N{FOUR-PER-EM SPACE}'): ' ',
    ord('\N{SIX-PER-EM SPACE}'): ' ',
    ord('\N{FIGURE SPACE}'): ' ',
    ord('\N{PUNCTUATION SPACE}'): ' ',
    ord('\N{THIN SPACE}'): ' ',
    ord('\N{HAIR SPACE}'): ' ',
    ord('\N{ZERO WIDTH SPACE}'): ' ',
    ord('\N{NARROW NO-BREAK SPACE}'): ' ',
    ord('\N{MEDIUM MATHEMATICAL SPACE}'): ' ',
    ord('\N{IDEOGRAPHIC SPACE}'): ' ',
    ord('\N{IDEOGRAPHIC HALF FILL SPACE}'): ' ',
    ord('\N{ZERO WIDTH NO-BREAK SPACE}'): ' ',
    ord('\N{TAG SPACE}'): ' ',
    })
table.update(dict(zip(map(ord,string.ascii_uppercase), string.ascii_lowercase)))
table.update(dict(zip(map(ord,string.ascii_lowercase), string.ascii_lowercase)))

stopwords = nltk.corpus.stopwords.words('portuguese')
stopwords.extend(['aquel', 'aquil', 'ate', 'del', 'entr', 'er', 'ess', 'est', 'estej'
               , 'estev', 'estiv', 'estivess', 'estv', 'fom', 'form', 'foss', 'h', 'haj'
               , 'hav', 'ho', 'houv', 'houvess', 'iss', 'ist', 'j', 'mesm', 'minh', 'muit'
               , 'noss', 'ns', 'par', 'pel', 'qu', 's', 'sej', 'ser', 'so', 'som', 'tamb'
               , 'tenh', 'ter', 'tev', 'tinh', 'tiv', 'tivess', 'tnh', 'vo', 'voc'
               , 'es', 'estives', 'fos', 'houves', 'is', 'nos', 'tives','fo','no'
               ])

def tokenize_and_steem(text):
    tokens = nltk.word_tokenize(strip(text.lower()))
    stems = []
    for item in tokens:
        stems.append(nltk.stem.RSLPStemmer().stem(item))
    return stems

def strip(text):
    return text.translate(table)
