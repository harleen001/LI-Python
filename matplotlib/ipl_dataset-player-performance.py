import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("batsman.csv")
batsman_runs = df.groupby('batter')['score'].sum().reset_index()
batsman_runs = batsman_runs.sort_values(by='score', ascending=False)

batsmanvalue = batsman_runs[(batsman_runs['score'] != 0) & (batsman_runs['score'] >= 500)]
x = batsmanvalue['batter']
y = batsmanvalue['score']

print(batsmanvalue.head())

plt.pie(y,labels=x,autopct=lambda pct: f'{int(round(pct * sum(y) / 100.0))}')
plt.title('Top Batsman Scores')
plt.show()