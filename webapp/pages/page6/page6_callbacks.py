from dash.dependencies import Input, Output, State
from app import app
from pages.home.home_data import get_trajectory
from dash import dcc
from dash import html as dhc
import dash
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np


@app.callback(
    Output('time-block-ranges-intervention', 'value'),
    Output('time-block-ranges-intervention', 'max'),
    Input("microbiome-trajectory-location", "data"),
    Input("number-of-timeblocks-intervention", "value"),
)
def display_value(trajectory_path, number_od_timeblocks):
    maximum = None
    values = []
    if trajectory_path:
        trajectory = get_trajectory(trajectory_path)
        
        maximum = trajectory.y.max()
        values = np.linspace(0, maximum, number_od_timeblocks)
    
    print("values", values, "\n\n")
    return values, maximum

@app.callback(
    Output('page-6-display-value-1', 'children'),
    Output("anomaly-type-intervention", "children"),
    Input("microbiome-trajectory-location", "data"),
    Input("time-block-ranges-intervention", "value"),
    Input("number-of-top-bacteria-intervention", "value"),
    Input("polynomial-degree-intervention", "value"),
)
def display_value(trajectory_path, time_block_ranges, num_top_bacteria, degree):
    results = []
    anomaly_type = []
    if trajectory_path:
        trajectory = get_trajectory(trajectory_path)
        anomaly_type = trajectory.anomaly_type.name
        
        result = trajectory.plot_intervention(
            time_block_ranges=time_block_ranges,
            num_top_bacteria=num_top_bacteria,
            degree=degree,
        )

        results = [
            dcc.Markdown(result["ret_val"], dangerously_allow_html=True),
            dhc.Br(),
            dcc.Graph(figure=result["fig"], config=result["config"], id="intervention"),
            dhc.Br(),
            dhc.Div(id="intervention-info"),
            dhc.Br(),
        ]
    return results, anomaly_type


@app.callback(
    [
        Output("intervention", "figure"),
        Output("intervention-info", "children"),
    ],
    [
        Input("intervention", "clickData"),
        Input("microbiome-trajectory-location", "data"),
        # Input("number-of-changes", "value"),
    ],
    [
        State("intervention", "figure"),
        State("time-block-ranges-intervention", "value"),
    ],
)
def display_value(click_data, trajectory_path, fig, time_block_ranges):
    import plotly.graph_objects as go
    ret_val = ""
    if click_data is not None and trajectory_path is not None:

        trajectory = get_trajectory(trajectory_path)
        curve_number = click_data['points'][0]['curveNumber']
        
        trace = fig['data'][curve_number]
        points = click_data['points'][0]["pointIndex"]
        number_of_changes = 5

        indices = trajectory.reference_groups == True  # & (self.anomaly == False)
        anomaly_type = trajectory.anomaly_type
        anomalies = trajectory.get_anomalies(anomaly_type=anomaly_type, indices=indices)
        intervention_indices = np.logical_and(indices, anomalies == False)
        
        results = trajectory.selection_update_trace(fig, time_block_ranges, number_of_changes, intervention_indices)(trace, points, None)
        fig = results["fig"].to_dict()
        ret_val = results["ret_val"]

        fig['data'][curve_number] = results["trace"]

    ret_val = dcc.Markdown(ret_val, dangerously_allow_html=True)
    return fig, ret_val
    