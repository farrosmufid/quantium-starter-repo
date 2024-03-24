import dash
from dash import html
from app import app


def test_check_header_exist(dash_duo):
    '''
    Tests if the header exists on the webpage started by Dash.

    Parameters:
    - dash_duo: Selenium WebDriver with added functionalities for testing Dash applications.
               This is used to interact with the web application, like starting a server, 
               finding elements, and waiting for elements to appear within a timeout.

    Returns:
    - None: This function does not return anything. Instead, it asserts if the header text 
            matches the expected string. If the assertion fails, the test will raise an 
            AssertionError.
    '''
    dash_duo.start_server(app)  

    header_text = dash_duo.wait_for_element('h1', timeout = 4).text

    assert header_text == 'Soul Foods Pink Morsel Sales'

def test_check_visualisation_exist(dash_duo):
    '''
    Tests if a specific line graph visualisation exists on the webpage.

    Parameters:
    - dash_duo: Selenium WebDriver with added functionalities for testing Dash applications.
               It is used to interact with the web application.

    Returns:
    - None: This function does not return anything. It asserts whether an element with a 
            specific ID exists. If the element does not exist, an assertion error is raised.
    
    '''
    dash_duo.start_server(app)  

    line_graph_exists = dash_duo.find_element("#pink-morsel-sales-line-graph")

    assert line_graph_exists is not None, "The graph with ID 'pink-morsel-sales-line-graph' was not found"

def test_check_region_picker_exist(dash_duo):
    '''
    Tests if a region picker radio exits on the webpage.

    Parameters:
    - dash_duo: Selenium WebDriver with added functionalities for testing Dash applications.
               It is used for interacting with the web application.

    Returns:
    - None: This function does not return anything. It asserts whether an element with a 
            specific ID exists. If the element does not exist, an assertion error is raised.

    '''
    dash_duo.start_server(app)  

    region_picker_exists = dash_duo.find_element("#region-type")

    assert region_picker_exists is not None, "The graph with ID 'region-type' was not found"



