import os
import pandas as pd

current_path = os.getcwd()
df_q1=pd.read_csv(os.getcwd()+"/df_Q1.csv")
df_q2=pd.read_csv(os.getcwd()+"/df_Q2.csv")


#get the data
df_q1_aag=df_q1["AAG_score"]
df_q1_ta=df_q1["TA_score"]
df_q2_aag=df_q2["AAG_score"]
df_q2_ta=df_q2["TA_score"]


#print the number of data
print("Number of data in Q1: ", len(df_q1))
print("Number of data in Q2: ", len(df_q2))
#calculate the correlation
correlation1 = df_q1_aag.corr(df_q1_ta)
print("Correlation between AI score and TA score in Q1: ", correlation1)
correlation2 = df_q2_aag.corr(df_q2_ta)
print("Correlation between AI score and TA score in Q2: ", correlation2)
#save it to a csv with name correlation.csv
correlation = pd.DataFrame([correlation1, correlation2], columns=["Correlation"], index=["Q1", "Q2"])
correlation.to_csv(current_path+"/correlation.csv")





