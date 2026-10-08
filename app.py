import psutil
from flask import Flask

app = Flask(__name__)


@app.route("/")
def system_health():
    current_CPU = psutil.cpu_percent(interval=1)
    current_Disk = psutil.disk_usage("/").percent
    current_Memory = psutil.virtual_memory().percent

    return f"""
    <h1>EC2 System Health</h1>

    <p>CPU Usage: {current_CPU}%</p>
    <p>Disk Usage: {current_Disk}%</p>
    <p>Memory Usage: {current_Memory}%</p>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
