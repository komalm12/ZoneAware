# api.py

from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return "<h3>Welcome! Go to <a href='/map'>/map</a> to view the accident map.</h3>"

@app.route('/map')
def show_map():
    # Read the saved map.html
    with open("vadodara_accident_map.html", "r", encoding="utf-8") as f:
        map_html = f.read()
    return render_template_string(map_html)

if __name__ == '__main__':
    app.run(debug=True)

