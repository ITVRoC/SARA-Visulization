from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from matplotlib import cm
from matplotlib import cbook
import pandas as pd
from matplotlib.colors import LightSource
import random

#Z = [[random.random()*100 for column in range(20)] for row in range(4)]
# Convert the list to a NumPy array
Z = []
Z_array = np.array(Z)
# Now, you can access the shape attribute
shape = Z_array.shape

rolos = [[1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1]]
largura = [i for i in range(5)]
largura = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
df = pd.read_csv('../data/sensors.csv')
Z = df['Gyroscope Y (deg/s)']
W = [[1, 0, 0.1*5, 0, 1],
     [1, 0, 0.2*5, 0, 1],
     [1, 0, 0.1*5, 0, 1],
     [1, 0, 0.5*5, 0, 1],
     [1, 0, 0.3*5, 0, 1],
     [1, 0, 0.1*5, 0, 1],
     [1, 0, 0.3*5, 0, 1],
     [1, 0, 0.4*5, 0, 1],
     [1, 0, 0.2*5, 0, 1],
     [1, 0, 0.1*5, 0, 1]]

#fig = px.line_3d(x=rolos, y=largura, z=W,
#                    labels={"x":"Comprimento", "y":"Largura", "z":"Giroscópio", "color":"Tempo"})

fig = go.Figure(data=[go.Surface(z=W)])

fig.add_trace(
    go.Surface(z=rolos,  colorscale='YlGnBu', showscale=False))

fig.show()