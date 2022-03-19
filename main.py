from flask import Flask, render_template, request, redirect, url_for
from src.detect import process_image

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# api endpoint for image upload
@app.route('/api/upload', methods=['POST'])
def upload():
    # receive the file from the client
    file = request.files['file']
    filepath = f'static/{file.filename}'
    file.save(filepath) # save to directory
    
    # process image
    process_image(filepath)

    # return server url to client
    return f"{request.url_root}{filepath}"


if __name__ == '__main__':
    app.run(debug=True)