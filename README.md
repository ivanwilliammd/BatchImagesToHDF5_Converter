# Batch Images to HDF5 Converter

This repo is used to compile 32 RGB images (JPG) to 1 HDF5 file for CT scan/MRI images with size 512x512 px, in order to feed 3D data to python generator

If there are less than 32 images on last batch, it will takes last 32 images into 1 HDF5 file
Interpolation of upsample used for upsampling are INTER_CUBIC


#Folder:
1. Original_size --> annotation generator and hdf5 generator splitted(TIME CONSUMING), use PIL
2. Upsample_2x --> change the height and width of target into 1024x1024px, annotation generator embedded with HDF5 generator (nodule >32px only), use OpenCV
3. Upsample_4x --> change the height and width of target into 2048x2048px, annotation generator embedded with HDF5 generator (nodule >32px only), use OpenCV

#File size
Generated file size ratio  
original_size : upsample_2x : upsample_4x = 1:4:16
To compress image use zip from CLI --> zip -r <zip_file_name> <folder_dir>
Compression result will reduce >80% of file size
