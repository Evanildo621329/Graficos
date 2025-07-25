import plotly.express as px
import pandas as pd


ano = ['2020', '2021', '2022', '2023', '2024']
valores = [32, 7, 15, 8, 38]

grafico = px.pie(names=ano, values=valores, title="Percentual do Canal", width=600, height=600)

grafico.show()
