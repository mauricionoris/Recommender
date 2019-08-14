import pandas as pd
import numpy as np
import sys

if len(sys.argv) - 1 != 2:
    raise ValueError('Incorrect parameter')

st =  int(sys.argv[1])
ed =  int(sys.argv[2])

if st >= ed:
    raise ValueError('End should be greater than start')

print (st, ed)

_datafolder = '~/repo/Recommender/data/'
mtx = pd.read_csv(_datafolder  +  'MatchPart.tsv', sep='\t')
mtxx = mtx.groupby(by=['CandidatoId'], as_index=False)['VagaId'].count()
mtxx.columns = ['CandidatoId','Apps']

rowid =0
batch =0
df = pd.DataFrame([], columns = ['Cnd_1', 'Cnd_2', 'Apps_1', 'Apps_2', 'Joint_Apps', 'Similarity'])

for u1 in range(st, ed):
    user1 = mtxx.iloc[u1]
    apps_u1 = mtx[mtx['CandidatoId'] == user1['CandidatoId']]
    for u2 in range(u1+1,mtxx.shape[0]):
        user2 = mtxx.iloc[u2]
        apps_u2 = mtx[mtx['CandidatoId'] == user2['CandidatoId']]

        inner = apps_u1.merge(apps_u2, left_on='VagaId', right_on='VagaId', how = 'inner', suffixes=('_U1', '_U2'))
        union = apps_u1.merge(apps_u2, left_on='VagaId', right_on='VagaId', how = 'outer', suffixes=('_U1', '_U2'))
        s = (inner.shape[0] / union.shape[0])
        if s < 1 and s > 0:
            row = [user1['CandidatoId'],user2['CandidatoId'],user1['Apps'],user2['Apps'],inner.shape[0], s]
            print(rowid, row)
            df.loc[rowid] = row
            rowid += 1

        if rowid%1000 == 0 and len(df) > 0:
            print('batch output_{}'.format(batch))
            df.to_csv(_datafolder + '/output/rec_{}_{}_colab_users_from_{}_to_{}.tsv'.format(st, ed, batch,rowid), sep='\t')
            batch = rowid
            df = pd.DataFrame([], columns = ['Cnd_1', 'Cnd_2', 'Apps_1', 'Apps_2', 'Joint_Apps', 'Similarity'])
