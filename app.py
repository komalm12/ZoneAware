# import streamlit as st
# import streamlit.components.v1 as components
# import pandas as pd
# import folium
# from folium.plugins import MarkerCluster

# # ---- Load Dataset ----
# data_path = r"C:\Users\Mahek Gohil\Desktop\urban_planning\algorides\api\vadodara_accidents_with_weather_time.csv"
# df = pd.read_csv(data_path)

# # ---- Filter Function ----
# def filter_data(df, area, weather=None, time=None):
#     filtered = df[df['area'] == area]
#     if weather:
#         filtered = filtered[filtered['weather'] == weather]
#     if time:
#         filtered = filtered[filtered['time_of_day'] == time]
#     return filtered

# # ---- Generate Map ----
# def generate_map(filtered_df, lat, lon):
#     fmap = folium.Map(location=[lat, lon], zoom_start=12)
#     cluster = MarkerCluster().add_to(fmap)

#     for _, row in filtered_df.iterrows():
#         popup = f"""
#         <b>Area:</b> {row['area']}<br>
#         <b>Weather:</b> {row['weather']}<br>
#         <b>Time of Day:</b> {row['time_of_day']}<br>
#         <b>Severity:</b> {row['severity']}<br>
#         <b>Deaths:</b> {row['deaths']} | Injured: {row['injured']}
#         """
#         color = "red" if row['severity'] == "Fatal" else "orange"
#         folium.CircleMarker(
#             location=[row['latitude'], row['longitude']],
#             radius=6,
#             color=color,
#             fill=True,
#             fill_color=color,
#             fill_opacity=0.8,
#             popup=popup
#         ).add_to(cluster)

#     return fmap

# # ---- Streamlit UI ----
# st.set_page_config(page_title="UrbanShield", page_icon="🛡️", layout="wide")

# st.sidebar.title("Navigation")
# # Direct buttons instead of radio
# if st.sidebar.button("Home"):
#     menu = "Home"
# elif st.sidebar.button("Dashboard"):
#     menu = "Dashboard"
# elif st.sidebar.button("Statistical Insights"):
#     menu = "Statistical Insights"
# else:
#     menu = "Home"

# st.markdown("<h1 style='text-align:center; color:#0D47A1; font-size:40px;'>UrbanShield</h1>", unsafe_allow_html=True)

# # Area mapping for auto lat/long
# area_mapping = df.groupby("area")[["latitude", "longitude"]].mean().to_dict(orient="index")

# if menu == "Home":
#     st.markdown("<h2 style='color:#0D47A1; font-size:30px;'>Vadodara Accident Risk Map</h2>", unsafe_allow_html=True)
#     full_map = generate_map(df, df['latitude'].mean(), df['longitude'].mean())
#     components.html(full_map._repr_html_(), height=600)

# elif menu == "Dashboard":
#     st.markdown("<h2 style='color:#0D47A1; font-size:30px;'>Filter Accident Data & View Map</h2>", unsafe_allow_html=True)

#     # Inputs
#     area = st.selectbox("Select Area", list(area_mapping.keys()))
#     weather = st.selectbox("Select Weather", ["All"] + df['weather'].unique().tolist())
#     time_of_day = st.selectbox("Select Time of Day", ["All"] + df['time_of_day'].unique().tolist())

#     # Latitude/Longitude Auto
#     lat = area_mapping[area]["latitude"]
#     lon = area_mapping[area]["longitude"]

#     # Filter Data
#     filtered_df = filter_data(df, area, weather if weather != "All" else None, time_of_day if time_of_day != "All" else None)

#     st.write(f"<h3 style='color:#0D47A1;'>Showing {len(filtered_df)} records for {area}</h3>", unsafe_allow_html=True)
#     if not filtered_df.empty:
#         filtered_map = generate_map(filtered_df, lat, lon)
#         components.html(filtered_map._repr_html_(), height=600)
#     else:
#         st.warning("No records found for the selected filters.")

# elif menu == "Statistical Insights":
#     import plotly.express as px

#     st.markdown("<hr>", unsafe_allow_html=True)
#     st.markdown("<h2 style='color:#0D47A1; font-size:30px;'>Key Metrics</h2>", unsafe_allow_html=True)
#     kpi1, kpi2, kpi3, kpi4 = st.columns(4)
#     kpi1.metric("Total Accidents", len(df))
#     kpi2.metric("Total Deaths", int(df['deaths'].sum()))
#     kpi3.metric("Total Injured", int(df['injured'].sum()))
#     kpi4.metric("Unique Areas", df['area'].nunique())

