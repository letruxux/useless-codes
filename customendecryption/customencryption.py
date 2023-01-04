import os
print(os.getcwd())
os.chdir(os.getcwd())
original = input("Text to encrypt?\n")

import pandas as pd
def generate_keys(keyFile):
    keys={}
    df=pd.read_csv(keyFile)
    df['Character']=df['Character'].astype(str)
    df['Key1']=df['Key1'].astype(str)
    df['Key']=''
    for index, row in df.iterrows():
        actualKey=''
        for i in range(len(row['Key1'])):
            actualKey+=row['Key1'][i]
        df.loc[index,'Key']=actualKey
    keys=pd.Series(df['Character'].values,index=df['Key']).to_dict()
    return keys


def encrypt_string(keyFile,stringToEncrypt):
    encodedString=''
    keys=generate_keys(keyFile)
    for j in stringToEncrypt:
        value = [i for i in keys if keys[i]==j]
        encodedString+=''.join(value)
    return encodedString

print(encrypt_string("EncodedKey.csv",original))