import pandas as pd
import plotly.express as px

dp=pd.read_csv("data.csv")
#fig=px.line(dp,x="date",y="cases",color="country",title="COVID CASES",orientation="h")
fig=px.bar(dp,x="date",y="cases",color="country",title="COVID CASES"py covidGraph.pypy covidGraph.py)
#fig=px.scatter(dp,x="date",y="cases",color="country",title="COVID CASES",size_max=60)
fig.show()
