
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
import dash_daq as daq
from dash import Dash, html, dcc
app = daq.Dash(__name__)

app.layout = html.Div([
    daq.Gauge(
        id='my-gauge-1',
        label="Default",
        value=6
    ),
    dcc.Slider(
        id='my-gauge-slider-1',
        min=0,
        max=10,
        step=1,
        value=5
    ),
])

@app.callback(Output('my-gauge-1', 'value'), Input('my-gauge-slider-1', 'value'))
def update_output(value):
    return value

if __name__ == '__main__':
    app.run_server(debug=True)
