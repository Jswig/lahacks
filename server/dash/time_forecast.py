import pandas as pd 
from fbprophet import Prophet

import plotly as plt 
import plotly.graph_objects as go 
import dash 
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output

import pickle
from os.path import join

DATA_PATH = '../../data'

with open(join(DATA_PATH, 'models/time_forecaster.pickle'), 'rb') as f:
   forecaster = pickle.load(f)

def draw_accidents(hours):
    future = forecaster.make_future_dataframe(periods = hours, freq = 'H',
        include_history = False)
    forecast = forecaster.predict(future)

    upper_bound = go.Scatter(
        name = 'Uncertainty interval',
        x = forecast['ds'],
        y = forecast['yhat_upper'],
        mode = 'lines',
        marker_color = '#A24A63',
        line_width = 0,
        fill = 'tonexty',
        hoverinfo = 'skip'
    )
    trace = go.Scatter(
        name = 'Forecast',
        x = forecast['ds'],
        y = forecast['yhat'],
        mode = 'lines',
        marker_color = '#A24A63',
        fill = 'tonexty',
        showlegend = False,

    )
    lower_bound = go.Scatter(
        name = 'Uncertainty lower',
        x = forecast['ds'],
        y = forecast['yhat_lower'],
        mode = 'lines',
        line_width = 0,
        showlegend = False,
        hoverinfo = 'skip'
    )
    layout = go.Layout(
        template = 'simple_white',
        yaxis = {'title_text': 'Number of Accidents'},
        xaxis = {'title_text': 'Time'}
    )
    data = [lower_bound, trace, upper_bound]
    return go.Figure(data, layout)

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1('Traffic accidents forecast'),
    dcc.Input(
        id = 'forecast_range',
        type = 'number',
        placeholder = 'Predict next n hours',
        min = 1,
    ),
    dcc.Graph(
        id = 'accidents_forecast',
        figure = draw_accidents(24000),
        config = {'displayModeBar' : False}
    )
])

# @app.callback(
#     Output('accidents_forecast', 'figure'),
#     [Input('forecast_range', 'value')]
# )
# def update_forecast(n_days):
#     return draw_accidents(n_days)

if __name__ == '__main__':
    app.run_server(debug = True)