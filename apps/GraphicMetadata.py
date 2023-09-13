import plotly.graph_objects as go

#mudando cores do gráfico
def definirTemplateGrafico():
    template_personalizado = go.layout.Template(
        layout=go.Layout(
            paper_bgcolor="#FFFFFF",  # Cor de fundo do papel (área ao redor do gráfico)
            plot_bgcolor="#FFFFFF",       # Cor de fundo do gráfico
            title_font=dict(color="black"),              # Cor do título do gráfico
            legend_font=dict(color="black"),             # Cor das legendas do gráfico
            xaxis=dict(
                tickfont=dict(color="black"),  # Cor dos rótulos do eixo x
                title_font=dict(color="black", size=20),          # Cor do título do eixo x
                showline=True,                # Exibir linha de referência do eixo x
                linewidth=2,                  # Largura da linha de referência do eixo x
                linecolor="black"               # Cor da linha de referência do eixo x
            ),
            yaxis=dict(
                tickfont=dict(color="black"),  # Cor dos rótulos do eixo y
                title_font=dict(color="black", size=18),          # Cor do título do eixo y
                showline=True,                 # Exibir linha de referência do eixo y
                linewidth=2,                   # Largura da linha de referência do eixo y
                linecolor="black"             # Cor da linha de referência do eixo y
            ),
            
            #title=eixoy[dropdown] + "  ao longo do tempo",     # Título do gráfico
            xaxis_gridcolor="#919191",    # Cor das gridlines perpendiculares ao eixo x
            yaxis_gridcolor="#919191"     # Cor das gridlines perpendiculares ao eixo y
        )
    )
    return template_personalizado