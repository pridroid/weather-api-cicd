from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/weather')
def weather():
    city = request.args.get('city', 'New York')
    return jsonify({
        'city': city,
        'temperature': '25°C',
        'description': 'Sunny'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
