from flask import Flask, render_template
import psutil

app = Flask(__name__)

@app.route('/')
def system_stats():
    stats = {
        'cpu_percent': psutil.cpu_percent(interval=1),
        'memory': psutil.virtual_memory(),
        'disk': psutil.disk_usage('/')
    }
    return render_template('stats.html', stats=stats)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
