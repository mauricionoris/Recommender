import pandas as pd
import numpy as np

_datafolder = '~/repo/Recommender/data/'

mp = pd.read_json(_datafolder  +  './MatchPart.json')[['CandidatoId','EmpresaId','VagaId']] #StatusList
mp = mp[pd.isna(mp.EmpresaId) != True ]
mp = mp[mp.EmpresaId != 'undefined' ]
mp = mp[mp['CandidatoId'].isnull() == False]
mp = mp[mp.CandidatoId != '']
mp.to_csv(_datafolder  +  'MatchPart.tsv', sep='\t')
