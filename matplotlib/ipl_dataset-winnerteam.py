import matplotlib.pyplot as plt
import pandas as pd

df_player = pd.read_csv("batsman.csv")
df_match = pd.read_csv("match.csv")
df_merged = pd.merge(df_player, df_match, left_on='match_no', right_on='match_number', how='left')

# This logic assumes team1 bats in the 1st inning and team2 in the 2nd
df_merged['batting_team'] = df_merged.apply(
    lambda row: row['team1'] if row['inningno'] == 1 else row['team2'], axis=1
)

team_runs = df_merged.groupby('batting_team')['score'].sum().reset_index()
team_runs = team_runs.sort_values(by='score', ascending=False)
top5winners = team_runs.head(5)

plt.figure(figsize=(10, 6))
bars = plt.bar(top5winners['batting_team'], top5winners['score'], color='skyblue', edgecolor='navy')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 50, yval, ha='center', va='bottom', fontweight='bold')

plt.title('Top 5 Teams by Total Runs', fontsize=14)
plt.xlabel('Team Name', fontsize=12)
plt.ylabel('Total Runs', fontsize=12)

plt.xticks(rotation=15)

plt.tight_layout()
plt.show()