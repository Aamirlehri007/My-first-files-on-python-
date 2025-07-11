import statsmodels.api as sm
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x= "sepal_width", y="sepal_length", color="species", marginal_y="violin",
                marginal_x="box", trendline="ols", template="simple_white")
fig.show() 