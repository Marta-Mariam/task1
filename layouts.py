import dash_bootstrap_components as dbc
from dash import dcc
from dash import dcc, html


def interface():
    return dbc.Container([
    dbc.NavbarSimple(
        brand="Показатели качества воздуха в городе",
        brand_style={"color": "#000000", 'fontSize': '30px', 'fontFamily': 'Arial', 'margin': 'auto', 'width': '100%', 'textAlign': 'center', 'whiteSpace': 'normal'},
        style={
            'background':'linear-gradient(to bottom, #84fab0, #8fd3f4)', 'flexWrap': 'wrap'
        },
        dark=True,
        
        className="mb-4 flex justify-content-between",
    ),
    dbc.Row([
        dbc.Col(
            dbc.Card(id='city_air_conditions', body=True, style={'background': 'linear-gradient(to right, #84fab0, #8fd3f4)'}), width=6, xs=12, md=6),
        dbc.Col([dbc.Input(id='city_name', value='Санкт-Петербург', type='text', placeholder='Укажите город',debounce=True,
                           style={'background': 'linear-gradient(to left, #84fab0, #8fd3f4)', 'fontSize': '16px', 'fontFamily': 'Arial'})]
            , className="mb-3", style={'font-size': '16px','fontFamily': 'Arial'})]),
    html.Div(style={'height': '10px'}),

    dbc.Row([
        dbc.Col(dcc.Graph(id='this_co'), width=6 ,xs=12, md=4),
        dbc.Col(dcc.Graph(id='this_no2'), width=6 ,xs=12, md=4),
        dbc.Col(dcc.Graph(id='this_o3'), width=6 ,xs=12, md=4)], className='mb-3'),
    
    dbc.Row([
        dbc.Col(dcc.Graph(id='this_so2'), width=6 ,xs=12, md=4),
        dbc.Col(dcc.Graph(id='this_pm2_5'), width=6 ,xs=12, md=4),
        dbc.Col(dcc.Graph(id='this_pm10'), width=6 ,xs=12, md=4)], className='mb-3'),
    
    html.Div(style={'height': '10px'})], fluid=True, style={'background-color': '#CFBEE6'})