import numpy as np
import pandas as pd


ans_df = pd.DataFrame(columns=['List1','List2'])

with open("input_from_adven.tsv", "r") as file:
    for line in file:
        line_strp = line.strip('\n').split(' '*3)
        new_row = pd.DataFrame({'List1': [line_strp[0]], 'List2': [line_strp[1]]})
        ans_df = pd.concat([ans_df,new_row], ignore_index=True)
        #print(line_strp)


#ans_df.columns = ['List_1', 'List_2']

#ans_df = pd.DataFrame({"List_1":np.sort(list_1),"List_2":np.sort(list_2)})
ans_df["List2_sorted"] = np.sort(ans_df['List2'])
ans_df["List1_sorted"] = np.sort(ans_df['List1'])
ans_df['Diff'] = np.abs(ans_df["List2_sorted"].astype(int) - ans_df["List1_sorted"].astype(int))

ans = sum(ans_df["Diff"])

print(ans)
#print(ans_df.columns)