#     st.markdown("<hr>", unsafe_allow_html=True)
#     st.markdown("<h2 style='color:#0D47A1; font-size:30px;'>Visualizations</h2>", unsafe_allow_html=True)

#     # Row 1
#     row1_col1, row1_col2 = st.columns(2)
#     with row1_col1:
#         st.markdown("<h3 style='color:#0D47A1;'>Type of Road vs Weather (Stacked Bar)</h3>", unsafe_allow_html=True)
#         pivot_road_weather = pd.crosstab(df['type_road'], df['weather']).reset_index()
#         fig = px.bar(
#             pivot_road_weather,
#             x='type_road',
#             y=pivot_road_weather.columns[1:],
#             labels={'value': 'Count', 'type_road': 'Type of Road'},
#             barmode='stack',
#             color_discrete_sequence=px.colors.qualitative.Set2,
#             template='plotly_white'
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     with row1_col2:
#         st.markdown("<h3 style='color:#0D47A1;'>Area vs Time of Day (Line Chart)</h3>", unsafe_allow_html=True)
#         area_time = pd.crosstab(df['area'], df['time_of_day']).reset_index()
#         fig = px.line(
#             area_time,
#             x='area',
#             y=area_time.columns[1:],
#             markers=True,
#             labels={'value': 'Count', 'area': 'Area'},
#             template='plotly_white'
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     # Row 2
#     row2_col1, row2_col2 = st.columns(2)
#     with row2_col1:
#         st.markdown("<h3 style='color:#0D47A1;'>Area vs Severity (Pie Chart)</h3>", unsafe_allow_html=True)
#         severity_counts = df['severity'].value_counts().reset_index()
#         severity_counts.columns = ['severity', 'count']
#         fig = px.pie(
#             severity_counts,
#             values='count',
#             names='severity',
#             color_discrete_sequence=px.colors.sequential.RdBu,
#             template='plotly_white'
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     with row2_col2:
#         st.markdown("<h3 style='color:#0D47A1;'>Type of Road vs Injured (Horizontal Bar)</h3>", unsafe_allow_html=True)
#         injured_by_road = df.groupby('type_road')['injured'].sum().sort_values().reset_index()
#         fig = px.bar(
#             injured_by_road,
#             x='injured',
#             y='type_road',
#             orientation='h',
#             color='injured',
#             color_continuous_scale='Blues',
#             template='plotly_white'
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     # Row 3
#     row3_col1, row3_col2 = st.columns(2)
#     with row3_col1:
#         st.markdown("<h3 style='color:#0D47A1;'>Type of Road vs Deaths (Bar Chart)</h3>", unsafe_allow_html=True)
#         deaths_by_road = df.groupby('type_road')['deaths'].sum().reset_index()
#         fig = px.bar(
#             deaths_by_road,
#             x='type_road',
#             y='deaths',
#             color='deaths',
#             color_continuous_scale='Reds',
#             template='plotly_white'
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     with row3_col2:
#         st.markdown("<h3 style='color:#0D47A1;'>Weather vs Severity (Pie Chart)</h3>", unsafe_allow_html=True)
#         weather_severity = df.groupby('weather')['severity'].value_counts().unstack(fill_value=0)
#         total_severity = weather_severity.sum(axis=0).reset_index()
#         total_severity.columns = ['severity', 'count']
#         fig = px.pie(
#             total_severity,
#             values='count',
#             names='severity',
#             color_discrete_sequence=px.colors.sequential.Mint,
#             template='plotly_white'
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     # Row 4
#     row4_col1, row4_col2 = st.columns(2)
#     with row4_col1:
#         st.markdown("<h3 style='color:#0D47A1;'>Time of Day vs Severity (Line Chart)</h3>", unsafe_allow_html=True)
#         time_severity = pd.crosstab(df['time_of_day'], df['severity']).reset_index()
#         fig = px.line(
#             time_severity,
#             x='time_of_day',
#             y=time_severity.columns[1:],
#             markers=True,
#             labels={'value': 'Count', 'time_of_day': 'Time of Day'},
#             template='plotly_white'
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     with row4_col2:
#         st.markdown("<h3 style='color:#0D47A1;'>Area vs Weather (Stacked Bar)</h3>", unsafe_allow_html=True)
#         pivot_area_weather = pd.crosstab(df['area'], df['weather']).reset_index()
#         fig = px.bar(
#             pivot_area_weather,
#             x='area',
#             y=pivot_area_weather.columns[1:],
#             labels={'value': 'Count', 'area': 'Area'},
#             barmode='stack',
#             color_discrete_sequence=px.colors.qualitative.Pastel,
#             template='plotly_white'
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     # Row 5
#     row5_col1, row5_col2 = st.columns(2)
#     with row5_col1:
#         st.markdown("<h3 style='color:#0D47A1;'>Area vs Injured (Bar Chart)</h3>", unsafe_allow_html=True)
#         injured_by_area = df.groupby('area')['injured'].sum().sort_values(ascending=False).reset_index()
#         fig = px.bar(
#             injured_by_area,
#             x='area',
#             y='injured',
#             color='injured',
#             color_continuous_scale='Greens',
#             template='plotly_white'
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     with row5_col2:
#         st.markdown("<h3 style='color:#0D47A1;'>Area vs Deaths (Donut Chart)</h3>", unsafe_allow_html=True)
#         deaths_by_area = df.groupby('area')['deaths'].sum().sort_values(ascending=False).head(5).reset_index()
#         fig = px.pie(
#             deaths_by_area,
#             values='deaths',
#             names='area',
#             hole=0.4,
#             color_discrete_sequence=px.colors.sequential.OrRd,
#             template='plotly_white'
#         )
#         st.plotly_chart(fig, use_container_width=True)




