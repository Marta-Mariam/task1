from dash import Input, Output, html
from utils.data_loader import load
import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = 'plotly_white'

def register_callbacks(app):
    @app.callback(
        Output('city_air_conditions', 'children'), #так как в лояуте задаем айди то их тут указываем он запоминает не названия переменных а айди типо следи за значениями этих айди
        Output ('this_co', 'figure'),
        Output ('this_no2', 'figure'),
        Output ('this_o3', 'figure'),
        Output ('this_so2', 'figure'),
        Output ('this_pm2_5', 'figure'),
        Output ('this_pm10', 'figure'),
        Input('city_name', 'value')
    )
    def update_dashboard(name_city): # name_city че хочу могу писать раз один импут то только он и вернет если много то вернет последовательно, в ретерне может не совпадать назавния и это норм
        response_json = load(name_city)
    
        weather_info = html.Div([
            html.H3(f"{response_json['city_name']}", className="card-title"),
            # html.P(f"US EPA Index: {response_json['us_cur']}", className="card-text"),
            # html.P(f"DEFRA Index: {response_json['defra_cur']}", className="card-text"),
            html.H5(["Текущая оценка качества воздуха: ", html.Span(f"{response_json['pm2_5_cur']} AQI", style={'font-size': '22px', 'font-weight': 'bold'})], className="card-text"),
            html.P(f"Обновлено: {response_json['last_updated']}", className="card-text")
        ], style={'marginBottom': '5px'})

        fig_co = go.Figure(data=[go.Scatter(x=response_json['hours'], y=response_json['co'], marker_color='#9D4CE0', mode='lines+markers', name='угарный газ')],
                           layout=go.Layout(title='Содержание угарного газа по часам',title_x=0.5, xaxis_title='Время', yaxis_title='показатели угарного газа', template='plotly_white'))
                           
        fig_no2 = go.Figure(data=[go.Scatter(x=response_json['hours'], y=response_json['no2'],  marker_color='#9D4CE0', fill='tozeroy', name='диоксид азота')],
                           layout=go.Layout(title='Содержание диоксида азота по часам', title_x=0.5, xaxis_title='Время', yaxis_title='показатели диоксида азота'))                

        fig_o3 = go.Figure(data=[go.Bar(x=response_json['hours'], y=response_json['o3'], marker=dict(color=response_json['o3'], colorscale=[[0, '#84fab0'], [1, '#8fd3f4']], colorbar=dict(title='', thickness=10)), name='озон')],
                           layout=go.Layout(title='Содержание озона по часам', title_x=0.5, xaxis_title='Время', yaxis_title='показатели озона'))                  
                           
        fig_so2 = go.Figure(data=[go.Bar(x=response_json['hours'], y=response_json['so2'], marker_color='#7FFFD4', name='диоксид серы')],
                           layout=go.Layout(title='Содержание диоксида серы по часам', title_x=0.5, xaxis=dict(title='Время', tickangle=90), yaxis_title='показатели диоксида серы'))                   
        
        fig_pm2_5 = go.Figure(data=[go.Scatter(x=response_json['hours'], y=response_json['pm2_5'], mode='lines+markers', marker=dict(size=10, color=response_json['pm2_5'], colorscale='purp', colorbar=dict(title='', thickness=10) ))],
                           layout=go.Layout(title='Оценка качества воздуха по часам<br>"значение цвета по типу загрязнения"', title_x=0.5, xaxis_title='Время', yaxis_title='уровень загрязнения'))


        fig_pm10 = go.Figure(data=[go.Scatter(x=response_json['hours'], y=response_json['pm10'], mode='lines+markers', marker_color='#9D4CE0', name='твёрдые частицы в воздухе')],
                           layout=go.Layout(title='Содержание в воздухе твёрдых<br>частиц по часам',title_x=0.5, xaxis_title='Время', yaxis_title='показатели отвёрдых частицы в воздухе')
        ) 
        # fig_pm10 = go.Figure(data=[go.Histogram(x=response_json['hours'], y=response_json['pm10'], marker_color='lightblue', name='твёрдые частицы в воздухе')],
        #                    layout=go.Layout(title='Содержание в воздухе твёрдых<br>частиц по часам',title_x=0.5, xaxis_title='Время', yaxis_title='показатели отвёрдых частицы в воздухе')
        # )                   
                           
                           
        return weather_info, fig_co, fig_no2, fig_o3, fig_so2, fig_pm2_5, fig_pm10

#возвращает последовательно в колбек когда пишем ретерн




# import numpy as np

# fig_pm2_5_colored = go.Figure(
#     data=go.Scatter(
#         x=hours,
#         y=response_json['pm2_5'],
#         mode='markers+lines',
#         marker=dict(
#             size=10,
#             color=response_json['pm2_5'],  # уровень загрязнения как цвет
#             colorscale='RdYlGn_r',  # Красный — плохо, Зелёный — хорошо
#             colorbar=dict(title='PM2.5 µg/m³')
#         ),
#         name='PM2.5'
#     )
# )
# fig_pm2_5_colored.update_layout(
#     title='PM2.5 по часам (цвет = загрязнение)',
#     xaxis_title='Время',
#     yaxis_title_title='µg/m³',
#     template='plotly_dark'
# )

# fig_wind = go.Figure()

# fig_wind.add_trace(go.Barpolar(
#     r=response_json['wind_speed'],  # Скорость ветра
#     theta=response_json['wind_dir'],  # Направление в градусах
#     marker=dict(
#         color=response_json['wind_speed'],
#         colorscale='Viridis',
#         colorbar=dict(title='Скорость ветра (км/ч)')
#     ),
#     name='Ветер'
# ))

# fig_wind.update_layout(
#     title='Направление и скорость ветра',
#     template='plotly_dark',
#     polar=dict(
#         angularaxis=dict(
#             direction="clockwise",
#             tickmode="array",
#             rotation=90,
#             tickvals=[0, 45, 90, 135, 180, 225, 270, 315],
#             ticktext=["С", "СВ", "В", "ЮВ", "Ю", "ЮЗ", "З", "СЗ"]
#         ),
#         radialaxis=dict(
#             title="Скорость ветра (км/ч)",
#             tickfont=dict(size=10)
#         )
#     )
# )