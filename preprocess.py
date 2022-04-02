import numpy as np
import glob
import os
from datetime import datetime

DIRECTORY = '/projectnb/dl523/projects/trace_22/data/CROHME_labeled_2016/'
TARGET = '/projectnb/dl523/projects/trace_22/data/processed/'



def make_dir(name):
	if not os.path.exists(name):
		os.mkdir(name)
		print('[ Directory ' + name + ' created ]')
		

if __name__ == "__main__":
	print('[ Begin Processing... ]')
	print('[' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ']' + '\n')

	paths = glob.glob(DIRECTORY + '**/*.inkml', recursive=True)
	
	print('[ Processing ' + str(len(paths)) + ' inkml files in ' + DIRECTORY + ']')

	make_dir(TARGET)

	total = len(paths)
	cnt = 0
	for inkmlfile_path in paths:
		cnt += 1
		filename = inkmlfile_path.split('/')[-1]
		print('['+str(cnt)+'/'+str(total)+'] working..', filename)

		try:
			pass
			#to_images(inkmlfile_path, TARGET + filename + '.png')
		except:
			print('ERROR: ' + filename)
		print('[SUCCESS]: saved to' + TARGET + filename) 


	
	



