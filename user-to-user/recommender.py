import pandas as pd
import numpy as np

_datafolder = './data/'
df_apps = pd.read_csv(_datafolder  +  'apps.tsv', sep='\t')
df_apps = df_apps.drop(['ApplicationDate', 'Split'],axis='columns')

df_top5 = pd.read_csv(_datafolder + 'top5ranking.tsv', sep='\t')
rowid =0
i=0
df_recom = pd.DataFrame([], columns = ['User_Rec_To', 'User_Rec_From', 'Recommended_Job'])
for u in range(0,df_top5.shape[0]):
    user1 = df_top5.iloc[u].User_1
    user2 = df_top5.iloc[u].User_2
    apps_u1 = df_apps[df_apps['UserID'] == user1]
    apps_u2 = df_apps[df_apps['UserID'] == user2]
    left = apps_u1.merge(apps_u2, left_on='JobID',  right_on='JobID', how = 'left', suffixes=('_U1', '_U2'))
    right = apps_u1.merge(apps_u2, left_on='JobID', right_on='JobID', how = 'right', suffixes=('_U1', '_U2'))

    jtr_user1 = right[np.isnan(right.UserID_U1)].JobID
    jtr_user2 = left[np.isnan(left.UserID_U2)].JobID

    for rtu_1 in range(0,jtr_user1.shape[0]):
        row = [user1,user2,jtr_user1.iloc[rtu_1]]
        print(rowid, row)
        df_recom.loc[rowid] = row
        rowid += 1

    for rtu_2 in range(0,jtr_user2.shape[0]):
        row = [user2,user1,jtr_user2.iloc[rtu_2]]
        print(rowid,row)
        df_recom.loc[rowid] = row
        rowid += 1

    if rowid > 1000:
        df_recom.to_csv(_datafolder + 'recom_lote_{}.tsv'.format(i), sep='\t')
        df_recom = pd.DataFrame([], columns = ['User_Rec_To', 'User_Rec_From', 'Recommended_Job'])
        i += 1
        rowid = 0

df_recom.to_csv(_datafolder + 'recom_Final.tsv', sep='\t')
