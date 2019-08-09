import pandas as pd
import numpy as np

_datafolder = '~/repo/Recommender/data/'

mp = pd.read_json(_datafolder + 'MatchPart.json')[['CandidatoId','VagaId']] #StatusList, #EmpresaId\n",
mp = mp[mp['CandidatoId'].isnull() == False]
mp = mp.drop_duplicates()
mp = mp[mp.CandidatoId != '']
#mp = mp.head(int(len(mp)*(0.05)))
mp.to_csv(_datafolder + 'MatchPart_cleaned.tsv', sep='\\t')
