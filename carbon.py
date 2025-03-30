from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get user input from form
    vehicle_type = request.form['vehicle_type']
    distance = request.form['distance']

    # Carbon Interface API setup (Example API)
    api_url = "https://www.carboninterface.com/api/v1/estimates"
    headers = {
        "Authorization": "Bearer YOUR_API_KEY",
        "Content-Type": "application/json"
    }
    data = {
        "type": "vehicle",
        "distance_unit": "km",
        "distance_value": distance,
        "vehicle_type": vehicle_type
    }

    # Make API request
    response = requests.post(api_url, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        carbon_kg = result['data']['attributes']['carbon_kg']
        return render_template('index.html', result=carbon_kg)
    else:
        return render_template('index.html', error="Failed to calculate emissions. Please try again.")

if __name__ == '__main__':
    app.run(debug=True)