
import pandas as pd
import numpy as np

_datafolder = './data/'

df = {}
for i in range(1,8):
    df[i] = pd.read_csv(_datafolder + 'rec_colab_users_{}.tsv'.format(i), sep='\t')

for i in range(1,8):
    print(df[i].shape)

i = 1
floor = 0.05
df_all = df[i][(df[i]['Similarity'] > floor) & (df[i]['Similarity'] < 1)]
for i in range(2,8):
    df_all = df_all.append(df[i][(df[i]['Similarity'] > floor) & (df[i]['Similarity'] < 1)])


df_all_1 = df_all.filter(['User_1','User_2','Similarity'],axis=1)
df_all_2 = df_all.filter(['User_2','User_1','Similarity'],axis=1)
df_all_2.columns = ['User_1','User_2','Similarity']

df_c = pd.concat([df_all_1,df_all_2])
df_top5 = df_c.groupby('User_1').apply(lambda dfg: dfg.nlargest(5,'Similarity')).reset_index(drop=True)

df_top5.to_csv(_datafolder + 'top5ranking.tsv', sep='\t')
