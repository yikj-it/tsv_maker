#%%
a=1
print(a)

#%%
import csv
from os import write
import numpy as np
import itertools
from numpy.testing._private.utils import temppath
import pandas as pd
from pandas._config.config import reset_option

lis = []
with open("inp.tsv","r",encoding="utf-8_sig") as i:

    # lis = itertools.takewhile(lambda col: col!=[],(col for col in csv.reader(i,delimiter='\t')))

    result = pd.DataFrame(np.array([]))
    res = []
    lis=[]
    writer = csv.writer(i)
    s=0
    col_name=[]

    for col in csv.reader(i,delimiter='\t'):


        if col == []:
            arr = np.array(lis)

            # 列の名前
            if col_name == []:
                col_name = arr[:,0]
                col_name = np.append(col_name,"table")

            tmp = [list(arr[:,i]) for i in range(1,arr.shape[1])]

            # ここを各リストを１行にせず多重配列の１行にまとめたい
            tmpp = pd.DataFrame(tmp)
            tmpp["table"]=[s]*(arr.shape[1]-1)
            tmpp.columns = col_name
            result = pd.concat([result,tmpp])
            res.append(tmp)
            lis=[]
            s+=1
            continue

        lis.append(col)


    # この形式でdfにすると、各順位ごとのdfになる
    # print(pd.DataFrame(res))
    # print(result)

    # このcsv自体は各テーブルごとに１行の情報になっている。
    # これでうまく加工できそう
    df = pd.DataFrame(res)
    df.to_csv("out.csv")
    result.to_csv("out_result.csv")

# %%
