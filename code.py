import os, os.path
from PIL import Image,ImageDraw
from clarifai.rest import Image as ClImage
from clarifai.rest import ClarifaiApp
import tkinter_canvas as tkc
import search

#%%capture
#importing and uploading images
def prepare_data(path, app):
	lines = [line.rstrip('\n') for line in open(path + '/filelist.txt')]
	image_count = len(lines)

	#importing only 2000 images
	for i in range(2000):
		app.inputs.create_image_from_filename(path+lines[i], concepts = [lines[i].split('/')[0]])

	labels = [j.split('/', 1)[0] for j in lines]
	#labels = labels[:3779]
	labels = sorted(list(set(labels)))
	return labels[:10]		#only 10 labels can be trained in free plan


#labels = os.listdir(path)

#training custom clarifai model
def train_model(labels):
	model = app.models.create('sketches', concepts=labels)
	model_id = model['model']['id']

	model = app.models.get(model_id)
	model.train()

	model = app.models.get(model_id)
	return model


#get model trained using GUI
def already_trained_model(app):
	model_id = 'doodles2'	#model name on the website

	#model = app.models.get(model_id)
	#model.train()

	model = app.models.get(model_id)
	return model

def predict_image(model, image_to_predict,img_path):
	path = img_path+'/'+image_to_predict
	image = ClImage(file_obj=open(path, 'rb'))
	y = model.predict([image])

	k = 0
	confidence_desc = []
	while True:
		try:
			confidence_desc.append(y['outputs'][0]['data']['concepts'][k]['name'])
			print y['outputs'][0]['data']['concepts'][k]['name'], ':', y['outputs'][0]['data']['concepts'][k]['value']
		except IndexError:
			break
		k = k+1
	return confidence_desc[0]


def main():
	app = ClarifaiApp('')
	path = '/Users/GodSpeed/Documents/CodeWork/recogneyes/recogneyes'
	#labels = prepare_data(path, app)
	#model = train_model(labels)
	model = already_trained_model(app)
	tkc

	most_confident = predict_image(model, 'canvas.png', path)
	good_image = search.main(most_confident)

main()
