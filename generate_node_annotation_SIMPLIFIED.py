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

agfa_dirs = all_dirs[0:8096]
agfa_dir_num=0
# print (agfa_dirs)
# print(len(agfa_dirs))
# IPython.embed()

kdc6_dirs = all_dirs[8096:]
kdc6_dir_num=0
# print (kdc6_dirs)


# total_data = df.shape[0]


# maxstopper = total_data - 1
# i=0

csv_file=open('lung_nodule_annotation_fastnodir.csv', mode='w+')
# # print (total_data)

for agfa_dir_num in range(len(agfa_dirs)):
	search_str = agfa_dirs[agfa_dir_num][0:16]
	search_slice = agfa_dirs[agfa_dir_num][-6:-3]
	print ('Searching: ACC = '+str(search_str)+' and slice = '+str(search_slice)+' at dataframe.......')
	annot_file_path = 'HDF5_File/'+str(agfa_dirs[agfa_dir_num])

	dfAcc=df[df['ACC'].str.match(search_str)]
	total_dfAcc=dfAcc.shape[0]
	# IPython.embed()
	p = 0
	i = 0
	maxstopper = total_dfAcc - 1
	# IPython.embed()

	for i in range(total_dfAcc):
		tipe = dfAcc.iloc[[i]].TIPE.values[0]
		x1 = dfAcc.iloc[[i]].Xmin.values[0]
		y1 = dfAcc.iloc[[i]].Ymin.values[0]
		x2 = dfAcc.iloc[[i]].Xmax.values[0]
		y2 = dfAcc.iloc[[i]].Ymax.values[0]
		z1_slice = dfAcc.iloc[[i]].Zt_minsplitnum.values[0]
		z1 = dfAcc.iloc[[i]].Zt_minsplit.values[0]
		z2_slice = dfAcc.iloc[[i]].Zt_maxsplitnum.values[0]
		z2 = dfAcc.iloc[[i]].Zt_maxsplit.values[0]
		# IPython.embed()

		z1_order = str('%0*d' % (3, z1_slice))
		z2_order = str('%0*d' % (3, z2_slice))

		if x1==0 and x2==0 and y1 ==0 and y2==0:
			print ('\tNo annotation found for ACC = '+str(agfa_dirs[agfa_dir_num])+'.......')
			csv_file.write(str(annot_file_path)+','','','','','','',''\n')
			p = p+1
			i = i+1
		else:
			if search_slice==z1_order==z2_order:
				print ('\tACC and z1, z2 order match found = '+str(search_str)+'.......')
				csv_file.write(str(annot_file_path)+','+str(x1)+','+str(y1)+','+str(x2)+','+str(y2)+','+str(z1)+','+str(z2)+','+str(tipe)+'\n')
				p = p+1
				i = i+1
			else:
				if search_slice==z2_order:
					print ('\tACC and z2 match found = '+str(search_str)+'.......')
					csv_file.write(str(annot_file_path)+','+str(x1)+','+str(y1)+','+str(x2)+','+str(y2)+','+'0'+','+str(z2)+','+str(tipe)+'\n')
					p = p+1
					i = i+1
				if search_slice==z1_order:
					print ('\tACC and z1 match found = '+str(search_str)+'.......')
					csv_file.write(str(annot_file_path)+','+str(x1)+','+str(y1)+','+str(x2)+','+str(y2)+','+str(z1)+','+'32'+','+str(tipe)+'\n')
					p = p+1
					i = i+1
				if p==0 and maxstopper==i:
					print ('\tNo data found for ACC = '+str(agfa_dirs[agfa_dir_num])+'.......')
					csv_file.write(str(annot_file_path)+','','','','','','',''\n')
					p = p+1
				else:
					i = i+1
	print('\tThere are %d new annotations added' %(p))
	agfa_dir_num = agfa_dir_num+1


for kdc6_dir_num in range(len(kdc6_dirs)):
	search_str = kdc6_dirs[kdc6_dir_num][0:10]
	search_slice = kdc6_dirs[kdc6_dir_num][-6:-3]
	print ('Searching: ACC = '+str(search_str)+' and slice = '+str(search_slice)+' at dataframe.......')
	annot_file_path = 'HDF5_File/'+str(kdc6_dirs[kdc6_dir_num])

	dfAcc=df[df['ACC'].str.match(search_str)]
	total_dfAcc=dfAcc.shape[0]
	# IPython.embed()
	p = 0
	i = 0
	maxstopper = total_dfAcc - 1

	for i in range(total_dfAcc):
		tipe = dfAcc.iloc[[i]].TIPE.values[0]
		x1 = dfAcc.iloc[[i]].Xmin.values[0]
		y1 = dfAcc.iloc[[i]].Ymin.values[0]
		x2 = dfAcc.iloc[[i]].Xmax.values[0]
		y2 = dfAcc.iloc[[i]].Ymax.values[0]
		z1_slice = dfAcc.iloc[[i]].Zt_minsplitnum.values[0]
		z1 = dfAcc.iloc[[i]].Zt_minsplit.values[0]
		z2_slice = dfAcc.iloc[[i]].Zt_maxsplitnum.values[0]
		z2 = dfAcc.iloc[[i]].Zt_maxsplit.values[0]

		z1_order = str('%0*d' % (3, z1_slice))
		z2_order = str('%0*d' % (3, z2_slice))

		if x1==0 and x2==0 and y1 ==0 and y2==0:
			print ('\tNo annotation found for ACC = '+str(kdc6_dirs[kdc6_dir_num])+'.......')
			csv_file.write(str(annot_file_path)+','','','','','','',''\n')
			p = p+1
			i = i+1
		else:
			if search_slice==z1_order==z2_order:
				print ('\tACC and z1, z2 order match found = '+str(search_str)+'.......')
				csv_file.write(str(annot_file_path)+','+str(x1)+','+str(y1)+','+str(x2)+','+str(y2)+','+str(z1)+','+str(z2)+','+str(tipe)+'\n')
				p = p+1
				i = i+1
			else:
				if search_slice==z2_order:
					print ('\tACC and z2 match found = '+str(search_str)+'.......')
					csv_file.write(str(annot_file_path)+','+str(x1)+','+str(y1)+','+str(x2)+','+str(y2)+','+'0'+','+str(z2)+','+str(tipe)+'\n')
					p = p+1
					i = i+1
				if search_slice==z1_order:
					print ('\tACC and z1 match found = '+str(search_str)+'.......')
					csv_file.write(str(annot_file_path)+','+str(x1)+','+str(y1)+','+str(x2)+','+str(y2)+','+str(z1)+','+'32'+','+str(tipe)+'\n')
					p = p+1
					i = i+1
				if p==0 and maxstopper==i:
					print ('\tNo data found for ACC = '+str(kdc6_dirs[kdc6_dir_num])+'.......')
					csv_file.write(str(annot_file_path)+','','','','','','',''\n')
					p = p+1
				else:
					i = i+1
	print('\tThere are %d new annotations added' %(p))
	kdc6_dir_num = kdc6_dir_num+1