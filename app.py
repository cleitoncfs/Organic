from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    banner_image_url = url_for('static', filename='images/banner-1.jpg')
    return render_template('index.html', banner_image_url=banner_image_url)


if __name__ == '__main__':
    app.run(debug=True)



