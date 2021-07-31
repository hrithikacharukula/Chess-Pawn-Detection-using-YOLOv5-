from flask import Flask , render_template , flash , request, redirect , url_for,jsonify
from werkzeug.utils import secure_filename
#from empty import empty
from predict import predi
from PIL import Image
import io
import os
import time
#from main import add
import datetime
UPLOAD_FOLDER = "C:\\Users\\hp\\Documents\\Deep Learning\\yolov5 (2)\\content\\yolov5\\static\\images\\inputs"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','mp4'])


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/')
@app.route('/home')
def index():
	return render_template('base.html')

@app.route('/uploader', methods=['GET', 'POST'])
def upload_image():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		print(filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		flash('Image successfully uploaded and displayed below')

		pathin = "static/images/inputs/" + filename
	
		start = datetime.datetime.now()
		predi(pathin)
		end =  datetime.datetime.now()
		delta = end  - start
		time_taken = str(int(delta.total_seconds()*1000))
		ouput_path = "static/images/outs/" + filename
		return render_template('pred.html', res2=[ouput_path,time_taken])

    
@app.route('/predictions')
def pred():
    return render_template('pred.html')
#@app.route('/modelperformace')
#def modelperformace():
#	return render_template('index.html')




if __name__ == "_main_":
	app.run(debug=True)