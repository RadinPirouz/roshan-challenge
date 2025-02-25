from flask import Flask, render_template_string, request
import random
import psutil
import datetime
import os

app = Flask(__name__)

DEFAULT_BACKGROUND_COLORS = "#FF5733,#33FF57,#3357FF"

def get_background_colors():
    colors = request.cookies.get('bg_colors', DEFAULT_BACKGROUND_COLORS)
    return colors.split(",")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resource Monitor</title>
    <style>
        body {
            background-color: {{ bg_color }};
            color: white;
            text-align: center;
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        .container {
            margin-top: 20%;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hello, World!</h1>
        <h2>Datetime: {{ datetime }}</h2>
        <h3>CPU Usage: {{ cpu }}%</h3>
        <h3>RAM Usage: {{ ram }}%</h3>
        <h3>Change Background Colors</h3>
        <form method="POST">
            <label for="colors">Enter Colors (comma-separated):</label><br>
            <input type="text" id="colors" name="colors" value="{{ bg_colors }}"><br><br>
            <input type="submit" value="Change Colors">
        </form>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_colors = request.form['colors']
        response = app.make_response(render_template_string(HTML_TEMPLATE,
                                                            bg_color=random.choice(new_colors.split(",")),
                                                            cpu=psutil.cpu_percent(interval=1),
                                                            ram=psutil.virtual_memory().percent,
                                                            datetime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                            bg_colors=new_colors))
        response.set_cookie('bg_colors', new_colors)
        return response

    bg_colors = get_background_colors()
    bg_color = random.choice(bg_colors)
    return render_template_string(HTML_TEMPLATE,
                                  bg_color=bg_color,
                                  cpu=psutil.cpu_percent(interval=1),
                                  ram=psutil.virtual_memory().percent,
                                  datetime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                  bg_colors=','.join(bg_colors))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

