from dash import Dash
from layouts import interface
from callbacks import register_callbacks
import dash_bootstrap_components as dbc


app = Dash(external_stylesheets=[dbc.themes.SKETCHY])


server = app.server

app.layout = interface()

register_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)