# import streamlit as st
# import streamlit.components.v1 as components
# import pandas as pd
# import folium
# from folium.plugins import MarkerCluster

# # ---- Load Dataset ----
# data_path = r"C:\Users\Mahek Gohil\Desktop\urban_planning\algorides\api\vadodara_accidents_with_weather_time.csv"
# df = pd.read_csv(data_path)

# # ---- CSS for Sidebar Navigation Appearance ----
# def local_css(css_code):
#     st.markdown(f"<style>{css_code}</style>", unsafe_allow_html=True)

# css_code = """
# /* Sidebar background and text */
# [data-testid="stSidebar"] {
#     background-color: #0D47A1;
# }
# [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3,
# [data-testid="stSidebar"] label, [data-testid="stSidebar"] span {
#     color: white;
# }

# /* Button styling */
# div.stButton > button {
#     background-color: #1565C0;
#     color: white;
#     border: none;
#     border-radius: 8px;
#     padding: 0.5rem 0.75rem;
#     font-weight: 600;
#     width: 100%;
#     margin-bottom: 10px;
#     transition: background-color 0.3s, color 0.3s;
# }
# div.stButton > button:hover {
#     background-color: #FFD54F;
#     color: black;
# }
# div.stButton > button:focus:not(:active) {
#     background-color: #FFD54F;
#     color: black;
# }

# /* Highlight active page button */
# div.stButton.active > button {
#     background-color: #FFD54F;
#     color: black;
# }
# """
# local_css(css_code)

# # ---- Filter Function ----
# def filter_data(df, area, weather=None, time=None):
#     filtered = df[df['area'] == area]
#     if weather:
#         filtered = filtered[filtered['weather'] == weather]
#     if time:
#         filtered = filtered[filtered['time_of_day'] == time]
#     return filtered

# # ---- Generate Map ----
# def generate_map(filtered_df, lat, lon):
#     fmap = folium.Map(location=[lat, lon], zoom_start=12)
#     cluster = MarkerCluster().add_to(fmap)

#     for _, row in filtered_df.iterrows():
#         popup = f"""
#         <b>Area:</b> {row['area']}<br>
#         <b>Weather:</b> {row['weather']}<br>
#         <b>Time of Day:</b> {row['time_of_day']}<br>
#         <b>Severity:</b> {row['severity']}<br>
#         <b>Deaths:</b> {row['deaths']} | Injured: {row['injured']}
#         """
#         color = "red" if row['severity'] == "Fatal" else "orange"
#         folium.CircleMarker(
#             location=[row['latitude'], row['longitude']],
#             radius=6,
#             color=color,
#             fill=True,
#             fill_color=color,
#             fill_opacity=0.8,
#             popup=popup
#         ).add_to(cluster)

#     return fmap

# # ---- Streamlit UI ----
# st.set_page_config(page_title="ZoneAware - Know the Risk, Plan the Future", page_icon="🛡️", layout="wide")

# # Improved sidebar navigation with highlighted active button:
# st.sidebar.title("ZoneAware - Know the Risk, Plan the Future ")
# menu_options = ["Home", "Dashboard", "Statistical Insights"]

