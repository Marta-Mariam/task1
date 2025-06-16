from dash import Input, Output, html
from utils.data_loader import load_data
import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = 'plotly_white'

def register_callbacks(app):
    @app.callback(
        Output('weather-output', 'children'),
        Output('temp-graph', 'figure'),
        Output('ap-graph', 'figure'),
        Output('wind-dir-graph', 'figure'),
        Input('city-input', 'value')
    )
    def update_dashboard(city):
        data = load_data(city)
    
        weather_info = html.Div([
            html.H3(f"{data['city_name']}", className="card-title", style={'font-size': '26px', 'fontFamily': 'Arial'}),
            html.Img(src=f"https:{data['icon']}", style={"height": "64px"}),
            html.H5(f"{data['temp']}°C", className="card-subtitle mb-2 text-muted", style={'font-size': '22px', 'fontFamily': 'Arial'}),
            html.P(data['condition'], className="card-text", style={'font-size': '16px', 'fontFamily': 'Arial', 'opacity': 0.7}),
        ], style={'font-size': '16px', 'fontFamily': 'Arial', 'marginBottom': '5px'})

        # График температуры
        temp_fig = go.Figure(
            data=[go.Scatter(
                x=data['hours'], 
                y=data['temps'], 
                mode='lines+markers',
                name='Температура',
                marker_color='#84fab0',
                line=dict(width=5),
                marker=dict(
                    size=15)  # Увеличьте это значение (было 10)

            )],
            layout=go.Layout(
                title='Температура по часам',
                title_x=0.5,
                xaxis_title='Время',
                yaxis_title='Температура (°C)',
                template='plotly_white',
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family='Arial')
            )
        )


        # График давления 
        ap_fig = go.Figure(
            data=[go.Bar(
                x=data['hours'],
                y=data['ap'],
                name='Атмосферное давление',
                marker=dict(
                    color=data['ap'],
                    colorscale=[[0, '#84fab0'], [1, '#8fd3f4']],
                    colorbar=dict(title='', thickness=10)
                )
            )],
            layout=go.Layout(
                title='Атмосферное давление',
                title_x=0.5,
                xaxis=dict(title='Время', tickangle=90),
                yaxis_title='АД (мм рт.ст.)',
                template='plotly_white',
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family='Arial')
            )
        )

        # График ветра
        wind_dir_fig = go.Figure(
            data=[go.Scatterpolar(
                r=data['wind'],
                theta=data['wind_dirs'],
                mode='lines+markers',
                name='Ветер',
                marker=dict(
                    size=10,
                    color=data['wind'],
                    colorscale='purp',
                    colorbar=dict(title='Скорость (м/с)', thickness=10),
                    line=dict(width=2)
                ),
                line=dict(color='#9D4CE0')
            )],
            layout=go.Layout(
                title='Направление и скорость ветра',
                title_x=0.5,
                polar=dict(
                    radialaxis=dict(visible=True),
                    angularaxis=dict(
                        direction="clockwise",
                        tickmode="array",
                        rotation=90,
                        tickvals=[0, 45, 90, 135, 180, 225, 270, 315],
                        ticktext=["С", "СВ", "В", "ЮВ", "Ю", "ЮЗ", "З", "СЗ"]
                    )
                ),
                template='plotly_white',
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family='Arial')
            )
        )
        
        return weather_info, temp_fig, ap_fig, wind_dir_fig