import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd  

df_app = pd.read_csv("appl2.csv", usecols = [1,2])

df_app = df_app.sort_values(by = ['opportunity_id'])

arr_out = np.zeros(shape = (334285,6))
arr_inp = np.array(df_app)

j = 0
for i in range(4678887):
    if arr_inp[i][1] == arr_inp[i+1][1]:
        arr_out[j][0] = arr_inp[i][1]
        if arr_inp[i][0] == 'accepted':
            arr_out[j][1] += 1
        elif arr_inp[i][0] == 'withdraw':
            arr_out[j][2] += 1
        elif arr_inp[i][0] == 'realized':
            arr_out[j][3] += 1
        elif arr_inp[i][0] == 'open':
            arr_out[j][4] += 1
        elif arr_inp[i][0] == 'rejected':
            arr_out[j][5] += 1
    else:
        arr_out[j][0] = arr_inp[i][1]
        if arr_inp[i][0] == 'accepted':
            arr_out[j][1] += 1
        elif arr_inp[i][0] == 'withdraw':
            arr_out[j][2] += 1
        elif arr_inp[i][0] == 'realized':
            arr_out[j][3] += 1
        elif arr_inp[i][0] == 'open':
            arr_out[j][4] += 1
        elif arr_inp[i][0] == 'rejected':
            arr_out[j][5] += 1
        j += 1

df = pd.DataFrame(arr_out)
df = df.rename(columns = {0:'opportunity_id',1:'accepted',2:'withdraw',3:'realized',4:'open',5:'rejected'})
df.to_csv("app_unq.csv", sep=",", index = True)





