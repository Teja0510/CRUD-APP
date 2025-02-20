from flask import Flask
import os
import datetime
import subprocess

app = Flask(_name_)

@app.route('/htop')
def htop():
    full_name = "Teja Gandham"  # Replace with your name
    username = os.getenv("USER") or os.getenv("USERNAME") or "codespace"
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)  # Convert to IST

    # Get system 'top' command output
    try:
        top_output = subprocess.check_output(["top", "-bn1"]).decode("utf-8")
    except Exception as e:
        top_output = f"Error fetching top output: {e}"

    return f"""
    <h1>Name: {Teja}</h1>
    <h2>User: {teja0510}</h2>
    <h3>Server Time (IST): {ist_time.strftime('%Y-%m-%d %H:%M:%S.%f')}</h3>
    <pre>Top Output:\n{top_output}</pre>
    """

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)