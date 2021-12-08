import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

import pandas as pd
import numpy as np

import example_figures as example
import roc_fig

figs = {
	'ROC Curves': roc_fig.fig,
	'Example Scatter': example.scatter,
	'Example Histogram': example.histogram
}

app = dash.Dash()

#fig_names = ['scatter', 'histogram']
fig_names = list(figs.keys())
fig_dropdown = html.Div([
    dcc.Dropdown(
        id='fig_dropdown',
        options=[{'label': x, 'value': x} for x in fig_names],
        value=None
    )])
fig_plot = html.Div(id='fig_plot')
app.layout = html.Div([fig_dropdown, fig_plot])

@app.callback(
dash.dependencies.Output('fig_plot', 'children'),
[dash.dependencies.Input('fig_dropdown', 'value')])

def update_output(fig_name):
    return name_to_figure(fig_name)

def name_to_figure(fig_name):
    figure = go.Figure()
    for name in fig_names:
    	if fig_name == name:
    		figure = figs[name]
    
    return dcc.Graph(figure=figure)

app.run_server(debug=True, use_reloader=False)