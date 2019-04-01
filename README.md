# 32images_hdf5converter

This repo is used to compile 32 RGB images to 1 HDF5 file
If there are less than 32 images on last batch, it will takes last 32 images into 1 HDF5 file
This code is optimized for CT scan/MRI images with size 512x512 px

Folder:
1. original_size
2. upsample --> change the height and width of target rescale (it used cubic interpolation)
