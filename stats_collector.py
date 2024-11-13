import time
import json
import psutil

def collect_stats():
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
            'disk': psutil.disk_usage('/').percent,
            }
    return stats

def save_stats_to_file():
    while True:
        stats = collect_stats()
        with open('/tmp/system_stats.json', 'w') as f:
            json.dump(stats, f)
        time.sleep(2)

if __name__ == '__main__':
    save_stats_to_file()
