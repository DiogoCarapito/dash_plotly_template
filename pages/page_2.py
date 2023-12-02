import dash
from dash import html
#import dash_bootstrap_components as dbc


dash.register_page(
    __name__,
    path="/page2",
    title="page2",
    name="page2",
    order=2,
)

def layout():
    
    page_2_layout = html.Div(
        [
            html.H2("Page 2", className="text-center"),
        ]
    )
    
    return page_2_layout