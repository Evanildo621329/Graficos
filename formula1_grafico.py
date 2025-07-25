import pandas as pd
import plotly.express as px

arquivo = pd.read_excel('formula1.xlsx', engine='openpyxl')

#print(arquivo['PILOTO'])
pilotos = arquivo['PILOTO']
pontos = arquivo['PONTOS']

#grafico = px.bar(x=pilotos, y=pontos, width=1000, height=500, title="Mundial de formula 1",)
grafico = px.bar(x=pontos, y=pilotos, width=1000, height=700, title="Mundial de formula 1",
                 orientation='h')

grafico.update_layout(title_x=0.5)
# Personalizando o título e adicionando subtítulo
grafico.update_layout(
    title={
        'text': "Mundial de Fórmula 1",
        'y': 0.95,  # Posição vertical (0 a 1)
        'x': 0.5,    # Posição horizontal (0 = esquerda, 0.5 = centro, 1 = direita)
        'xanchor': 'center',  # Alinhamento horizontal
        'yanchor': 'top',     # Alinhamento vertical
        'font': {
            'size': 24,       # Tamanho da fonte
            'color': 'darkblue',  # Cor do texto
            'family': 'Arial'    # Fonte
        }
    },
    annotations=[
        dict(
            text="Temporada 2023 - Pontos por Piloto",
            x=0.5,
            y=0.88,
            xref="paper",
            yref="paper",
            showarrow=False,
            font=dict(size=14, color="gray")
        )
    ]
)

grafico.show()


