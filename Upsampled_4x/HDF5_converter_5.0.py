import glob
import os
import cv2
import numpy as np
import h5py
import IPython 
import pandas as pd
import csv


df = pd.read_csv('lung_annotation_raw_Final.csv')
df = df[['ACC','TIPE','Xmin','Ymin','Xmax','Ymax','Zt_minsplitnum','Zt_minsplit_rev','Zt_maxsplitnum','Zt_maxsplit_rev','box_size']]
df

csv_file=open('lung_nodule_annotation_5.0.csv', mode='w+')


path = '/home/ivanwilliam/Documents/Full_images/5.0/'
all_dirs = os.listdir(path)
dir_it=0

height = 2048
width = 2048
ratio = height/512


for dir_it in range(len(all_dirs)):
	file_path = '/home/ivanwilliam/Documents/Full_images/5.0/'+str(all_dirs[dir_it])

	for root, dirs, files in os.walk(file_path):
		print('\n\tFound directory: %s' % root)

		
		fileName = sorted(files, key=str)
		N_file = len(fileName)
		# import IPython;IPython.embed()
		i = 1
		k = 0
		
		if i in range(N_file):	
			hdf32_list=[]
			for fileName in sorted (files, key=str):
				if N_file*5-k*32>=32:
					print('Opening %d out of %d image at directory: %s/%s' % (i, N_file, root, fileName))
					picture_ds = cv2.imread('%s/%s' % (root, fileName))
					resize_picture_ds = cv2.resize(picture_ds, dsize=(height, width), interpolation=cv2.INTER_CUBIC)
					pics_array= np.array(resize_picture_ds)

					if i==1:
						pics32_list=[]
						pics32_list.append(pics_array)
						pics32_list.append(pics_array)
						pics32_list.append(pics_array)
						pics32_list.append(pics_array)
						pics32_list.append(pics_array)
						
					else:
						pics32_list.append(pics_array)
						pics32_list.append(pics_array)
						pics32_list.append(pics_array)
						pics32_list.append(pics_array)
						pics32_list.append(pics_array)
						if i*5-32*(k+1)>0:
							pics32_array=np.stack((pics32_list[0], pics32_list[1], pics32_list[2], pics32_list[3], pics32_list[4], 
								pics32_list[5], pics32_list[6], pics32_list[7], pics32_list[8], pics32_list[9],
								pics32_list[10], pics32_list[11], pics32_list[12], pics32_list[13], pics32_list[14], 
								pics32_list[15], pics32_list[16], pics32_list[17], pics32_list[18], pics32_list[19],
								pics32_list[20], pics32_list[21], pics32_list[22], pics32_list[23], pics32_list[24], 
								pics32_list[25], pics32_list[26], pics32_list[27], pics32_list[28], pics32_list[29],
								pics32_list[30], pics32_list[31]), axis=0)
							
							print('\n Compiling 32 images into HDF list \n')
							hdf32_list.append(pics32_array)
							k = k+1
							if N_file*5-k*32>=32:
								pics32_list = pics32_list[32:]
					i=i+1
					
				else:
					if len(pics32_list)>32:
						print('Opening %d out of %d image at directory: %s/%s' % (i, N_file, root, fileName))
						picture_ds = cv2.imread('%s/%s' % (root, fileName))
						resize_picture_ds = cv2.resize(picture_ds, dsize=(height, width), interpolation=cv2.INTER_CUBIC)
						pics_array= np.array(resize_picture_ds)

						s = len(pics32_list)
						r = 32*(k+1)-N_file*5
						x = s%32
						e = s-(r+x)

						print('\n\tThere are less than 32 file remaining, using last 32 images as LAST BATCH of HDF5 from %d till %d' % (i, N_file))
						
						
						pics32_list = pics32_list[e:s]
						print('\t...............Start with '+str(len(pics32_list)) +' data(s) from previous batch...............')
						pics32_list.append(pics_array)
						pics32_list.append(pics_array)
						pics32_list.append(pics_array)
						pics32_list.append(pics_array)
						pics32_list.append(pics_array)
						i=i+1
					else:
						print('Opening %d out of %d image at directory: %s/%s' % (i, N_file, root, fileName))
						picture_ds = cv2.imread('%s/%s' % (root, fileName))
						resize_picture_ds = cv2.resize(picture_ds, dsize=(height, width), interpolation=cv2.INTER_CUBIC)
						pics_array= np.array(resize_picture_ds)

						if i==N_file:
							pics32_list.append(pics_array)
							pics32_list.append(pics_array)
							pics32_list.append(pics_array)
							pics32_list.append(pics_array)
							pics32_list.append(pics_array)
													
							pics32_array=np.stack((pics32_list[0], pics32_list[1], pics32_list[2], pics32_list[3], pics32_list[4], 
								pics32_list[5], pics32_list[6], pics32_list[7], pics32_list[8], pics32_list[9],
								pics32_list[10], pics32_list[11], pics32_list[12], pics32_list[13], pics32_list[14], 
								pics32_list[15], pics32_list[16], pics32_list[17], pics32_list[18], pics32_list[19],
								pics32_list[20], pics32_list[21], pics32_list[22], pics32_list[23], pics32_list[24], 
								pics32_list[25], pics32_list[26], pics32_list[27], pics32_list[28], pics32_list[29],
								pics32_list[30], pics32_list[31]), axis=0)
							print('\n Compiling LAST 32 images into 1 HDF list\n')
							hdf32_list.append(pics32_array)
							k=k+1
							
						else:
							pics32_list.append(pics_array)
							pics32_list.append(pics_array)
							pics32_list.append(pics_array)
							pics32_list.append(pics_array)
							pics32_list.append(pics_array)
						i=i+1


