import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd  

# appl  "Unnamed: 0", "status", "opportunity_id", "favourite", "interviewed", "an_status", "experience_start_date", "experience_end_date", "matched_or_rejected_at", "paid_at"
# oppt "Unnamed: 0","opportunity_id", "created_at", "applications_close_date", "openings", "earliest_start_date", "latest_end_date", "duration_min", "programme_id", "name_region", "name_entity", "opp_background_req", "opp_language_req", "opp_skill_req", "opp_background_pref", "opp_language_pref", "opp_skill_pref", "favourites_count", "opportunity_applications_count", "status", "matched_or_rejected_at", "experience_start_date", "experience_end_date"
df_appl = pd.read_csv("opportunity_applications_iba_challenge.csv")
df_appl = pd.read_csv("opportunity_applications_iba_challenge.csv", usecols = [1,2], names = ["appl_status", "oppt_id"])
df_oppl = pd.read_csv("opportunity_iba_challenge.csv")
df_oppl = pd.read_csv("opportunity_iba_challenge.csv")
df_bgr = pd.read_csv("Cantonese3.csv", usecols = [1])
df_lgg = pd.read_csv("x1.csv",usecols = [1])
# extract data
asia = df_oppt.loc[df_oppt['name_region'] == 'Asia Pacific']
df_bgr_spl= df_bgr['opp_background_req'].str.split(',', expand=True)

arr_lgg_req = np.array(df_lgg_req)
for i in range(707273):
    stack = []
    for j in range(17):
        if arr_lgg_req[i][j] not in stack:
            stack.append(arr_lgg_req[i][j])
    for j in range(17):
        arr_lgg_req[i][j] = np.nan
    for k in range(len(stack)):
        arr_lgg_req[i][k] = stack[k]
df_lgg_req = pd.DataFrame(arr_lgg_req)
df_lgg_req = df_lgg_req[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]]  


c0 = pd.DataFrame(df_lgg_req[0].value_counts())
c1 = pd.DataFrame(df_lgg_req[1].value_counts())
c2 = pd.DataFrame(df_lgg_req[2].value_counts())
c3 = pd.DataFrame(df_lgg_req[3].value_counts())
c4 = pd.DataFrame(df_lgg_req[4].value_counts())
c5 = pd.DataFrame(df_lgg_req[5].value_counts())
c6 = pd.DataFrame(df_lgg_req[6].value_counts())
c7 = pd.DataFrame(df_lgg_req[7].value_counts())
c8 = pd.DataFrame(df_lgg_req[8].value_counts())
c9 = pd.DataFrame(df_lgg_req[9].value_counts())
c10 = pd.DataFrame(df_lgg_req[10].value_counts())
c11 = pd.DataFrame(df_lgg_req[11].value_counts())
c12 = pd.DataFrame(df_lgg_req[12].value_counts())
c13 = pd.DataFrame(df_lgg_req[13].value_counts())
c14 = pd.DataFrame(df_lgg_req[14].value_counts())

result = pd.merge(c0, c1, left_index = True, right_index = True, how = 'outer')
result = pd.merge(result, c14, left_index = True, right_index = True, how = 'outer')

arr_rst = np.array(result)
for i in range(53):
    frq = []
    ttl = 0
    for j in range(15):
        ttl += arr_rst[i][j]
    frq[i] = ttl 

df_lgg_req = pd.DataFrame(arr_lgg_req)
        



# check data
date = asia['applications_close_date'].tolist()
for i, a in enumerate(date):
    if (a != np.nan & (a < '2005-01-01 00:00:00') | (a > '2020-01-01 00:00:00')):
        print(a)
 
asia['openings'].describe()
df_appl.dtypes
bg_req.describe()

# count of missing values
count_nan = len(df_opp) - df_opp.count()

# drop duplicate columns
asia = asia.drop_duplicates(subset = ['opportunity_id'], keep ='first')
# drop columns
asia = asia.drop(columns = 'name_region' )

# add indices 
df_appl = df_appl.reset_index(drop = True)
df_appl['index_appl'] = df_appl.index + 1
cols = df_appl.columns.tolist()
cols = cols[-1:] + cols[:-1]
df_appl = df_appl[cols]

# clean req
col = uniq[2].tolist()
for i, a in enumerate(col):
    if a == 'Other':
        col[i] = np.nan
uniq[2] = col

col1 = uniq[0].value_counts()

# clean openings
lgg = asia['opp_language_req'].tolist()
for i, a in enumerate(openings):
    if a.contain(''):
        openings[i] = np.nan
asia['openings'] = openings

# extract null
has_null = df_opp.isnull().any(axis = 1)
df_opp['has_null'] = has_null
df_ass = df_opp.loc[df_opp['has_null'] == False]
df_ass = df_ass.drop(columns = 'has_null' )

df_ass.to_csv("ass.csv", sep=",", index = True)

# clean matched_or_rejected_at in appl
matched = df_appl['matched_or_rejected_at'].tolist() 
for i, a in enumerate(matched):
    if pd.to_datetime(a) in pd.period_range(start = '1980-01-01 00:00:00', end = '2020-01-01 00:00:00'):
        matched[i] = a
    else:
        matched[i] = np.NaN    
matched_c = []
for a in matched:
    matched_c.append(a)     
df_appl['matched_or_rejected_at'] = matched_c

# inner join
oppt_to_join = df_oppt.drop_duplicates(subset = 'opportunity_id', keep ='first')
oppt_to_join = oppt_to_join.drop(columns = ["index_oppt","matched_or_rejected_at"])
df = pd.merge(df_appl, oppt_to_join, on='opportunity_id')
df = df.drop(columns = ["experience_start_date", "experience_end_date"])
df_appl = df
df_app = df.sort_values("opportunity_id")
df["opp_background_req"].describe()
df["opp_language_req"].describe()
df["opp_skill_req"].describe()
df["opp_background_pref"].describe()
df["opp_language_pref"].describe()
df["opp_skill_pref"].describe()

#Drop the S.No column
#df = df.drop("S.No", axis = 1)

# =============================================================================
# #Truncate the Time from the date-time fields
# df = df.replace(r"[\d]{2}[:][\d]{2}[:][\d]{2}", "", regex = True)
# 
# 
# #Calculating no of weeks
# CreatedOn = df['created_at'].tolist()
# for i, a in enumerate(CreatedOn):
#    CreatedOn[i] = a.replace(" ", "")
# 
# CreatedOnDate = []
# for a in CreatedOn:
#     CreatedOnDate.append(datetime.datetime.strptime(a, '%Y-%m-%d').date())
# 
# weekslist = []
# for a in CreatedOnDate:
#     weekslist.append(int(round(((datetime.date(2019,1,12) - a).days)/7)))
#     
# df['Weeks'] = weekslist
# cols = df.columns.tolist()
# cols = cols[:3] + cols[-1:] + cols[3:-1]
# df = df[cols]
# =============================================================================


#Drop row by condition
#df = df[(df['openings'] < 5000)]
#df = df[(df['favourites_count'] < 1000)]

#Print row with condition
#X = df[df['favourites_count'] < 1000]

#FD of openings
#FD_openings = df['favourites_count'].value_counts()
#FD_openings = FD_openings.sort_index()
#FD_openings['Null'] = len(df['favourites_count']) - df['favourites_count'].count()


#Export the cleaned data
x = asia[['opp_background_req','opp_language_req','opp_skill_req','opp_background_pref','opp_language_pref','opp_skill_pref']]
result.to_csv("lgg_frq.csv", sep=",", index = True)
