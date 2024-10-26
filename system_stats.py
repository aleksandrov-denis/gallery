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
    # CPU usage per core
    cpu_percents = psutil.cpu_percent(percpu=True)
    # temp for each core
    temps = psutil.sensors_temperatures()
    cpu_temps = [temp.current for temp in temps.get('cpu_thermal', temps.get('coretemp', []))]
    
    # if only one temperature read, then replicate for all cores
    if len(cpu_temps) == 1:
        cpu_temps = cpu_temps * len(cpu_percents)

    stats = {
        'cpu_percents': cpu_percents,
        'cpu_temps': cpu_temps,
        'memory': psutil.virtual_memory().percent,
        'disk': psutil.disk_usage('/').percent
    }
    return jsonify(stats)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
