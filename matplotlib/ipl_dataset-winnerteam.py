import matplotlib.pyplot as plt
import pandas as pd

df_player=pd.read_csv("ipl_data.csv")
df_match=pd.read_csv("match.csv")

df_merged = pd.merge(df_player, df_match, left_on='match_no', right_on='match_number', how='left')

team_runs = df_merged.groupby('batting_team')['score'].sum().reset_index()
team_runs = team_runs.sort_values(by='score', ascending=False)
print(team_runs.head())