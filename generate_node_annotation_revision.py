import pandas as pd
import glob
import os
from PIL import Image
import numpy as np
import h5py
import IPython
import csv


df = pd.read_csv('Nodules_Annotation.csv')
df = df[['ACC','TIPE','Xmin','Ymin','Xmax','Ymax','Zt_minsplitnum','Zt_minsplit','Zt_maxsplitnum','Zt_maxsplit']]
df

path = '/media/ivanwilliam/BINUS_DATA/HDF5_Fullfile/'
all_dirs = os.listdir(path)
all_dirs.sort()
# print(all_dirs)

total_data = df.shape[0]

dir_it=0
maxstopper = total_data - 1
i=0

csv_file=open('lung_nodule_annotation.csv', mode='w+')
# print (total_data)



for dir_it in range(len(all_dirs)):
	file_path = '/media/ivanwilliam/BINUS_DATA/HDF5_Fullfile/'+str(all_dirs[dir_it])

	if 'AGFA' in all_dirs[dir_it]:
		search_str = all_dirs[dir_it][0:16]
		search_slice = all_dirs[dir_it][-6:-3]
	if 'KDC6' in all_dirs[dir_it]:
		search_str = all_dirs[dir_it][0:16]
		search_slice = all_dirs[dir_it][-6:-3]
	
	print ('Searching: ACC = '+str(search_str)+' and slice = '+str(search_slice)+' at dataframe.......')
	annot_file_path = 'HDF5_File/'+str(all_dirs[dir_it])

	p = 0
	i = 0
	for i in range(total_data):
		acc_id = df.iloc[[i]].ACC.values[0]
		tipe = df.iloc[[i]].TIPE.values[0]
		x1 = df.iloc[[i]].Xmin.values[0]
		y1 = df.iloc[[i]].Ymin.values[0]
		x2 = df.iloc[[i]].Xmax.values[0]
		y2 = df.iloc[[i]].Ymax.values[0]
		z1_slice = df.iloc[[i]].Zt_minsplitnum.values[0]
		z1 = df.iloc[[i]].Zt_minsplit.values[0]
		z2_slice = df.iloc[[i]].Zt_maxsplitnum.values[0]
		z2 = df.iloc[[i]].Zt_maxsplit.values[0]

		z1_order = str('%0*d' % (3, z1_slice))
		z2_order = str('%0*d' % (3, z2_slice))
      
 #    # if "AGFA" in all_dirs[dir_it]:
    
 #    print ('Searching: ACC = '+str(search_str)+' and slice = '+str(search_slice)+'.......')
		if search_slice==z1_order==z2_order and acc_id == search_str:
			print ('\tACC and z1, z2 order match found = '+str(search_str)+'.......')
			csv_file.write(str(annot_file_path)+','+str(x1)+','+str(y1)+','+str(x2)+','+str(y2)+','+str(z1)+','+str(z2)+','+str(tipe)+'\n')
			p = p+1
			i = i+1
		else:
			if search_slice==z2_order and acc_id==search_str:
				print ('\tACC and z2 match found = '+str(search_str)+'.......')
				csv_file.write(str(annot_file_path)+','+str(x1)+','+str(y1)+','+str(x2)+','+str(y2)+','+'0'+','+str(z2)+','+str(tipe)+'\n')
				p = p+1
				i = i+1
			if search_slice==z1_order and acc_id==search_str:
				print ('\tACC and z1 match found = '+str(search_str)+'.......')
				csv_file.write(str(annot_file_path)+','+str(x1)+','+str(y1)+','+str(x2)+','+str(y2)+','+str(z1)+','+'32'+','+str(tipe)+'\n')
				p = p+1
				i = i+1
			if p==0 and maxstopper==i:
				print ('\tNo data found for ACC found = '+str(all_dirs[dir_it])+'.......')
				csv_file.write(str(annot_file_path)+','+'0'+','+'0'+','+'0'+','+'0'+','+'0'+','+'0'+','+'no_nodule'+'\n')
				p = p+1
			else:
				i = i+1

	dir_it = dir_it+1
	print('\tThere are %d new annotations added' %(p))