# # Persistent state for active button highlighting
# if "active_page" not in st.session_state:
#     st.session_state.active_page = "Home"

# for option in menu_options:
#     if st.sidebar.button(option, key=option):
#         st.session_state.active_page = option

# menu = st.session_state.active_page

# st.markdown("<h1 style='text-align:center; color:#0D47A1; font-size:40px;'>ZoneAware - Know the Risk, Plan the Future</h1>", unsafe_allow_html=True)

# # Area mapping for auto lat/long
# area_mapping = df.groupby("area")[["latitude", "longitude"]].mean().to_dict(orient="index")

# if menu == "Home":
#     st.markdown("<h2 style='color:#0D47A1; font-size:30px;'>Vadodara Accident Risk Map</h2>", unsafe_allow_html=True)
#     full_map = generate_map(df, df['latitude'].mean(), df['longitude'].mean())
#     components.html(full_map._repr_html_(), height=600)

# elif menu == "Dashboard":
#     st.markdown("<h2 style='color:#0D47A1; font-size:30px;'>Filter Accident Data & View Map</h2>", unsafe_allow_html=True)

#     area = st.selectbox("Select Area", list(area_mapping.keys()))
#     weather = st.selectbox("Select Weather", ["All"] + df['weather'].unique().tolist())
#     time_of_day = st.selectbox("Select Time of Day", ["All"] + df['time_of_day'].unique().tolist())

#     lat = area_mapping[area]["latitude"]
#     lon = area_mapping[area]["longitude"]

#     filtered_df = filter_data(df, area, weather if weather != "All" else None, time_of_day if time_of_day != "All" else None)

#     st.write(f"<h3 style='color:#0D47A1;'>Showing {len(filtered_df)} records for {area}</h3>", unsafe_allow_html=True)
#     if not filtered_df.empty:
#         filtered_map = generate_map(filtered_df, lat, lon)
#         components.html(filtered_map._repr_html_(), height=600)
#     else:
#         st.warning("No records found for the selected filters.")

# elif menu == "Statistical Insights":
#     import plotly.express as px

#     st.markdown("<hr>", unsafe_allow_html=True)
#     st.markdown("<h2 style='color:#0D47A1; font-size:30px;'>Key Metrics</h2>", unsafe_allow_html=True)
#     kpi1, kpi2, kpi3, kpi4 = st.columns(4)
#     kpi1.metric("Total Accidents", len(df))
#     kpi2.metric("Total Deaths", int(df['deaths'].sum()))
#     kpi3.metric("Total Injured", int(df['injured'].sum()))
#     kpi4.metric("Unique Areas", df['area'].nunique())

#     st.markdown("<hr>", unsafe_allow_html=True)
#     st.markdown("<h2 style='color:#0D47A1; font-size:30px;'>Visualizations</h2>", unsafe_allow_html=True)


