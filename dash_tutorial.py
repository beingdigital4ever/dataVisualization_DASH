import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
import datetime
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(children=[
    dcc.Input(id='input',value='', type="text"),
    html.Div(id='output_graph')
    ]) 

@app.callback(Output(component_id='output_graph',component_property='children'),
              [Input(component_id='input', component_property='value')])


def update_data(input_data):
    
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime(2017, 2, 3)
    df = web.DataReader(input_data, 'iex', start, end)
    df.reset_index(inplace = True)
    df.set_index("date",inplace=True)
    #df = df.drop("symbol", axis=1)



    return dcc.Graph(id='example',
                  figure={
                      'data':[{'x':df.index,'y':df.close,'name':input_data,'type':'line'}],

                        'layout':{'title':input_data}
                      })


if __name__ == "__main__":
    app.run_server(debug=True)
