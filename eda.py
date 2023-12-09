import pandas as pd
import seaborn as sns


"""
D_clients.csv
D_close_loan.csv
D_job.csv
D_last_credit.csv
D_loan.csv
D_pens.csv
D_salary.csv
D_target.csv
D_work.csv
"""


#df = pd.read_csv("datasets/bank-mix.csv")
#df.head()

df_clients = pd.read_csv("datasets/D_clients.csv")
df_loan = pd.read_csv("datasets/D_loan.csv")
df_close_loan = pd.read_csv("datasets/D_close_loan.csv")
df_salary = pd.read_csv("datasets/D_salary.csv")
df_last_credit = pd.read_csv("datasets/D_last_credit.csv")
df_target = pd.read_csv("datasets/D_target.csv")
df_job = pd.read_csv("datasets/D_job.csv")

df_credits = pd.merge(df_loan, df_close_loan, how = "left", on = "ID_LOAN")
df_client_credits = df_credits[["ID_CLIENT","CLOSED_FL"]].groupby("ID_CLIENT").aggregate(["count","sum"])
df_client_credits.columns = ["credits","closed"]

df_mix_tmp = pd.merge(df_clients, df_client_credits, how = "left", left_on = "ID", right_on = "ID_CLIENT")
df_mix_tmp_1 = pd.merge(df_mix_tmp, df_salary, how = "left", left_on = "ID", right_on = "ID_CLIENT")
df_mix = pd.merge(df_mix_tmp_1, df_job, how = "left", left_on = "ID", right_on = "ID_CLIENT")

df_mix.to_csv("datasets/final.csv")