#     # Row 1
#     row1_col1, row1_col2 = st.columns(2)
#     with row1_col1:
#         st.markdown("<h3 style='color:#0D47A1;'>Type of Road vs Weather (Stacked Bar)</h3>", unsafe_allow_html=True)
#         pivot_road_weather = pd.crosstab(df['type_road'], df['weather']).reset_index()
#         fig = px.bar(
#             pivot_road_weather,
#             x='type_road',
#             y=pivot_road_weather.columns[1:],
#             labels={'value': 'Count', 'type_road': 'Type of Road'},
#             barmode='stack',
#             color_discrete_sequence=px.colors.qualitative.Set2,
#             template='plotly_white'
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     with row1_col2:
#         st.markdown("<h3 style='color:#0D47A1;'>Area vs Time of Day (Line Chart)</h3>", unsafe_allow_html=True)
#         area_time = pd.crosstab(df['area'], df['time_of_day']).reset_index()
#         fig = px.line(
#             area_time,
#             x='area',
#             y=area_time.columns[1:],
#             markers=True,
#             labels={'value': 'Count', 'area': 'Area'},
#             template='plotly_white'
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     # Row 2
#     row2_col1, row2_col2 = st.columns(2)
#     with row2_col1:
#         st.markdown("<h3 style='color:#0D47A1;'>Area vs Severity (Pie Chart)</h3>", unsafe_allow_html=True)
#         severity_counts = df['severity'].value_counts().reset_index()
#         severity_counts.columns = ['severity', 'count']
#         fig = px.pie(
#             severity_counts,
#             values='count',
#             names='severity',
#             color_discrete_sequence=px.colors.sequential.RdBu,
#             template='plotly_white'
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     with row2_col2:
#         st.markdown("<h3 style='color:#0D47A1;'>Type of Road vs Injured (Horizontal Bar)</h3>", unsafe_allow_html=True)
#         injured_by_road = df.groupby('type_road')['injured'].sum().sort_values().reset_index()
#         fig = px.bar(
#             injured_by_road,
#             x='injured',
#             y='type_road',
#             orientation='h',
#             color='injured',
#             color_continuous_scale='Blues',
#             template='plotly_white'
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     # Row 3
#     row3_col1, row3_col2 = st.columns(2)
#     with row3_col1:
#         st.markdown("<h3 style='color:#0D47A1;'>Type of Road vs Deaths (Bar Chart)</h3>", unsafe_allow_html=True)
#         deaths_by_road = df.groupby('type_road')['deaths'].sum().reset_index()
#         fig = px.bar(
#             deaths_by_road,
#             x='type_road',
#             y='deaths',
#             color='deaths',
#             color_continuous_scale='Reds',
#             template='plotly_white'
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     with row3_col2:
#         st.markdown("<h3 style='color:#0D47A1;'>Weather vs Severity (Pie Chart)</h3>", unsafe_allow_html=True)
#         weather_severity = df.groupby('weather')['severity'].value_counts().unstack(fill_value=0)
#         total_severity = weather_severity.sum(axis=0).reset_index()
#         total_severity.columns = ['severity', 'count']
#         fig = px.pie(
#             total_severity,
#             values='count',
#             names='severity',
#             color_discrete_sequence=px.colors.sequential.Mint,
#             template='plotly_white'
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     # Row 4
#     row4_col1, row4_col2 = st.columns(2)
#     with row4_col1:
#         st.markdown("<h3 style='color:#0D47A1;'>Time of Day vs Severity (Line Chart)</h3>", unsafe_allow_html=True)
#         time_severity = pd.crosstab(df['time_of_day'], df['severity']).reset_index()
#         fig = px.line(
#             time_severity,
#             x='time_of_day',
#             y=time_severity.columns[1:],
#             markers=True,
#             labels={'value': 'Count', 'time_of_day': 'Time of Day'},
#             template='plotly_white'
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     with row4_col2:
#         st.markdown("<h3 style='color:#0D47A1;'>Area vs Weather (Stacked Bar)</h3>", unsafe_allow_html=True)
#         pivot_area_weather = pd.crosstab(df['area'], df['weather']).reset_index()
#         fig = px.bar(
#             pivot_area_weather,
#             x='area',
#             y=pivot_area_weather.columns[1:],
#             labels={'value': 'Count', 'area': 'Area'},
#             barmode='stack',
#             color_discrete_sequence=px.colors.qualitative.Pastel,
#             template='plotly_white'
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     # Row 5
#     row5_col1, row5_col2 = st.columns(2)
#     with row5_col1:
#         st.markdown("<h3 style='color:#0D47A1;'>Area vs Injured (Bar Chart)</h3>", unsafe_allow_html=True)
#         injured_by_area = df.groupby('area')['injured'].sum().sort_values(ascending=False).reset_index()
#         fig = px.bar(
#             injured_by_area,
#             x='area',
#             y='injured',
#             color='injured',
#             color_continuous_scale='Greens',
#             template='plotly_white'
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     with row5_col2:
#         st.markdown("<h3 style='color:#0D47A1;'>Area vs Deaths (Donut Chart)</h3>", unsafe_allow_html=True)
#         deaths_by_area = df.groupby('area')['deaths'].sum().sort_values(ascending=False).head(5).reset_index()
#         fig = px.pie(
#             deaths_by_area,
#             values='deaths',
#             names='area',
#             hole=0.4,
#             color_discrete_sequence=px.colors.sequential.OrRd,
#             template='plotly_white'
#         )
#         st.plotly_chart(fig, use_container_width=True)




import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder

# ---- Load Dataset ----
data_path = r"C:\Users\Mahek Gohil\Desktop\urban_planning\algorides\api\vadodara_accidents_with_weather_time.csv"
df = pd.read_csv(data_path)

# ---- CSS ----
def local_css(css_code):
    st.markdown(f"<style>{css_code}</style>", unsafe_allow_html=True)
    st.markdown("""
<style>
body, .stApp { background-color: #8baac6; }
</style>
""", unsafe_allow_html=True)

