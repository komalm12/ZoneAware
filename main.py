import pandas as pd
import folium
from folium.plugins import MarkerCluster

def create_map():
    # Load dataset
    file_path = r"C:\Users\hp\Downloads\api\vadodara_accidents_with_weather_time.csv"
    df = pd.read_csv(file_path)

    # Center of Vadodara
    map_center = [df['latitude'].mean(), df['longitude'].mean()]
    accident_map = folium.Map(location=map_center, zoom_start=12)

    # Marker Cluster
    marker_cluster = MarkerCluster().add_to(accident_map)

    severity_color = {
        'Fatal': 'red',
        'Nonfatal': 'orange',
        'Deadly': 'black'
    }

    for _, row in df.iterrows():
        popup_text = f"""
        <b>Area:</b> {row['area']}<br>
        <b>Severity:</b> {row['severity']}<br>
        <b>Deaths:</b> {row['deaths']} | <b>Injured:</b> {row['injured']}<br>
        <b>Weather:</b> {row['weather']}<br>
        <b>Time of Day:</b> {row['time_of_day']}
        """
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=6,
            color=severity_color.get(row['severity'], 'blue'),
            fill=True,
            fill_color=severity_color.get(row['severity'], 'blue'),
            fill_opacity=0.8,
            popup=folium.Popup(popup_text, max_width=300)
        ).add_to(marker_cluster)

    return accident_map