######################################################################################			
			if fileName[0:4]=='AGFA':
				search_str=fileName[0:16]
				dfAcc=df[df['ACC'].str.match(search_str)]
				total_dfAcc=dfAcc.shape[0]
				print('Using AGFA as search keyword')
			if fileName[0:4]=='KDC6':
				search_str=fileName[0:10]
				dfAcc=df[df['ACC'].str.match(search_str)]
				total_dfAcc=dfAcc.shape[0]
				print('Using KDC6 as search keyword')
			else:
				print('Continue......................')
			
			# maxstopper = total_dfAcc - 1
			# import IPython;IPython.embed()


			h=0
			p=0		
			for h in range(total_dfAcc):
				tipe = dfAcc.iloc[[h]].TIPE.values[0]
				x1 = dfAcc.iloc[[h]].Xmin.values[0]
				y1 = dfAcc.iloc[[h]].Ymin.values[0]
				x2 = dfAcc.iloc[[h]].Xmax.values[0]
				y2 = dfAcc.iloc[[h]].Ymax.values[0]
				z1_slice = dfAcc.iloc[[h]].Zt_minsplitnum.values[0]
				z1 = dfAcc.iloc[[h]].Zt_minsplit_rev.values[0]
				z2_slice = dfAcc.iloc[[h]].Zt_maxsplitnum.values[0]
				z2 = dfAcc.iloc[[h]].Zt_maxsplit_rev.values[0]
				box_size = dfAcc.iloc[[h]].box_size.values[0]

				z1_order = str('%0*d' % (3, z1_slice))
				z2_order = str('%0*d' % (3, z2_slice))

				x1 = x1*ratio
				y1 = y1*ratio
				x2 = x2*ratio
				y2 = y2*ratio
				box_size=box_size*ratio
				
				

				# import IPython;IPython.embed()
 				
				if (x1==0 and x2==0 and y1 ==0 and y2==0) or box_size<32:
					print ('\tNo annotation or NODULE too small (<32pix) = '+str(all_dirs[dir_it])+'.......')
					annot_file_path = 'HDF5_File/'+str(str(all_dirs[dir_it])+'_'+str(z1_order))
					# csv_file.write(str(annot_file_path)+','','','','','','',''\n')
					hdf5_name=str(str(all_dirs[dir_it])+'_'+str(z1_order))
					print(hdf5_name+" isn't made")
					h = h+1
					
				else:
					if z1_slice==z2_slice:
						## Printing annotation for z1 & z2
						print ('\tACC and z1, z2 order match found = '+str(search_str)+'.......')
						annot_file_path = 'HDF5_File/'+str(str(all_dirs[dir_it])+'_'+str(z1_order))
						csv_file.write(str(annot_file_path)+','+str(x1)+','+str(y1)+','+str(x2)+','+str(y2)+','+str(z1)+','+str(z2)+','+str(tipe)+'\n')
						
						## Write hdf5 file for z1 & z2

						hdf5_name=str(str(all_dirs[dir_it])+'_'+str(z1_order))
						hdf5_path = '/media/ivanwilliam/Ivan_HDD_2TB/i3d_hdf5_lung_data_resized_4x/HDF5_file/'+str(hdf5_name)+'.h5'
						
						exists = os.path.isfile(hdf5_path)
						if exists:
							print(hdf5_name+" already exists. \n Continue to next hdf5 files .................")
						else:
							hdf_file = h5py.File(hdf5_path, 'w')
							matrix123 = hdf32_list[z1_slice-1]
							hdf_file.create_dataset(name='dataset', data=matrix123)
							hdf_check=h5py.File(hdf5_path, 'r')
							base_items = list (hdf_check.items())
							print ("HDF5_file at "+str(hdf5_path)+" which contain: "+str(base_items)+" successfully created")
							hdf_file.close()
				
						p = p+1
						h = h+1
					else:
						if z2_slice>z1_slice:
							print ('\tz2 and z1 slice position differ, splitting it into 2 file and annotation..........')							
							
							## Printing annotation for z1
							print ('\tACC and z1 match found = '+str(search_str)+'.......')
							annot_file_path = 'HDF5_File/'+str(str(all_dirs[dir_it])+'_'+str(z1_order))
							csv_file.write(str(annot_file_path)+','+str(x1)+','+str(y1)+','+str(x2)+','+str(y2)+','+str(z1)+','+'32'+','+str(tipe)+'\n')

							## Printing annotation for z2
							print ('\tACC and z2 match found = '+str(search_str)+'.......')
							annot_file_path = 'HDF5_File/'+str(str(all_dirs[dir_it])+'_'+str(z2_order))
							csv_file.write(str(annot_file_path)+','+str(x1)+','+str(y1)+','+str(x2)+','+str(y2)+','+'1'+','+str(z2)+','+str(tipe)+'\n')


							## Write hdf5 file for z1
							hdf5_name=str(str(all_dirs[dir_it])+'_'+str(z1_order))
							hdf5_path = '/media/ivanwilliam/Ivan_HDD_2TB/i3d_hdf5_lung_data_resized_4x/HDF5_file/'+str(hdf5_name)+'.h5'
							
							exists = os.path.isfile(hdf5_path)
							if exists:
								print(hdf5_name+" already exists. \n Continue to next hdf5 files .................")
							else:
								hdf_file = h5py.File(hdf5_path, 'w')
								matrix123 = hdf32_list[z1_slice-1]
								hdf_file.create_dataset(name='dataset', data=matrix123)
								hdf_check=h5py.File(hdf5_path, 'r')
								base_items = list (hdf_check.items())
								print ("HDF5_file at "+str(hdf5_path)+" which contain: "+str(base_items)+" successfully created")
								hdf_file.close()

							## Write hdf5 file for z2
							hdf5_name=str(str(all_dirs[dir_it])+'_'+str(z2_order))
							hdf5_path = '/media/ivanwilliam/Ivan_HDD_2TB/i3d_hdf5_lung_data_resized_4x/HDF5_file/'+str(hdf5_name)+'.h5'
							
							exists = os.path.isfile(hdf5_path)
							if exists:
								print(hdf5_name+" already exists. \n Continue to next hdf5 files .................")
							else:
								hdf_file = h5py.File(hdf5_path, 'w')
								matrix123 = hdf32_list[z2_slice-1]
								hdf_file.create_dataset(name='dataset', data=matrix123)
								hdf_check=h5py.File(hdf5_path, 'r')
								base_items = list (hdf_check.items())
								print ("HDF5_file at "+str(hdf5_path)+" which contain: "+str(base_items)+" successfully created")
								hdf_file.close()
						
							p = p+1
							h = h+1

						else:
							h = h+1
			print('\tThere are %d new annotations added' %(p))
		
		
		k = 0
		h = 0
		i = 1
		hdf32_list=[]
		pics32_list=[]
		pics32_array=[]
		dir_it=dir_it + 1