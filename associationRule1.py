import numpy as np  
import pandas as pd  

df_opp = pd.read_csv("lgg.csv")

# drop duplicate columns
df_opp = df_opp.drop_duplicates(subset = ['opportunity_id'], keep ='first')

# drop columns
df_opp = df_opp.drop(columns = ['Unnamed: 0','applications_close_date','earliest_start_date','latest_end_date','matched_or_rejected_at','experience_start_date','experience_end_date','openings','duration_min','favourites_count','opportunity_applications_count'])
df_opp = df_opp.loc[df_opp['created_at'] >= '2009-01-01 00:00:00']

df_app = pd.read_csv("opportunity_applications_iba_challenge.csv", usecols = [1, 2])
df = df_app.merge(df_opp, left_on = 'opportunity_id', right_on = 'opportunity_id', how = 'left')

df_asi = df.loc[df['name_region'] == 'Asia Pacific']
df_asi_ent = df_asi.loc[df_asi['programme_id'] == 'Global Entrepreneur']

count_nan = len(df_asi_ent) - df_asi_ent.count()


df_skp= df_asi_ent['opp_skill_pref'].str.split(',', expand=True)
describe = df_skp.describe()
df_asi_ent['skp_1'] = df_skp[0]
df_asi_ent['skp_2'] = df_skp[1]

df_asi_ent = df_asi_ent.drop(columns = ['opportunity_id','created_at','name_region','opp_background_req','opp_language_req','opp_skill_req','opp_background_pref','opp_language_pref','opp_skill_pref', 'programme_id'])
df_asi_ent = df_asi_ent.drop(columns = ['programme_id'])



from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori 
from mlxtend.frequent_patterns import association_rules
data = df_asi_ent

records = []  
for i in range(data.shape[0]):  
    records.append([str(data.values[i,j]) for j in range(data.shape[1])])

te = TransactionEncoder()
te_ary = te.fit(records).transform(records)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support = 0.009, use_colnames=True)

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.2)
result = rules[(rules['consequents'] == {'rejected'}) & (rules['confidence'] > 0.5)]













