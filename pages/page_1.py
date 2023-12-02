import dash
from dash import html
#import dash_bootstrap_components as dbc


dash.register_page(
    __name__,
    path="/",
    title="",
    name="",
    order=1,
)

def layout():
    
    page_1_layout = html.Div(
        [
            html.H2("Page 1", className="text-center"),
        ]
    )
    
    return page_1_layout