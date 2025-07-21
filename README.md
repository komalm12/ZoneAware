# ZoneAware

**Know the Risk, Plan the Future**

ZoneAware is a data-driven web application designed to visualize, analyze, and predict accident risks across different zones of Vadodara, India. By leveraging historical accident data along with weather and time-of-day features, ZoneAware helps urban planners, municipal authorities, and citizens understand accident hotspots and take informed action to improve road safety.

## Features

- **Vadodara Accident Risk Map:**  
  Interactive map visualizing accident locations, severity (fatal, nonfatal, deadly), and contextual data (weather, time of day, area).
- **Dashboard:**  
  - Filter accident data by area, weather, and time of day.
  - Predict accident severity for a selected location and scenario using machine learning.
  - View and edit latitude/longitude for precise location analysis.
- **Statistical Insights:**  
  Key metrics (total accidents, deaths, injuries, unique areas covered) and a variety of visualizations (stacked bar charts, pie/donut charts, etc.).
- **Improvement Suggestions:**  
  Automated, severity-specific safety improvement recommendations based on model predictions.
- **Modern UI:**  
  Clean, Streamlit-based interface with sidebar navigation and custom styling.

## How It Works

1. **Data Loading & Mapping:**  
   Loads a comprehensive Vadodara accident dataset including weather and time-of-day info. Plots data on an interactive Folium map.
2. **Filtering & Visualization:**  
   Filter data by area, weather, and time. Visualize accident severity, deaths, and injuries across the city.
3. **Prediction Engine:**  
   Uses machine learning (XGBoost Classifier) to predict accident severity for user-selected conditions.
4. **Actionable Insights:**  
   Suggests targeted improvements to reduce accident risk and severity, tailored to the predicted outcome.

## Getting Started

### Prerequisites

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- pandas, folium, scikit-learn, xgboost, plotly

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/komalm12/ZoneAware.git
   cd ZoneAware
   ```

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the dataset:**  
   Place your Vadodara accident data CSV (must include columns: `area`, `latitude`, `longitude`, `weather`, `time_of_day`, `severity`, `deaths`, `injured`) in the project directory and update the data path in `app.py` and `main.py`.

4. **Run the app:**
   ```bash
   streamlit run app.py
   ```
   or for map-only demo:
   ```bash
   python main.py
   ```

## Project Structure

```
ZoneAware/
├── app.py        # Main Streamlit web application
├── main.py       # Standalone map visualizer
├── requirements.txt
└── (your CSV data file)
```

## Example Use Cases

- Identify high-risk accident zones in Vadodara
- Plan traffic interventions and urban improvements
- Predict risk for future urban projects or events
- Raise community awareness about traffic safety

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
