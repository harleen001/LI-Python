import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("batsman.csv")
batsman_runs = df.groupby('batter')['score'].sum().reset_index()
batsman_runs = batsman_runs.sort_values(by='score', ascending=False)


batsmanvalue = batsman_runs[batsman_runs['score'] >= 500]
x = batsmanvalue['batter']
y = batsmanvalue['score']


plt.figure(figsize=(10, 6))

def absolute_value(val):
    a  = int(round(val/100.*y.sum()))
    return a

plt.pie(y,labels=x, autopct=absolute_value, startangle=140,pctdistance=0.85, textprops={'fontsize': 10})

plt.title('Total Runs by Top Batsmen', fontsize=15)
plt.axis('equal') 
plt.tight_layout()
plt.show()