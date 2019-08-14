source = [
'/media/sf_repo/data_output',
'/media/sf_repo/data_output_1',
'/media/sf_repo/data_output_2'
]

import pandas as pd
import os

dest = '~/repo/Recommender/data/similarity.tsv'
df = pd.DataFrame([], columns = ['Cnd_1', 'Cnd_2', 'Apps_1', 'Apps_2', 'Joint_Apps', 'Similarity'])

for d in source:
    files = os.listdir(d)
    print(d)
    for f in files:
        print(f)
        df_s = pd.read_csv(d + '/' + f, sep='\t')
        df = pd.concat([df,df_s])


df.reset_index(drop=True)
df_1= df[['Cnd_1','Cnd_2', 'Apps_1', 'Apps_2', 'Joint_Apps','Similarity']]
df_1 = df_1.drop_duplicates()
print(df_1.shape)
df_1.to_csv(dest, sep='\t')
