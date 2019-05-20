import scipy.io as sio
from shutil import copytree
import json
import os


if __name__ == '__main__':

	with open('config.json') as f:
		data = json.load(f)
		segmentation_file = data["segmentation"]

	old = sio.loadmat(segmentation_file)
	src_dir = os.path.dirname(segmentation_file)
	out_dir = 'wmc'

	sio.savemat("%s/classification.mat" %out_dir, {"classfication": old["classification"]})
	copytree('%s/tracts' %src_dir, '%s/tracts' %out_dir)
	if os.path.exists('%s/surfaces' %src_dir):
		copytree('%s/surfaces' %src_dir, '%s/surfaces' %out_dir)
