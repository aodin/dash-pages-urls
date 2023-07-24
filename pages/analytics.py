import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__)

layout = html.Div(
    children=[
        dcc.Location(id="analytics-url", refresh=False),
        html.H1(children="This is our Analytics page"),
        html.Div(
            [
                "Select a city: ",
                dcc.RadioItems(
                    ["New York City", "Montreal", "San Francisco"],
                    "Montreal",
                    id="analytics-input",
                ),
            ]
        ),
        html.Br(),
        html.Div(id="analytics-output"),
    ]
)


@callback(
    Output("analytics-output", "children"),
    Output("analytics-url", "search"),
    Input("analytics-input", "value"),
)
def update_city_selected(input_value):
    return f"You selected: {input_value}", f"?value={input_value}"
