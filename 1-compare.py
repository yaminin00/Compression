import pandas as pd

# 'new_customer_audited_records.csv'
#  new_customers_all_status_except_audited.csv

df1 = pd.read_csv('C:/Users/NammaYamini/OneDrive - M2P Solutions Private Limited/projects/others/compressor/input-csvs/update_non_audited_records_12thApril2023.csv')
df2 = pd.read_csv('C:/Users/NammaYamini/OneDrive - M2P Solutions Private Limited/projects/others/compressor/src/total-s3images-140423.csv')

# merged_df = pd.merge(df1, df2, on='file', how='outer')

# merged_df.to_csv('C:/Users/AnilKumarRaparthi/OneDrive - Syntizen Technologies Private Limited/MyProjects/others/compressor/size-compared-updation/batch2-new-customers-all-status-except-audited.csv', mode='a', header=False, index=False)
merged_df = df1.merge(df2, on='file')
result_df = merged_df.loc[merged_df.index.isin(df1.index)]
result_df.to_csv('C:/Users/NammaYamini/OneDrive - M2P Solutions Private Limited/projects/others/compressor/size-compared-updation/batch10-update_non_audited_records_12thApril2023.csv', mode='a', header=False, index=False)