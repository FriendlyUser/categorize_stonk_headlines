# takes the original  data and converts it to the new format
import spacy
import pandas as pd
from utils import Categories
# import en_stonk_pipeline

df = pd.read_csv('data/company.csv')
# change the category "negative" to "useless"
df.loc[df['category'] == 'negative', 'category'] = Categories.USELESS
# 
# for positive earnings, probably mostly earnings for now
df.loc[df['category'] == 'positive', 'category'] = Categories.EARNINGS

df.to_csv('data/company_adjusted.csv', index=False)
# df['category'] = df['category'].apply(lambda x: Categories[x].value)