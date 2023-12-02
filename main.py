import dash_bootstrap_components as dbc
from dash import (
    Dash,
    html,
    page_container,
)  # , page_registry, Input, Output, State, dcc


# Boostrap theme
bs = "https://cdn.jsdelivr.net/npm/bootswatch@5.2.3/dist/simplex/bootstrap.min.css"

# Register pages
app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    external_stylesheets=[bs, dbc.icons.BOOTSTRAP],
)

# App title
app.title = "dash template"

# App layout
app.layout = html.Div(
    [
        html.H1("Dash Template", className="text-center"),
        page_container,
    ]
)

# App server
server = app.server

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
