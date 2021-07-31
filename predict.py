import os

def predi(x):
	#os.chdir('../')
	path = 'python detect.py --weights runs/train/exp2/weights/last.pt --img 640 --conf 0.25 --source ' + x  + ' --name outs --project static/images/'
	os.system(path)
	#os.chdir('./flask_app/')
