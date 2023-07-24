import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__, path="/")

layout = html.Div(
    children=[
        dcc.Location(id="home-url", refresh=False),
        dcc.Input(id="home-init", type="hidden", value=""),
        html.H1(children="This is our Home page"),
        html.Div(
            children="""
        This is our Home page content.
    """
        ),
    ]
)


@callback(Output("home-url", "search"), Input("home-init", "value"))
def update_search(home_init):
    return f"?value=home"
