from dash import Dash, dcc, html, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go 
import pandas as pd
import numpy as np
import psycopg2 as psy

#Define cores e detalhes dos gráficos plotly
#import GraphicMetadata as gmeta
#template_personalizado = gmeta.definirTemplateGrafico()

#app = Dash(__name__)

#Conecta ao banco de dados
import DataBaseConnection as dbconn
#conn = dbconn.conectarAoBanco() #Conexão
#fetched_data = dbconn.consultaBanco(conn, "select * from test2") #consulta query

#gera dataframe sobre os dados recebidos da query
#all_data_frame = pd.DataFrame(data=fetched_data, columns=["id",'AcelerometroX','AcelerometroY','AcelerometroZ','GyroscopioX','GyroscopioY','GyroscopioZ', 'localizacao', 'Tempo']) 

#---------------Crud do tempo-----------------------
#time_cursor_fetch = dbconn.consultaBanco(conn, "select time from test2")
#time_frame = pd.DataFrame(data = time_cursor_fetch, columns=['Time'])
#temp_time_frame = []
#for time in time_frame['Time']:
#  temp_time_frame.append(time[11:19])
#new_time_frame = pd.DataFrame(data = temp_time_frame, columns=['Tempo'])
#---------------Crud do tempo-----------------------
#---------------Curva padrão------------------------
#pattern_fetch = dbconn.consultaBanco(conn, "select * from sensors")
#pattern_frame = pd.DataFrame(data=pattern_fetch, columns=["id",'AcelerometroXpadrao','AcelerometroYpadrao','AcelerometroZpadrao','GyroscopioXpadrao','GyroscopioYpadrao','GyroscopioZpadrao', 'localizacao', 'Tempo'])
#---------------Curva padrão------------------------
#concat_frame = pd.concat([all_data_frame, pattern_frame]) 
#concat_frame['Tempo'] = new_time_frame["Tempo"]

#Módulo pandas responsável por ler a base de dados em csv
df = pd.read_csv('../data/sensors.csv')

#all_of_data = [df, all_data_frame]

x = df['Time (s)']%5
y = (df['Gyroscope X (deg/s)'])%90
fig2 = go.Figure(data=go.Histogram2d(x=x, y=y))

#breakpoint
import DashBoard as db
#app = db.geraDashboard(concat_frame)
app = db.geraDashboard(df)

if __name__ == '__main__':
  app.run_server(debug=True)