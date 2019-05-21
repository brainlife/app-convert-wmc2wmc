import scipy.io as sio
from shutil import copytree, copy
import json
import os
from json import encoder


def pretty_floats(obj):
  if isinstance(obj, float):
      return round(obj, 2)
  elif isinstance(obj, dict):
      return dict((k, pretty_floats(v)) for k, v in obj.items())
  elif isinstance(obj, (list, tuple)):
      return list(map(pretty_floats, obj))
  return obj


if __name__ == '__main__':

	with open('config.json') as f:
		data = json.load(f)
		segmentation_file = data["segmentation"]

	old = sio.loadmat(segmentation_file)
	src_dir = os.path.dirname(segmentation_file)
	out_dir = 'wmc'

	sio.savemat("%s/classification.mat" %out_dir, {"classfication": old["classification"]})
	if os.path.exists('%s/surfaces' %src_dir):
		copytree('%s/surfaces' %src_dir, '%s/surfaces' %out_dir)
	#copytree('%s/tracts' %src_dir, '%s/tracts' %out_dir)

	#round json files
	os.makedirs('%s/tracts' %out_dir)
	tract_dir = '%s/tracts' %src_dir
	tracts = os.listdir(tract_dir)
	count = len(tracts)
	for i in range(1,count):
		in_fname = '%s/%s.json' %(tract_dir, i)
		out_fname = '%s/tracts/%s.json' %(out_dir, i)
		with open(in_fname) as f:
			d = json.load(f)
			fibers = d['coords']
			new_fibers = pretty_floats(fibers)
			with open(out_fname, 'w') as g:
				jsonfile = {'name': d['name'], 'color': d['color'], 'coords': new_fibers}
				json.dump(jsonfile, g, separators=(',',':'))
	copy('%s/tracts/tracts.json' %src_dir, '%s/tracts' %out_dir)	

