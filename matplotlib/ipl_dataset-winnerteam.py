import matplotlib.pyplot as plt
import pandas as pd

df_player=pd.read_csv("batsman.csv")
df_match=pd.read_csv("match.csv")

df_merged = pd.merge(df_player, df_match, left_on='match_no', right_on='match_number', how='left')


df_merged['batting_team'] = df_merged.apply(lambda row: row['team1'] if row['inningno'] == 1 else row['team2'], axis=1)


team_runs = df_merged.groupby('batting_team')['score'].sum().reset_index()
team_runs = team_runs.sort_values(by='score', ascending=False)
top10winners=team_runs.head(5)

plt.bar(top10winners['batting_team'],top10winners['score'])
plt.show()