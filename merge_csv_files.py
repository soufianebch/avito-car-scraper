from variables import *
import pandas as pd
import glob
import os
import csv

print('Concatinating files..')
files = os.path.join("output", "avito_car_dataset*.csv")
files = glob.glob(files)
df = pd.read_csv(files[0],encoding="latin-1")
for i in range(1,len(files)):
    try:
        df = pd.concat([df,pd.read_csv(files[i],encoding="latin-1")], ignore_index=True)
    except:
        pass

try:
    df.drop('Id', inplace=True, axis=1)
    df.drop('Unnamed: 0', inplace=True, axis=1)
except:
    pass

try:
    # df.sort_values("Marque", inplace=True)
    l1 = len(df)
    df.drop_duplicates(subset ="Lien",keep = False, inplace = True)
    print(l1-len(df),'duplicated row has been removed!')
    print('result: ',len(df),'row')
except:
    pass

df.to_csv(r'output\avito_car_dataset_ALL.csv', index=True, mode = 'w', header=True, encoding="latin-1")
print('Done!')
