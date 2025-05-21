import dash
import dash.html as html
import dash.dcc as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import os

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the base folder for static files (Dash will serve from the 'assets' folder)
assets_folder = 'assets/'

# Get lists of files in the respective directories inside 'assets'
attack_type_charts_dir = os.path.join(assets_folder, 'attack_type_charts/PNG')
fatalities_by_year_png_dir = os.path.join(assets_folder, 'fatalities_by_year_png')
high_fatality_maps_by_year_dir = os.path.join(assets_folder, 'high_fatality_maps_by_year')
military_fatalities_heatmap_dir = os.path.join(assets_folder, 'military_fatalities_heatmap')
overall_map_grouped_by_year_dir = os.path.join(assets_folder, 'overall_map_grouped_by_year')
top_actors_by_fatality_dir = os.path.join(assets_folder, 'top_actors_by_fatality')

# Function to get all files from a directory of a specific type (e.g., png, html)
def get_files_from_dir(directory, file_extension):
    return [f for f in os.listdir(directory) if f.endswith(file_extension)]

# Get all PNG and HTML files in the directories
attack_type_charts = get_files_from_dir(attack_type_charts_dir, '.png')
fatalities_by_year_png = get_files_from_dir(fatalities_by_year_png_dir, '.png')
high_fatality_maps_by_year = get_files_from_dir(high_fatality_maps_by_year_dir, '.html')
military_fatalities_heatmap = get_files_from_dir(military_fatalities_heatmap_dir, '.html')
overall_map_grouped_by_year = get_files_from_dir(overall_map_grouped_by_year_dir, '.html')
top_actors_by_fatality = get_files_from_dir(top_actors_by_fatality_dir, '.png')

# Layout for the dashboard
app.layout = html.Div([

    # Wrap the entire content in a container Div to apply centering styles
    html.Div([
        # Header Row
        dbc.Row([  
            dbc.Col(
                html.H1("2022 - 2025 Ukraine - Russo Mass Casualty Events Dashboard", className="text-center"),
                width=12
            )
        ]),

        # text row
        dbc.Row([
            dbc.Col(
                html.P("This dashboard provides a visual representation of mass casualty events in the Ukraine - Russo war based on military and civilian casualties, along with the distribution of fatalities 2022 - 2025.", style={'color': '#fff'}),  # White text
                width=12  
            )
        ]),

        # Row for displaying all high fatality heatmap HTML files
        dbc.Row([  
            dbc.Col(
                html.Div(
                    [html.Iframe(src=f'/assets/high_fatality_maps_by_year/{file}', width="100%", height="600px")
                     for file in high_fatality_maps_by_year],
                    style={
                        'overflowY': 'scroll',       # Enable vertical scrolling if content is too tall
                        'maxHeight': '700px',         # Set maximum height for iframe
                        'padding': '10px',            # Padding around the iframe
                        'backgroundColor': '#333',    # Dark background for each iframe block
                    }
                ),
                width=10  # Adjust width to take more of the screen
            )
        ]),

        # Row for displaying all military fatalities heatmap HTML files
        dbc.Row([  
            dbc.Col(
                html.Div(
                    [html.Iframe(src=f'/assets/military_fatalities_heatmap/{file}', width="100%", height="600px")
                     for file in military_fatalities_heatmap],
                    style={
                        'overflowY': 'scroll',
                        'maxHeight': '700px',
                        'padding': '10px',
                        'backgroundColor': '#333',  # Dark background for the block
                    }
                ),
                width=10  # Adjust width to take more space
            )
        ]),

        # Row for displaying all PNG charts
        dbc.Row([  
            dbc.Col(
                html.Div(
                    [html.Img(src=f'/assets/attack_type_charts/PNG/{file}', style={"width": "100%"})
                     for file in attack_type_charts],
                    style={
                        'overflowY': 'scroll',       # Enable scrolling if image is too large
                        'maxHeight': '700px',
                        'padding': '10px',
                        'backgroundColor': '#333',   # Dark background for image block
                    }
                ),
                width=10  # Adjust width for better balance
            )
        ]),

        # Row for displaying other PNG charts
        dbc.Row([  
            dbc.Col(
                html.Div(
                    [html.Img(src=f'/assets/fatalities_by_year_png/{file}', style={"width": "100%"})
                     for file in fatalities_by_year_png],
                    style={
                        'border': '2px solid #fff',
                        'overflowY': 'scroll',
                        'maxHeight': '700px',
                        'padding': '10px',
                        'backgroundColor': '#333',
                    }
                ),
                width=8  # Adjust width for better appearance
            )
        ]),

        # Row for displaying top actors chart (PNG)
        dbc.Row([  
            dbc.Col(
                html.Div(
                    [html.Img(src=f'/assets/top_actors_by_fatality/{file}', style={"width": "100%"})
                     for file in top_actors_by_fatality],
                    style={
                        'border': '2px solid #fff',
                        'overflowY': 'scroll',
                        'maxHeight': '700px',
                        'padding': '10px',
                        'backgroundColor': '#333',
                    }
                ),
                width=8  # Adjust width for better fit
            )
        ]),

    ], style={
        'maxWidth': '90%',   # Allow the content to be wider, but still leave some space on the sides
        'margin': '0 auto',  # Centers the content horizontally
        'padding': '20px',   # Add padding inside the container
        'boxSizing': 'border-box',  # Ensures padding is included within the width
        'backgroundColor': '#222',  # Dark background for the whole container
        'color': '#fff'  # White text color for contrast
    })
])

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
