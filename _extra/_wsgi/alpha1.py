# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import gepard as g
from gepard.fits import th_KM09a, th_KM09b, th_KM10, th_KM10b, th_AFKM12, th_KM15

from dash import Dash, Input, Output, callback, dcc, html

models = {'KM09a': th_KM09a, 'KM09b': th_KM09b, 'KM10b': th_KM10b,
          'KM10': th_KM10, 'AFKM12': th_AFKM12, 'KM15': th_KM15}
cffs = ['ImH', 'ReH', 'ImE', 'ReE', 'ImHt', 'ReHt', 'ImEt', 'ReEt']

app = Dash(__name__, requests_pathname_prefix='/alpha/')


app.layout = html.Div(children=[
    html.Div([
      html.Label('Select a model:'),
      dcc.Dropdown(
        id='model-dropdown',
        options=[{'label': k, 'value': k} for k in models.keys()],
        value='KM15'
      )]),
    html.Div([
      html.Label('Select CFF:'),
      dcc.Dropdown(
        id='cff-dropdown',
        options=[{'label': k, 'value': k} for k in cffs],
        value='ImH'
      )]),
    html.Label('Mandelstam t'),
    dcc.Input(
        id='mandelstam-t',
        type='number',
        value=-0.2
    ),
    html.Br(),
    html.Label('xi min'),
    dcc.Input(
        id='xi-min',
        type='number',
        value=0.001
    ),
    html.Label('xi max'),
    dcc.Input(
        id='xi-max',
        type='number',
        value=0.3
    ),
    dcc.RadioItems(
        id='loglin-radio',
        options=[
            {'label': 'linear', 'value': 'linear'},
            {'label': 'logarithmic', 'value': 'log'},
        ],
        value='linear'
    ),
    dcc.Graph(
        id='plot-graph'
    ),
    html.Br(),
    html.Div(id='grid')
])


@app.callback(
    Output('plot-graph', 'figure'),
    Input('model-dropdown', 'value'),
    Input('cff-dropdown', 'value'),
    Input('mandelstam-t', 'value'),
    Input('xi-min', 'value'),
    Input('xi-max', 'value'),
    Input('loglin-radio', 'value'),
    )
def update_graph(model, cff, t, ximin, ximax, loglin):
    model_name = model
    th = models[model]
    if loglin == 'log':
        xis = np.logspace(np.log10(ximin), np.log10(ximax))
    else:  # linear
        xis = np.linspace(ximin, ximax)
    y = np.array([xi*getattr(th, cff)(g.DataPoint({'xi': xi, 't': t, 'Q2': 4})) for xi in xis])
        
    fig = go.Figure(
        data=[go.Scatter(x=xis, y=y)],
        layout=go.Layout(
            title=model_name,
            xaxis_title = 'xi',
            yaxis_title = 'xi*{}'.format(cff),
            xaxis_type = loglin
        )
    )
    return fig


@app.callback(
    Output('grid', 'children'),
    Input('model-dropdown', 'value'),
    Input('cff-dropdown', 'value'),
    Input('mandelstam-t', 'value'),
    Input('xi-min', 'value'),
    Input('xi-max', 'value'),
    Input('loglin-radio', 'value'),
    )
def update_grid(model, cff, t, ximin, ximax, loglin):
    th = models[model]
    if loglin == 'log':
        xis = np.logspace(np.log10(ximin), np.log10(ximax))
    else:  # linear
        xis = np.linspace(ximin, ximax)
    y = np.array([xi*getattr(th, cff)(g.DataPoint({'xi': xi, 't': t, 'Q2': 4})) for xi in xis])

    df = pd.DataFrame(np.array([xis, y]).transpose())
    df.columns = ['xi', 'xi*{}'.format(cff)]

    table = html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in df.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(df.iloc[i][col]) for col in df.columns
            ]) for i in range(len(df))
        ])
    ])
    return table

server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)
