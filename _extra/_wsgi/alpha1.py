import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import numpy as np
from plotly.subplots import make_subplots



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.update({'requests_pathname_prefix':'/alpha/'})

x = np.linspace(2,5,100)
y = np.linspace(2,5,100)

varA = 4
varB = 1


X, Y = np.meshgrid(x, y)
fig = go.Figure(go.Surface(
    x = x,
    y = y,
    z = int(varA)*np.sin(int(varB)*X+Y)
))

fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                  highlightcolor="limegreen", project_z=True))

fig.update_layout(
    height=700, width=800,
    title_text="3D plot",
    scene = {
    "xaxis": {"nticks": 20},
    "zaxis": {"nticks": 6},
    'camera_eye': {"x": 0, "y": -1, "z": 0.5},
    "aspectratio": {"x": 1, "y": 1, "z": 0.5}
})

app.layout = html.Div([
    html.H3(children='Test app 3'),
    html.Div([
        html.Label('Odabir funkcije:'),
            dcc.Dropdown(
                options=[
                {'label': 'Asin(b*x+y)', 'value': 'SIN'},
                {'label': 'Acos(b*x+y)', 'value': 'COS'},
                {'label': 'Asinh(b*x-y)', 'value': 'SINH'},
                {'label': 'Acosh(b*x-y)', 'value': 'COSH'}
                ],
                id='Fselect',
                value=['SIN'],
                multi=True
            ),

        html.Div([
            html.Label('A: '),
            dcc.Input(
                id='numA',
                type='number',
                value=4
            ),
            html.Label('B: '),
             dcc.Input(
                id='numB',
                type='number',
                value=1,
            ),
                   ],
        style={'width': '30%', 'display': 'inline-block'}),

        html.Div([
            html.Label('Xrange: '),
            dcc.RangeSlider(
                id='x-axis',
                min=0,
                max=10,
                step=0.5,
                value=[2,5],
                marks={i: '{}'.format(i) for i in range(11)},
                allowCross=False
            ),
            html.Label('Yrange: '),
            dcc.RangeSlider(
                id='y-axis',
                min=0,
                max=10,
                step=0.5,
                value=[2,5],
                marks={i: '{}'.format(i) for i in range(11)},
                allowCross=False,
            )
        ],style={'width': '60%', 'float': 'right'})
    ]),

    html.Hr(),

    html.Div([
            html.Label('Prikaz: '),
            dcc.RadioItems(
                    id='g-type',
                    options=[
                        {'label': '3D', 'value': '3d'},
                        {'label': '2D', 'value': '2d'},
                   ],
                    value='3d',
                    labelStyle={'display': 'inline-block'}
                ),
            ],
        style={'width': '30%', 'display': 'inline-block'}),

    html.Div([
        html.Label('Z-offset: '),
        dcc.Input(
                id='z-off',
                type='number',
                value=0
        ),  
        ],style={'width': '60%', 'float': 'right'}),

    html.Hr(),
    
    html.Div([
    dcc.Graph(id='Test-output',figure = fig)
    ],style={'width': '90%', 'float': 'centre'})

])

@app.callback(
    Output('Test-output','figure'),
    [Input('numA', 'value'),
     Input('numB', 'value'),
     Input('x-axis', 'value'),
     Input('y-axis', 'value'),
     Input('g-type', 'value'),
     Input('Fselect', 'value'),
     Input('z-off', 'value')])
     

def update_graph(varA, varB, Xrange, Yrange, Gtype, Fselect, Zoff):


    x = np.linspace(Xrange[0],Xrange[-1],100)
    y = np.linspace(Yrange[0],Yrange[-1],100)
    
    if Gtype == '2d':

        funkdict2D = {
          "SIN": [int(varA)*np.sin(int(varB)*float(Xrange[0])+y),int(varA)*np.sin(int(varB)*float(Xrange[-1])+y),
                  int(varA)*np.sin(int(varB)*x+float(Yrange[0])),int(varA)*np.sin(int(varB)*x+float(Yrange[-1]))],
          "COS": [int(varA)*np.cos(int(varB)*float(Xrange[0])+y),int(varA)*np.cos(int(varB)*float(Xrange[-1])+y),
                  int(varA)*np.cos(int(varB)*x+float(Yrange[0])),int(varA)*np.cos(int(varB)*x+float(Yrange[-1]))],
          "SINH": [int(varA)*np.sinh(int(varB)*float(Xrange[0])-y),int(varA)*np.sinh(int(varB)*float(Xrange[-1])-y),
                  int(varA)*np.sinh(int(varB)*x-float(Yrange[0])),int(varA)*np.sinh(int(varB)*x-float(Yrange[-1]))],
          "COSH": [int(varA)*np.cosh(int(varB)*float(Xrange[0])-y),int(varA)*np.cosh(int(varB)*float(Xrange[-1])-y),
                  int(varA)*np.cosh(int(varB)*x-float(Yrange[0])),int(varA)*np.cosh(int(varB)*x-float(Yrange[-1]))]
        }
        
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=("Xmin" , "Xmax", "Ymin", "Ymax"))

        data0 = list()
        data1 = list()
        data2 = list()
        data3 = list()

        j=0
        for i in Fselect:
            fig.add_trace(go.Scatter(x=y, y=funkdict2D[i][0]+j*Zoff, name=i), row=1, col=1)
            fig.add_trace(go.Scatter(x=y, y=funkdict2D[i][1]+j*Zoff, name=i), row=1, col=2)
            fig.add_trace(go.Scatter(x=y, y=funkdict2D[i][2]+j*Zoff, name=i), row=2, col=1)
            fig.add_trace(go.Scatter(x=y, y=funkdict2D[i][3]+j*Zoff, name=i), row=2, col=2)
            j+=1

        fig.update_xaxes(title_text="y", row=1, col=1)
        fig.update_xaxes(title_text="y", row=1, col=2)
        fig.update_xaxes(title_text="x", row=2, col=1)
        fig.update_xaxes(title_text="x", row=2, col=2)

        fig.update_yaxes(title_text="z", row=1, col=1)
        fig.update_yaxes(title_text="z", row=1, col=2)
        fig.update_yaxes(title_text="z", row=2, col=1)
        fig.update_yaxes(title_text="z", row=2, col=2)
        
        fig.update_layout(title_text="2D plots")

        
        return fig

    else:

        X, Y = np.meshgrid(x, y)

        funkdict3D = {
          "SIN": int(varA)*np.sin(int(varB)*X+Y),
          "COS": int(varA)*np.cos(int(varB)*X+Y),
          "SINH": int(varA)*np.sinh(int(varB)*X-Y),
          "COSH": int(varA)*np.cosh(int(varB)*X-Y)
        }


        data = list()
        j=0
        for i in Fselect:
            data.append(go.Surface(
            x = x,
            y = y,
            z = funkdict3D[i]+j*Zoff,
            showscale=not(j),
            name = i
            ))
            j+=1
            
        fig = go.Figure(data)

        fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                  highlightcolor="limegreen", project_z=True))
        
        fig.update_layout(
            title_text="3D plot",
            scene = {
            "xaxis": {"nticks": 20},
            "zaxis": {"nticks": 6},
            'camera_eye': {"x": 0, "y": -1, "z": 0.5},
            "aspectratio": {"x": 1, "y": 1, "z": 0.5}
        })
        return fig


if __name__ == '__main__':
    app.run_server(debug=True)
    
