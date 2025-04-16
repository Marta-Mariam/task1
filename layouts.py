import dash_bootstrap_components as dbc
from dash import dcc
from dash import dcc, html

def interface():
    return dbc.Container([
    dbc.NavbarSimple(
        brand="Состояния воздуха в городе",
        brand_style={"color": "#000000", 'fontWeigt': 'bold', 'textAlign': 'center'}, #цвет бренда названия
        # style={
            #     "backgroundColor": "#e0f7fa",  # Цвет фона
            #     "border": "2px solid black",     # Чёрная окантовка
            #     "borderRadius": "8px"            # (опционально) немного скруглённые углы
            # },
        # color="primary",
        style={
            'background':'linear-gradient(to bottom, #84fab0, #8fd3f4)' #сверху вниз градиент
        },
        dark=True,
        
        className="mb-4 flex justify-content-between",
    ),
    dbc.Row([
        dbc.Col(
            dbc.Card(id='city_air_conditions', body=True, style={'background': 'linear-gradient(to right, #84fab0, #8fd3f4)'}), width=6, xs=12, md=6),
        dbc.Col([dbc.Input(id='city_name', value='Санкт-Петербург', type='text', placeholder='Укажите город',debounce=True, # placeholder='Укажите город' не отображается потому что есть значение value если его не будет тогда выведется
                           style={'background': 'linear-gradient(to left, #84fab0, #8fd3f4)'})]
            , className="mb-3")]),
    html.Div(style={'height': '10px'}), # пустая строка отступа

    dbc.Row([
        dbc.Col(dcc.Graph(id='this_co'), width=6 ,xs=12, md=4),
        dbc.Col(dcc.Graph(id='this_no2'), width=6 ,xs=12, md=4),
        dbc.Col(dcc.Graph(id='this_o3'), width=6 ,xs=12, md=4)], className='mb-3'),
    
    dbc.Row([
        dbc.Col(dcc.Graph(id='this_so2'), width=6 ,xs=12, md=4),
        dbc.Col(dcc.Graph(id='this_pm2_5'), width=6 ,xs=12, md=4),
        dbc.Col(dcc.Graph(id='this_pm10'), width=6 ,xs=12, md=4)], className='mb-3'),
    
    html.Div(style={'height': '10px'})], fluid=True, style={'background-color': '#CFBEE6'})
    
#  если я захочу по центру надпись состояния воздуха так как это кастом а не стиль
# dbc.Navbar(
#     dbc.Container([
#         dbc.NavbarBrand(
#             html.Div("Состояния воздуха в городе", style={
#                 'fontWeight': 'bold',
#                 'textAlign': 'center',
#                 'width': '100%',
#                 'color': 'black',
#                 'fontSize': '24px'
#             }),
#             className="mx-auto"
#         ),
#     ]),
#     style={'background': 'linear-gradient(to bottom, #84fab0, #8fd3f4)'},
#     dark=False,  # нужно False, иначе цвет текста может быть нечитабельным
#     className="mb-4"
# )


    # width=6,  # Ширина на больших экранах
    # xs=12,    # На очень маленьких экранах - 12 колонок (полная ширина)
    # md=6,     # На средних экранах - 6 колонок (половина ширины)
    # className="mb-3"  # Отступ снизу



    # def interface():
    # return dbc.Container([
    #     html.Div(
    #         dbc.NavbarSimple(
    #             brand="Состояние воздуха в городе",
    #             brand_style={"color": "black"},
    #             dark=False,  # отключаем темный режим, чтобы был светлый фон
    #             className="mb-4 text-center"
    #         ),
    #         style={
    #             "backgroundColor": "#e0f7fa",
    #             "border": "2px solid black",
    #             "borderRadius": "8px",
    #             "padding": "8px"  # добавим немного отступа
    #         }
    #     )
    # ])