css_code = """
[data-testid="stSidebar"] { background-color: #232b3c; }
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] label, [data-testid="stSidebar"] span { color: white; }
div.stButton > button { background-color: #768390; color: white; border: none; border-radius: 8px; padding: 0.5rem 0.75rem; font-weight: 600; width: 100%; margin-bottom: 10px; }
div.stButton > button:hover { background-color: #ccd6e1; color: black; }
"""
local_css(css_code)

# ---- Filter Function ----
def filter_data(df, area, weather=None, time=None):
    filtered = df[df['area'] == area]
    if weather: filtered = filtered[filtered['weather'] == weather]
    if time: filtered = filtered[filtered['time_of_day'] == time]
    return filtered

# ---- Generate Map ----
def generate_map(filtered_df, lat, lon):
    fmap = folium.Map(location=[lat, lon], zoom_start=12)
    cluster = MarkerCluster().add_to(fmap)

    for _, row in filtered_df.iterrows():
        popup = f"""
        <b>Area:</b> {row['area']}<br>
        <b>Weather:</b> {row['weather']}<br>
        <b>Time of Day:</b> {row['time_of_day']}<br>
        <b>Severity:</b> {row['severity']}<br>
        <b>Deaths:</b> {row['deaths']} | Injured: {row['injured']}
        """
        color = "red" if row['severity'] == "Fatal" else "black" if row['severity'] == "Deadly" else "green"
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=6, color=color, fill=True, fill_color=color,
            fill_opacity=0.8, popup=popup
        ).add_to(cluster)

    if "predicted_severity" in st.session_state:
        pred_class = st.session_state["predicted_severity"]
        pred_color = "red" if pred_class == "Fatal" else "black" if pred_class == "Deadly" else "green"
        folium.CircleMarker(
            location=[lat, lon],
            radius=10, color='blue', fill=True, fill_color=pred_color,
            fill_opacity=0.95, weight=3, popup=f"Predicted: {pred_class}"
        ).add_to(cluster)

    return fmap

# ---- Model Training and Prediction ----
def train_and_predict(df, area, weather, time):
    label_enc = LabelEncoder()
    df['severity_encoded'] = label_enc.fit_transform(df['severity'])
    X = pd.get_dummies(df[['area', 'weather', 'time_of_day']])
    y = df['severity_encoded']
    model = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
    model.fit(X, y)
    input_df = pd.DataFrame([[area, weather, time]], columns=['area', 'weather', 'time_of_day'])
    input_X = pd.get_dummies(input_df).reindex(columns=X.columns, fill_value=0)
    pred_encoded = model.predict(input_X)[0]
    pred_class = label_enc.inverse_transform([pred_encoded])[0]
    return pred_class

# ---- UI ----
st.set_page_config(page_title="ZoneAware - Know the Risk, Plan the Future", layout="wide")
st.sidebar.title("ZoneAware")
menu_options = ["Home", "Dashboard", "Statistical Insights", "Improvement Suggestions"]

if "active_page" not in st.session_state:
    st.session_state.active_page = "Home"

for option in menu_options:
    if st.sidebar.button(option, key=option):
        st.session_state.active_page = option

menu = st.session_state.active_page

st.markdown("<h1 style='text-align:center; color:#242324; font-size:40px;'>ZoneAware - Know the Risk, Plan the Future</h1>", unsafe_allow_html=True)
area_mapping = df.groupby("area")[["latitude", "longitude"]].mean().to_dict(orient="index")

if menu == "Home":
    st.markdown("<h2 style='color:#242324;'>Vadodara Accident Risk Map</h2>", unsafe_allow_html=True)
    full_map = generate_map(df, df["latitude"].mean(), df["longitude"].mean())
    components.html(full_map._repr_html_(), height=600)

