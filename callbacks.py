from dash import Input, Output, html
from utils.data_loader import load
import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = 'plotly_white'

def register_callbacks(app):
    @app.callback(
        Output('city_air_conditions', 'children'), 
        Output ('this_co', 'figure'),
        Output ('this_no2', 'figure'),
        Output ('this_o3', 'figure'),
        Output ('this_so2', 'figure'),
        Output ('this_pm2_5', 'figure'),
        Output ('this_pm10', 'figure'),
        Input('city_name', 'value')
    )
    def update_dashboard(name_city):
        response_json = load(name_city)
        
        weather_info = html.Div([
            html.H3(f"{response_json['city_name']}", className="card-title",style={'font-size': '26px', 'fontFamily': 'Arial'} ),
            html.H5(["Текущая оценка качества воздуха: ", html.Span(f"{response_json['pm2_5_cur']} AQI", style={'font-size': '22px', 'fontFamily': 'Arial'})], className="card-text", style={'font-size': '22px', 'fontFamily': 'Arial'}),
            html.P(f"Обновлено: {response_json['last_updated']}", className="card-text", style={'font-size': '16px','fontFamily': 'Arial', 'opacity': 0.7})
        ], style={'font-size': '16px','fontFamily': 'Arial', 'marginBottom': '5px'})

        fig_co = go.Figure(data=[go.Scatter(x=response_json['hours'], y=response_json['co'], marker_color='#9D4CE0', mode='lines+markers', name='угарный газ')],
                           layout=go.Layout(title='Угарный газ',title_x=0.5, xaxis_title='Время', yaxis_title='показатели угарного газа', template='plotly_white'))
                           
        fig_no2 = go.Figure(data=[go.Scatter(x=response_json['hours'], y=response_json['no2'],  marker_color='#9D4CE0', fill='tozeroy', name='диоксид азота')],
                           layout=go.Layout(title='Диоксид азота', title_x=0.5, xaxis_title='Время', yaxis_title='показатели диоксида азота'))                

        fig_o3 = go.Figure(data=[go.Bar(x=response_json['hours'], y=response_json['o3'], marker=dict(color=response_json['o3'], colorscale=[[0, '#84fab0'], [1, '#8fd3f4']], colorbar=dict(title='', thickness=10)), name='озон')],
                           layout=go.Layout(title='Озон', title_x=0.5, xaxis=dict(title='Время', tickangle=90), yaxis_title='показатели озона'))                  
                           
        fig_so2 = go.Figure(data=[go.Bar(x=response_json['hours'], y=response_json['so2'], marker_color='#7FFFD4', name='диоксид серы')],
                           layout=go.Layout(title='Диоксид серы', title_x=0.5, xaxis=dict(title='Время', tickangle=90), yaxis_title='показатели диоксида серы'))                   
        
        fig_pm2_5 = go.Figure(data=[go.Scatter(x=response_json['hours'], y=response_json['pm2_5'], mode='lines+markers', marker=dict(size=10, color=response_json['pm2_5'], colorscale='purp', colorbar=dict(title='', thickness=10) ))],
                           layout=go.Layout(title='Оценка качества воздуха', title_x=0.5, xaxis_title='Время', yaxis_title='уровень загрязнения'))


        fig_pm10 = go.Figure(data=[go.Scatter(x=response_json['hours'], y=response_json['pm10'], mode='lines+markers', marker_color='#9D4CE0', name='твёрдые частицы')],
                           layout=go.Layout(title='Твёрдые частицы',title_x=0.5, xaxis_title='Время', yaxis_title='показатели твёрдых частиц')
        ) 
                        
                           
                           
        return weather_info, fig_co, fig_no2, fig_o3, fig_so2, fig_pm2_5, fig_pm10