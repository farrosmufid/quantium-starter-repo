import dash
from dash import html
from app import app

# Import callback function we want to test
from app import update_plot

def test_check_header_exist(dash_duo):
    dash_duo.start_server(app)  

    header_text = dash_duo.wait_for_element('h1', timeout = 4).text

    assert header_text == 'Soul Foods Pink Morsel Sales'

def test_check_visualisation_exist(dash_duo):
    dash_duo.start_server(app)  

    line_graph_exists = dash_duo.find_element("#pink-morsel-sales-line-graph")

    assert line_graph_exists is not None, "The graph with ID 'pink-morsel-sales-line-graph' was not found"

def test_check_region_picker_exist(dash_duo):
    dash_duo.start_server(app)  

    region_picker_exists = dash_duo.find_element("#region-type")

    assert region_picker_exists is not None, "The graph with ID 'region-type' was not found"



