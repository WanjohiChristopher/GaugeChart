from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
import dash_daq as daq

app = Dash(__name__)
app.layout = daq.Gauge(
    color={
        "ranges": {
            "red": [0, 2],
            "pink": [2, 4],
            "#ADD8E6": [4, 6],
            "#4169E1": [6, 8],
            "blue": [8, 10],
        },
    },
    scale={
        "custom": {
            1: {"label": "Strong Sell"},
            3: {"label": "Sell"},
            5: {"label": "Neutral"},
            7: {"label": "Buy"},
            9: {"label": "Strong Buy"},
        }
    },
    value=2,
    max=10,
    min=0,
)

if __name__ == "__main__":
    app.run_server()