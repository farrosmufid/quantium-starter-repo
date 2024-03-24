import pandas as pd
import numpy as np

import dash
from dash import dcc, html, Input, Output, Dash, State, callback, ctx, dash_table
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import plotly.express as px

import plotly.io as pio
import plotly.graph_objects as go


app = Dash(__name__, external_stylesheets=[dbc.themes.YETI, dbc.icons.FONT_AWESOME])

colors = {
    'background':'#0081A7',
    'text': '#FDFCDC'
}

# Load dataset
soul_foods_sales_df = pd.read_csv('./soul_foods_sales.csv')
soul_foods_sales_df['date'] = pd.to_datetime(soul_foods_sales_df['date'])
    

app.layout = html.Div( [
    html.H1('Soul Foods Pink Morsel Sales', style = {'text-align': 'center'}),
    dbc.Row(
        [
            dbc.Col(
                html.Div(
                    dcc.DatePickerRange(
                    id = 'sales-date-range',
                    min_date_allowed = min(soul_foods_sales_df['date']),
                    max_date_allowed = max(soul_foods_sales_df['date']),
                    month_format = 'MMMM Y',
                    start_date_placeholder_text = 'DD/MM/YYYY',
                    end_date_placeholder_text = 'DD/MM/YYYY',
                    display_format = 'DD/MM/YYYY'
                )
            ), width = 3),

            dbc.Col(
                html.Div(
                dcc.RadioItems (
                    options = [
                        {'label': 'North', 'value': 'north'},
                        {'label': 'East', 'value': 'east'},
                        {'label': 'South', 'value': 'south'},
                        {'label': 'West', 'value': 'west'},
                        {'label': 'All', 'value': 'all'}
                    
                    ], 
                    id = 'region-type',
                    value = 'all', 
                    inline = True,
                    labelStyle = {'margin-right': '10px'}
                )
            ), width = 3)
        ], justify = 'evenly'
    ),
    
    dcc.Graph(id = 'pink-morsel-sales-line-graph')
])

@callback(
    Output(component_id = 'pink-morsel-sales-line-graph', component_property = 'figure'),
    Input(component_id = 'sales-date-range', component_property = 'start_date'),
    Input(component_id = 'sales-date-range', component_property = 'end_date'),
    Input(component_id = 'region-type', component_property = 'value')
)

def update_plot(start_date, end_date, region_type):
    # Load dataset
    soul_foods_sales_df = pd.read_csv('./soul_foods_sales.csv')
    soul_foods_sales_df['date'] = pd.to_datetime(soul_foods_sales_df['date'])
    
    # Filter date
    if start_date is not None:
        start_datetime = pd.to_datetime(start_date, format = '%Y-%m-%d')
        soul_foods_sales_df = soul_foods_sales_df.loc[soul_foods_sales_df['date'] >= start_datetime]

    if end_date is not None:
        end_datetime = pd.to_datetime(end_date, format = '%Y-%m-%d')
        soul_foods_sales_df = soul_foods_sales_df.loc[soul_foods_sales_df['date'] <= end_datetime]
    
    # Filter region
    if region_type == 'north':
        soul_foods_sales_df = soul_foods_sales_df[soul_foods_sales_df['region'] == 'north']
    elif region_type == 'east':
        soul_foods_sales_df = soul_foods_sales_df[soul_foods_sales_df['region'] == 'east']
    elif region_type == 'south':
        soul_foods_sales_df = soul_foods_sales_df[soul_foods_sales_df['region'] == 'south']
    elif region_type == 'west':
        soul_foods_sales_df = soul_foods_sales_df[soul_foods_sales_df['region'] == 'west']
    
    # Create line chart
    soul_foods_sales_df_line_plot = px.line(soul_foods_sales_df, x = 'date', y = 'sales', 
                                            title = 'Pink Morsel Sales (2018-2022)')
    soul_foods_sales_df_line_plot.update_xaxes(title_text = 'Date')
    soul_foods_sales_df_line_plot.update_yaxes(title_text = 'Sales')
    soul_foods_sales_df_line_plot.update_layout(
        title_x = 0.5,
        paper_bgcolor = colors['background'],
        font_color = colors['text']
    )

    soul_foods_sales_df_line_plot['data'][0]['line']['color']="#F07167"


    return soul_foods_sales_df_line_plot

if __name__ == '__main__':
    app.run(debug = True)
