from flask import Flask, render_template, request, send_file
from PIL import Image
import numpy as np
import io

app = Flask(__name__)

def colorize_based_on_time(image, era):
    # Dummy colorization based on era
    if era == '1900s':
        # Apply a sepia filter or specific palette for 1900s
        return image.convert('RGB').point(lambda p: p * 0.5)
    elif era == '1950s':
        return image.convert('RGB').point(lambda p: p * 0.7)
    # Add more eras as needed
    else:
        return image.convert('RGB')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        era = request.form['era']
        if file:
            image = Image.open(file.stream).convert('L')
            colorized_image = colorize_based_on_time(image, era)
            img_io = io.BytesIO()
            colorized_image.save(img_io, 'PNG')
            img_io.seek(0)
            return send_file(img_io, mimetype='image/png')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
