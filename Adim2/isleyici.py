# -*- coding: utf-8 -*-
import pandas as pd
from numpy import nan
import numpy as np
df = pd.read_json('arsalar.json')
df = df.drop('ilanid', 1)
df = df.drop('baslik', 1)

df = df.drop('ilce', 1)


df['boyut']= df['boyut'].str.replace('.','').str.strip()
df['boyut']=pd.to_numeric(df['boyut'], errors='coerce')

df['fiyat']= df['fiyat'].str.replace('TL','').str.replace('.','').str.strip()
df['fiyat']=pd.to_numeric(df['fiyat'], errors='coerce')
df['m2fiyat']=pd.to_numeric(df['m2fiyat'], errors='coerce')
df= df.replace(0,nan)
df = df.dropna(how='any',axis=0)

#Konut arsalarının, illere göre medyanı
df_konut = df[df['imar'] == "Konut"]
group_konut = df_konut.groupby('il')['fiyat'].median()
output_konut= group_konut.to_json()
with open('konut-il.json', 'w') as f:
    f.write(output_konut)

#Python3 asagi elveda diyor
print group_konut
print "[+] " + str(group_konut.count()) + " ilin konut arsaları medyanları alındı."

print "[?] İstanbul ili ortalama arsa fiyatı: " + str(df[df.il == u'İstanbul'].mean()['fiyat'])
print "[?] İstanbul ili konut imarlı medyan arsa fiyatı: " + str(df[np.logical_and(df.il == u'İstanbul', df.imar == u'Konut')].median()['fiyat'])

