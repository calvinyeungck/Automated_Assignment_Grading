import pandas as pd
from scipy.stats import wilcoxon
import os
import pdb

current_path = os.getcwd()
#wilcoxon test for Q1-9
df = pd.read_csv(os.getcwd()+"/survey_result.csv")
results = []
# pdb.set_trace()
for i in range(9):
    #get the df 3rd column
    df_q = df.iloc[:, 2+i].dropna()

    #convert the df to numpy array
    df_q = df_q.to_numpy()

    #perform t-test
    t_stat, p_value = wilcoxon(df_q - 3, alternative='greater')

    # print(t_stat, p_value)
    #print the non scientific notation
    print(f"Q{i+1}",'{:.10f}'.format(t_stat),'{:.10f}'.format(p_value),len(df_q))

    results.append([t_stat,p_value,len(df_q)])

#binom test for Q10
from scipy.stats import binomtest

binary_responses = df.iloc[:, 11].dropna()
binary_responses = binary_responses.to_list()
#minus the value by 1
binary_responses = [x-1 for x in binary_responses]

#perform binom test
binomtest_results  = binomtest(sum(binary_responses),len(binary_responses),0.5,alternative='greater')
t_stat, p_value, n = binomtest_results.statistic, binomtest_results.pvalue, binomtest_results.n
print(f"Q10",'{:.10f}'.format(t_stat),'{:.10f}'.format(p_value),n)

results.append([t_stat,p_value,n])

#convert the results to df
results = pd.DataFrame(results,columns=['Test_Stats', 'p_value', 'n'],index=[f'Q{i+1}' for i in range(len(results))])

#save the result
results.to_csv(current_path+"/result.csv")

#compare strong and weak student
from scipy.stats import mannwhitneyu

results_group = []
# pdb.set_trace()
for i in range(10):
    #get the df 3rd column
    # df_q = df.iloc[:, 2+i].dropna()
    df_q_s = df[df.group=="strong"].iloc[:, 2+i].dropna()
    df_q_w = df[df.group=="weak"].iloc[:, 2+i].dropna()

    #convert the df to numpy array
    df_q_s = df_q_s.to_numpy()
    df_q_w = df_q_w.to_numpy()

    #perform t-test
    t_stat, p_value = mannwhitneyu(df_q_w, df_q_s, alternative='greater')

    # print(t_stat, p_value)
    #print the non scientific notation
    print(f"Q{i+1}",'{:.10f}'.format(t_stat),'{:.10f}'.format(p_value),len(df_q_w),len(df_q_s))

    results_group.append([t_stat,p_value,len(df_q_w),len(df_q_s)])

#convert results_group to df
results_group = pd.DataFrame(results_group,columns=['Test_Stats', 'p_value', 'n_weak','n_strong'],index=[f'Q{i+1}' for i in range(len(results))])

#save the df
results_group.to_csv(current_path+"/result_group.csv")
