#%%
import pandas as pd

val_label_path = r'/Users/srfolk/Desktop/HackathonLV2/Hackathon_Image_Xray/val.csv'
val_pred_path = r'/Users/srfolk/Downloads/submission_yoloV9e39ep_trainval_conf0481.csv'

val_labeldf = pd.read_csv(val_label_path)
val_predf = pd.read_csv(val_pred_path)

# %%
val_predf['Label']


# %%
# Initialize the 'disease' column with 'Negative' as the default value
for df in [val_labeldf, val_predf]:
    df['disease'] = 'Negative'

# Update the 'disease' column based on the presence of '2' or '6' in the 'Label' column
for i, row in val_labeldf.iterrows():
    if any(label in row['Label'] for label in ['2', '6']):
        val_labeldf.at[i, 'disease'] = 'Positive'

for i, row in val_predf.iterrows():
    if any(label in row['Label'] for label in ['2', '6']):
        val_predf.at[i, 'disease'] = 'Positive'

#%%
len(val_predf)
#%%
TP = 0
FN = 0
TN = 0
FP = 0

for j in range (len(val_labeldf)):
    if val_labeldf['disease'][j] == 'Positive' and val_predf['disease'][j] == 'Positive':
        TP += 1
    elif val_labeldf['disease'][j] == 'Positive' and val_predf['disease'][j] == 'Negative':
        FN += 1
    elif val_labeldf['disease'][j] == 'Negative' and val_predf['disease'][j] == 'Negative':
        TN += 1
    elif val_labeldf['disease'][j] == 'Negative' and val_predf['disease'][j] == 'Positive':
        FP += 1

#%%
#calculate
SEN = TP/(TP+FN)
SPEC = TN/(TN+FP)

# %%
print(f"SENT{SEN}")
print(f"SPEC{SPEC}")
print(f"TP{TP}")
print(f"FN{FN}")
print(f"TN{TN}")
print(f"FP{FP}")
# %%