elif menu == "Dashboard":
    st.markdown("<h2 style='color:#0D47A1;'>Filter Accident Data & View Map</h2>", unsafe_allow_html=True)

    area = st.selectbox("Select Area", list(area_mapping.keys()))
    weather = st.selectbox("Select Weather", ["All"] + df["weather"].dropna().unique().tolist())
    time_of_day = st.selectbox("Select Time of Day", ["All"] + df["time_of_day"].dropna().unique().tolist())

    # Fetch and allow user to edit latitude and longitude
    default_lat = area_mapping[area]["latitude"]
    default_lon = area_mapping[area]["longitude"]

    lat = st.number_input("Latitude", value=float(default_lat), format="%.6f")
    lon = st.number_input("Longitude", value=float(default_lon), format="%.6f")

    if st.button("Predict Severity for This Selection"):
        pred_class = train_and_predict(
            df,
            area,
            weather if weather != "All" else df["weather"].mode()[0],
            time_of_day if time_of_day != "All" else df["time_of_day"].mode()[0]
        )
        st.success(f"Predicted Severity: {pred_class}")
        st.session_state["predicted_severity"] = pred_class

    filtered_df = filter_data(
        df,
        area,
        weather if weather != "All" else None,
        time_of_day if time_of_day != "All" else None
    )
    st.markdown(f"<h3>Showing {len(filtered_df)} records for {area}</h3>", unsafe_allow_html=True)

    if not filtered_df.empty:
        filtered_map = generate_map(filtered_df, lat, lon)
        components.html(filtered_map._repr_html_(), height=600)
    else:
        st.warning("No records found for the selected filters.")

elif menu == "Statistical Insights":
    import plotly.express as px

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:#0D47A1; font-size:30px;'>Key Metrics</h2>", unsafe_allow_html=True)
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("Total Accidents", len(df))
    kpi2.metric("Total Deaths", int(df['deaths'].sum()))
    kpi3.metric("Total Injured", int(df['injured'].sum()))
    kpi4.metric("Unique Areas", df['area'].nunique())

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:#0D47A1; font-size:30px;'>Visualizations</h2>", unsafe_allow_html=True)


    # Row 1
    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        st.markdown("<h3 style='color:#0D47A1;'>Type of Road vs Weather (Stacked Bar)</h3>", unsafe_allow_html=True)
        pivot_road_weather = pd.crosstab(df['type_road'], df['weather']).reset_index()
        fig = px.bar(
            pivot_road_weather,
            x='type_road',
            y=pivot_road_weather.columns[1:],
            labels={'value': 'Count', 'type_road': 'Type of Road'},
            barmode='stack',
            color_discrete_sequence=px.colors.qualitative.Set2,
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)

    with row1_col2:
        st.markdown("<h3 style='color:#0D47A1;'>Area vs Time of Day (Line Chart)</h3>", unsafe_allow_html=True)
        area_time = pd.crosstab(df['area'], df['time_of_day']).reset_index()
        fig = px.line(
            area_time,
            x='area',
            y=area_time.columns[1:],
            markers=True,
            labels={'value': 'Count', 'area': 'Area'},
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)

    # Row 2
    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        st.markdown("<h3 style='color:#0D47A1;'>Area vs Severity (Pie Chart)</h3>", unsafe_allow_html=True)
        severity_counts = df['severity'].value_counts().reset_index()
        severity_counts.columns = ['severity', 'count']
        fig = px.pie(
            severity_counts,
            values='count',
            names='severity',
            color_discrete_sequence=px.colors.sequential.RdBu,
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)

    with row2_col2:
        st.markdown("<h3 style='color:#0D47A1;'>Type of Road vs Injured (Horizontal Bar)</h3>", unsafe_allow_html=True)
        injured_by_road = df.groupby('type_road')['injured'].sum().sort_values().reset_index()
        fig = px.bar(
            injured_by_road,
            x='injured',
            y='type_road',
            orientation='h',
            color='injured',
            color_continuous_scale='Blues',
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)

    # Row 3
    row3_col1, row3_col2 = st.columns(2)
    with row3_col1:
        st.markdown("<h3 style='color:#0D47A1;'>Type of Road vs Deaths (Bar Chart)</h3>", unsafe_allow_html=True)
        deaths_by_road = df.groupby('type_road')['deaths'].sum().reset_index()
        fig = px.bar(
            deaths_by_road,
            x='type_road',
            y='deaths',
            color='deaths',
            color_continuous_scale='Reds',
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)

    with row3_col2:
        st.markdown("<h3 style='color:#0D47A1;'>Weather vs Severity (Pie Chart)</h3>", unsafe_allow_html=True)
        weather_severity = df.groupby('weather')['severity'].value_counts().unstack(fill_value=0)
        total_severity = weather_severity.sum(axis=0).reset_index()
        total_severity.columns = ['severity', 'count']
        fig = px.pie(
            total_severity,
            values='count',
            names='severity',
            color_discrete_sequence=px.colors.sequential.Mint,
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)

    # Row 4
    row4_col1, row4_col2 = st.columns(2)
    with row4_col1:
        st.markdown("<h3 style='color:#0D47A1;'>Time of Day vs Severity (Line Chart)</h3>", unsafe_allow_html=True)
        time_severity = pd.crosstab(df['time_of_day'], df['severity']).reset_index()
        fig = px.line(
            time_severity,
            x='time_of_day',
            y=time_severity.columns[1:],
            markers=True,
            labels={'value': 'Count', 'time_of_day': 'Time of Day'},
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)

    with row4_col2:
        st.markdown("<h3 style='color:#0D47A1;'>Area vs Weather (Stacked Bar)</h3>", unsafe_allow_html=True)
        pivot_area_weather = pd.crosstab(df['area'], df['weather']).reset_index()
        fig = px.bar(
            pivot_area_weather,
            x='area',
            y=pivot_area_weather.columns[1:],
            labels={'value': 'Count', 'area': 'Area'},
            barmode='stack',
            color_discrete_sequence=px.colors.qualitative.Pastel,
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)

    # Row 5
    row5_col1, row5_col2 = st.columns(2)
    with row5_col1:
        st.markdown("<h3 style='color:#0D47A1;'>Area vs Injured (Bar Chart)</h3>", unsafe_allow_html=True)
        injured_by_area = df.groupby('area')['injured'].sum().sort_values(ascending=False).reset_index()
        fig = px.bar(
            injured_by_area,
            x='area',
            y='injured',
            color='injured',
            color_continuous_scale='Greens',
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)

    with row5_col2:
        st.markdown("<h3 style='color:#0D47A1;'>Area vs Deaths (Donut Chart)</h3>", unsafe_allow_html=True)
        deaths_by_area = df.groupby('area')['deaths'].sum().sort_values(ascending=False).head(5).reset_index()
        fig = px.pie(
            deaths_by_area,
            values='deaths',
            names='area',
            hole=0.4,
            color_discrete_sequence=px.colors.sequential.OrRd,
            template='plotly_white'
        )
        st.plotly_chart(fig, use_container_width=True)
