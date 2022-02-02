import pandas as pd
import plotly.express as px
import csv

df = pd.read_csv("dataset1.csv")
mean = df.groupby(["student_id","level"])["attempts"].mean()

fig = px.scatter(mean,x= "student_id", y= "level", size = "attempt", color = "attempt")
