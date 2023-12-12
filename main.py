from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def cat():
    response = requests.get("https://api.thecatapi.com/v1/images/search?random=RAND").json()
    image_url = response[0]['url']
    return render_template('cat_template.html', image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)