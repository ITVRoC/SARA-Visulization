from dash import Dash, dcc, Output, Input, html
import dash_bootstrap_components as dbc
import plotly.express as px
import GraphicMetadata as gmeta
import plotly.graph_objects as go


def geraDashboard(df):
    # Componentes
    app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
    
    pageTitle = dcc.Markdown(children="# Monitoramento de saúde da correia", className="fonte")
    logoImg = html.Img(src="assets/ITV_Logo.png", alt="Logo ITV", className="logo")
    header = html.Header(children=([logoImg, pageTitle]), className="header")
    
        #Acelerômetro
    accGraph = dcc.Graph(figure={},
                         config={'displayModeBar': False},
                         style={'width':'100%'})
    accGraphTitle = dcc.Markdown(children="## Acelerômetro", style={'margin':'0 auto'})
    accGraphRadioItems = dcc.RadioItems(options=[{"label": " Eixo X", "value":"Accelerometer X (g)"}, 
                                                 {"label": " Eixo Y", "value":"Accelerometer Y (g)"}, 
                                                 {"label": " Eixo Z", "value":"Accelerometer Z (g)"}], 
                                        value="Accelerometer Y (g)", 
                                        inline=True,
                                        style={"font-size": 25, 
                                               "display": "flex", 
                                               "justify-content": "space-evenly",
                                               "alignItems":"flex-start", 
                                               "margin-bottom": -8,
                                               "width":"100%"})
    accGraphCheckbox = dcc.Checklist(options=[" Curva Padrão"],
                                     value=[],
                                     style={"font-size": 25})
    
        #Giroscópio
    girGraph = dcc.Graph(figure={},
                         config={'displayModeBar': False},
                         style={'width':'100%'})
    girGraphTitle = dcc.Markdown(children="## Giroscópio", style={'margin':'0 auto'})
    girGraphRadioItems = dcc.RadioItems(options=[{"label": " Eixo X", "value":"Gyroscope X (deg/s)"}, 
                                                 {"label": " Eixo Y", "value":"Gyroscope Y (deg/s)"}, 
                                                 {"label": " Eixo Z", "value":"Gyroscope Z (deg/s)"}], 
                                        value="Gyroscope Y (deg/s)", 
                                        inline=True,
                                        style={"font-size": 25, 
                                               "display": "flex", 
                                               "justify-content": "space-evenly",
                                               "alignItems":"flex-start", 
                                               "margin-bottom": -8,
                                               "width":"100%"})
    girGraphCheckbox = dcc.Checklist(options=[" Curva Padrão"],
                                     value=[],
                                     style={"font-size": 25})
    
    # Layout
    app.layout = dbc.Container([dbc.Row([header]),
                                dbc.Row([
                                    dbc.Col([accGraphTitle, accGraphRadioItems, accGraph, accGraphCheckbox], width=6, style={'display':'flex', 'flexDirection':'column', 'justifyContent':'space-between', 'alignItems':'center', 'width':'50%'}),
                                    dbc.Col([girGraphTitle, girGraphRadioItems, girGraph, girGraphCheckbox], width=6, style={'display':'flex', 'flexDirection':'column', 'justifyContent':'space-between', 'alignItems':'center', 'width':'50%'})
                                ], style={'display':'flex', 'marginTop':60, 'justifyContent':'space-between'})], 
                                style={"margin":"0 auto",'maxWidth':'100vw'}
                               )
       
    #Callback
        #Acelerometro
    @app.callback(
        Output(accGraph, "figure"),
        Input(accGraphRadioItems, "value"),
        Input(accGraphCheckbox, "value")
    )
    def update_accGraph(radioItem, checkbox):
        
        #plota gráfico
        template_personalizado = gmeta.definirTemplateGrafico()
        fig = px.line(x=df['Time (s)'], y = df[radioItem], template=template_personalizado)
        fig.update_traces(line_color='#ECB11F')
        
        #plota segunda linha caso checkbox seja assinalada
        if checkbox != []:
            fig.add_trace(go.Scatter(x=df['Time (s)'], y=df["Magnetometer X (uT)"], line=dict(color="#007E7A"), name="Padrão"))
            
        fig.update_yaxes(type='linear')
        
        return fig
    
        #Giroscópio
    @app.callback(
        Output(girGraph, "figure"),
        Input(girGraphRadioItems, "value"),
        Input(girGraphCheckbox, "value")
    )
    def update_girGraph(radioItem, checkbox):
        
        #plota gráfico
        template_personalizado = gmeta.definirTemplateGrafico()
        fig2 = px.line(x=df['Time (s)'], y = df[radioItem], template=template_personalizado)
        fig2.update_traces(line_color='#ECB11F')
        
        #plota segunda linha caso checkbox seja assinalada
        if checkbox != []:
            fig2.add_trace(go.Scatter(x=df['Time (s)'], y=df["Magnetometer X (uT)"], line=dict(color="#007E7A"), name="Padrão"))
            
        fig2.update_yaxes(type='linear')
        
        return fig2
    
    return app