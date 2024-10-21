from flask import Flask, render_template, jsonify
import psutil

app = Flask(__name__)

@app.route('/')
def index():
        return render_template('stats.html')

@app.route('/projects.html')
def projects():
    return render_template('projects.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/api/stats')
def api_stats():
    stats = {
        'cpu_percent': psutil.cpu_percent(interval=1),
        'memory': psutil.virtual_memory().percent,
        'disk': psutil.disk_usage('/').percent
    }
    return jsonify(stats)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
