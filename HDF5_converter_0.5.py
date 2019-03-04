import glob
import os
from PIL import Image
import numpy as np
import h5py
import IPython 

path = '/home/ivanwilliam/Documents/Full_images/0.5'
all_dirs = os.listdir(path)
dir_it=0

for dir_it in range(len(all_dirs)):
	file_path = '/home/ivanwilliam/Documents/Full_images/0.5/'+str(all_dirs[dir_it])
	# import IPython; IPython.embed()

	for root, dirs, files in os.walk(file_path):
		print('\n\tFound directory: %s' % root)

		# for subdir in dirs:
		# 	print('SUBFOLDER OF ' + str(root) + ': ' + str(subdir))
		# 	namedir = str(subdir)
		
		fileName = sorted(files, key=str)
		N_file = len(fileName)

		i = 1
		k = 0
		
		if i in range(N_file):	
		# print('\t%s' % fileName)
		# if filename.endswith('%0*d.jpg', (4))
			hdf32_list=[]
			for fileName in sorted (files, key=str):
				if N_file-k*64>=64:
					print('Opening %d out of %d image at directory: %s/%s' % (i, N_file, root, fileName))
					picture_ds = Image.open('%s/%s' % (root, fileName))
					pics_array= np.array(picture_ds) 

					if i%64==1:
						pics32_list=[]
						pics32_list.append(pics_array)
						
						# import IPython; IPython.embed()
					if i%64==0:
						# print('Opening %d out of %d image at directory: %s/%s' % (i, N_file, root, fileName))
						# picture_ds = Image.open('%s/%s' % (root, fileName))
						# pics_array= np.array(picture_ds) 
						pics32_list.append(pics_array)
						pics32_array=np.stack((pics32_list[0], pics32_list[2], pics32_list[4], pics32_list[6], pics32_list[8], 
							pics32_list[10], pics32_list[12], pics32_list[14], pics32_list[16], pics32_list[18],
							pics32_list[20], pics32_list[22], pics32_list[24], pics32_list[26], pics32_list[28], 
							pics32_list[30], pics32_list[32], pics32_list[34], pics32_list[36], pics32_list[38],
							pics32_list[40], pics32_list[42], pics32_list[44], pics32_list[46], pics32_list[48], 
							pics32_list[50], pics32_list[52], pics32_list[54], pics32_list[56], pics32_list[58],
							pics32_list[60], pics32_list[62]), axis=0)
						print('\n Compiling 32 images into HDF list \n')
						hdf32_list.append(pics32_array)
						k = k+1
						# import IPython; IPython.embed()
						# i=i+1
						# import IPython; IPython.embed()
					else:
						# print('Opening %d out of %d image at directory: %s/%s' % (i, N_file, root, fileName))
						# picture_ds = Image.open('%s/%s' % (root, fileName))
						# pics_array= np.array(picture_ds) 
						pics32_list.append(pics_array)
						# i=i+1
						# import IPython; IPython.embed()
						# print('Array shape of %s is %s' % (fileName, array.shape)) # (512, 512, 3)
					i=i+1
					
				else:
					if i==k*64+1:
						print('Opening %d out of %d image at directory: %s/%s' % (i, N_file, root, fileName))
						picture_ds = Image.open('%s/%s' % (root, fileName))
						pics_array= np.array(picture_ds) 
						r = N_file - k*64

						print('\n\tThere are less than 64 file remaining, using last 64 images as LAST BATCH of HDF5 from %d till %d' % (i, N_file))
						
						x = 64-r
						pics32_list = pics32_list[62-x:62]
						print('\t...............Start with '+str(len(pics32_list)) +' data(s) from previous batch...............')
						# import IPython; IPython.embed()
						pics32_list.append(pics_array)
						# import IPython; IPython.embed()
						# print(len(pics32_list))
						i=i+1
					else:
						print('Opening %d out of %d image at directory: %s/%s' % (i, N_file, root, fileName))
						picture_ds = Image.open('%s/%s' % (root, fileName))
						pics_array= np.array(picture_ds) 
						

						if i==N_file:
							pics32_list.append(pics_array)
							# print(len(pics32_list))
							pics32_array=np.stack((pics32_list[0], pics32_list[2], pics32_list[4], pics32_list[6], pics32_list[8], 
								pics32_list[10], pics32_list[12], pics32_list[14], pics32_list[16], pics32_list[18],
								pics32_list[20], pics32_list[22], pics32_list[24], pics32_list[26], pics32_list[28], 
								pics32_list[30], pics32_list[32], pics32_list[34], pics32_list[36], pics32_list[38],
								pics32_list[40], pics32_list[42], pics32_list[44], pics32_list[46], pics32_list[48], 
								pics32_list[50], pics32_list[52], pics32_list[54], pics32_list[56], pics32_list[58],
								pics32_list[60], pics32_list[62]), axis=0)
							print('\n Compiling LAST 32 images into 1 HDF list\n')
							hdf32_list.append(pics32_array)
							# import IPython; IPython.embed()
							# i=i+1
							k=k+1
							# import IPython; IPython.embed()
						
						else:
							# print('Opening %d out of %d image at directory: %s/%s' % (i, N_file, root, fileName))
							# picture_ds = Image.open('%s/%s' % (root, fileName))
							# pics_array= np.array(picture_ds) 
							pics32_list.append(pics_array)
							# print(len(pics32_list))
						i=i+1
						# import IPython; IPython.embed()
			
			
			# hdf_file = h5py.File(hdf5_path, 'w')
			h = 0
			# hdf_file.open()
			for h in range (k):
				hdf5_name=str(all_dirs[dir_it])+'_%0*d' % (3, h+1)
				hdf5_path = '/media/ivanwilliam/BINUS_DATA/HDF5_File/'+str(hdf5_name)+'.h5'
				hdf_file = h5py.File(hdf5_path, 'w')
				matrix123 = hdf32_list[h]
				hdf_file.create_dataset(name='dataset', data=matrix123)
				
				hdf_check=h5py.File(hdf5_path, 'r')
				base_items = list (hdf_check.items())
				print ("HDF5_file at "+str(hdf5_path)+" which contain: "+str(base_items)+" successfully created")
				# print ("Base directory items: " + '\n' + str(base_items) + '\n with total of ' +str(len(base_items))+ ' dataset(s)')	
				h=h+1
			    	# if h < k:
			    	# 	h=h+1
			    	# if h == k:
			    	# 	hdf_file.close()
			
			# import IPython; IPython.embed()
		k = 0
		h = 0
		i = 1
		hdf32_list=[]
		pics32_list=[]
		pics32_array=[]
		dir_it=dir_it + 1