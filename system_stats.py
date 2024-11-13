from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stats.html')
def stats():
    return render_template('stats.html')


@app.route('/projects.html')
def projects():
    return render_template('projects.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/api/stats')
def api_stats():
    try:
        with open('/tmp/system_stats.json', 'r') as f:
            stats = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        stats = {
                'cpu_percents': [0] * 4,
                'cpu_temps': [0] * 4,
                'memory': 0,
                'disk': 0
                }
    return jsonify(stats)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
