import os
print(os.getcwd())
os.chdir(os.getcwd())
original = input("Text to encrypt?\n")

import pandas as pd
def generate_keys(keyFile):
    keys={}
    df=pd.read_csv(keyFile)
    df['Key1']=df['Key1'].astype(str)
    df['Character']=df['Character'].astype(str)
    df['Key']=''
    for index, row in df.iterrows():
        actualKey=''
        for i in range(len(row['Character'])):
            actualKey+=row['Character'][i]
        df.loc[index,'Key']=actualKey
    keys=pd.Series(df['Key1'].values,index=df['Character']).to_dict()
    return keys


def encrypt_string(keyFile,stringToEncrypt):
    encodedString=''
    keys=generate_keys(keyFile)
    for j in stringToEncrypt:
        value = [i for i in keys if keys[i]==j]
        encodedString+=''.join(value)
    return encodedString

print(encrypt_string("EncodedKey.csv",original))