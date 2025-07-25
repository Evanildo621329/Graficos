import plotly.express as px
import pandas as pd
# Dados para o gráfico de linha 

eixo_x = ['2020', '2021', '2022', '2023']
eixo_y = [300, 99, 153, 359]

grafico = px.line(x=eixo_x, y=eixo_y, title="Vendas A.I com Daniel", 
                  height=500, width=900)

grafico.show()
