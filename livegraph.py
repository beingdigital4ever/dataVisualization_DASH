import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
import random
from collections import deque

X = deque(maxlen = 20)
Y = deque(maxlen = 20)

X.append(1)
Y.append(1)

app = dash.Dash()
app.layout = html.Div(children = [
    dcc.Graph('graph-live',animate=True),
    dcc.Interval('graph-update',
                 interval=1000,
                 n_intervals = 0)
    ])

@app.callback(Output('graph-live','figure'),
              [Input('graph-update','n_intervals')])

def update_data(n):

    X.append(X[-1]+1)
    Y.append(Y[-1]+(Y[-1]*random.uniform(-0.1,0.1)))

    data = go.Scatter(
        x = list(X),
        y = list(Y),
        name="Scatter",
        mode="lines+markers")

    return {'data':[data], 'layout':go.Layout( xaxis = dict(range=[min(X),max(X)]),
                                               yaxis = dict(range=[min(Y),max(Y)])
                                               )}

if __name__ == '__main__':
    app.run_server(debug = True)
