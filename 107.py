import csv
import plotly.graph_objects as go 
import pandas as pd 

df=pd.read_csv('data.csv')
student_df=df.loc[df['student_id']=="TRL_xsl"]
mean=student_df.groupby('level')['attempt'].mean()
print(mean)

figure=go.Figure(go.Bar(
    x=mean,
    y=['level1','level2','level3','level4'],
    orientation='h'
))
figure.show()