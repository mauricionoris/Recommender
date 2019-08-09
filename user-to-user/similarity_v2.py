import pandas as pd
import numpy as np

_datafolder = '~/repo/Recommender/data/'
mtx = pd.read_csv(_datafolder  +  'MatchPart.tsv', sep='\t')
mtxx = mtx.groupby(by=['CandidatoId'], as_index=False)['VagaId'].count()
mtxx.columns = ['CandidatoId','Apps']

rowid =0
batch =0

def setOutput():
    df = pd.DataFrame([], columns = ['Cnd_1', 'Cnd_2', 'Apps_1', 'Apps_2', 'Joint_Apps', 'Similarity'])
    return df;

def checkIfCompared(u1,u2):
    if len(df[(df['Cnd_1'] == u1) & df['Cnd_2'] == u2)] > 0:
        return True;
    if len(df[(df['Cnd_2'] == u1) & df['Cnd_1'] == u2)] > 0:
        return True;
    return False

def addSim(apps_u1, apps_u2):

    if len(apps_u1) == 1 and len(apps_u2) == 1:
        return;

    inner = apps_u1.merge(apps_u2, left_on='VagaId', right_on='VagaId', how = 'inner', suffixes=('_U1', '_U2'))
    union = apps_u1.merge(apps_u2, left_on='VagaId', right_on='VagaId', how = 'outer', suffixes=('_U1', '_U2'))

    s = (inner.shape[0] / union.shape[0])
    row = [user1['CandidatoId'],user2['CandidatoId'],user1['Apps'],user2['Apps'],inner.shape[0], s]
    print(rowid, row)
    df.loc[rowid] = row
    rowid += 1
    return;

def dump(rowid, n):
    if rowid%n == 0 :
        print('Dumping a slice of output_{}'.format(batch))
        df.loc[batch,n].to_csv(_datafolder + '/output/rec_colab_users_from_{}_to_{}.tsv'.format(batch,n), sep='\t')
        batch = n
    return;

for u1 in range(0,mtxx.shape[0]-1):
    user1 = mtxx.iloc[u1]
    apps_u1 = mtx[mtx['CandidatoId'] == user1['CandidatoId']]
    apps_j = set();
    for j in range(0,apps_u1.shape[0]):
        apps_j.update(mtx[mtx['VagaId'] == apps_u1.iloc[j].VagaId)]['CandidatoId'].values.tolist())

    for u2 in apps_j:
        user2 = mtxx[mtxx['CandidatoId'] == u2]
        apps_u2 = mtx[mtx['CandidatoId'] == user2['CandidatoId']]
        if checkIfCompared(user1['CandidatoId'], user2['CandidatoId']) == False:
            addSim(apps_u1, apps_u2)
            dump(rowid,1000)