elif menu == "Improvement Suggestions":
    st.markdown("""
        <style>
        .simple-list-container {
            background-color: #ccd6e1;
            padding: 30px;
            border-radius: 8px;
            max-width: 800px;
            margin: 0 auto;
        }

        .simple-list-container h2 {
            color: #0D47A1;
            font-size: 28px;
            text-align: center;
            margin-bottom: 20px;
        }

        .simple-list-container ul {
            color: black;
            font-size: 18px;
            line-height: 1.8;
        }

        .simple-list-container li {
            margin-bottom: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    severity = st.session_state.get("predicted_severity", None)

    if severity is None:
        st.warning("Please generate a prediction in the Dashboard first.")
    else:
        guidelines = {
            "Fatal": [
                "Install high-resolution speed cameras at accident-prone zones to monitor and deter overspeeding.",
                "Enhance street lighting in poorly lit areas to improve night-time visibility for drivers and pedestrians.",
                "Redesign intersections with a history of severe crashes to reduce conflict points and improve traffic flow.",
                "Establish rapid emergency response units with GPS tracking to reduce response times to serious accidents.",
                "Enforce strict helmet and seatbelt laws through frequent roadside checks and digital monitoring.",
                "Install rumble strips on highways to alert drivers when they are veering off lanes.",
                "Deploy Automatic Number Plate Recognition (ANPR) systems to track and penalize repeated traffic violators."
            ],
            "Nonfatal": [
                "Construct clearly marked pedestrian crossings at busy intersections and school zones.",
                "Repaint and maintain road markings regularly to ensure lane discipline and visibility.",
                "Launch road safety awareness campaigns targeting both drivers and pedestrians.",
                "Trim foliage and remove visual obstructions near junctions to enhance visibility.",
                "Maintain and expand dedicated footpaths and cycle lanes to separate vulnerable users from motor traffic."
            ],
            "Deadly": [
                "Conduct thorough road safety audits to identify and address critical design flaws.",
                "Install median barriers on wide roads to prevent head-on collisions.",
                "Develop a trauma care network by equipping hospitals along highways for accident emergency handling.",
                "Organize regular mock emergency drills involving police, ambulance, and fire services.",
                "Implement Intelligent Transport Systems (ITS) for real-time traffic monitoring and management."
            ]
        }

        st.markdown(f"""
            <div class="simple-list-container">
                <h2>Improvement Suggestions for: <span style='color:#d32f2f'>{severity}</span></h2>
                <ul>
                    {''.join(f'<li>{item}</li>' for item in guidelines.get(severity, []))}
                </ul>
            </div>
        """, unsafe_allow_html=True)
