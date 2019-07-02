# Batch Images to HDF5 Converter

This repo is used to compile 32 RGB images (JPG) to 1 HDF5 file for CT scan/MRI images with size 512x512 px, in order to feed 3D data to python generator

If there are less than 32 images on last batch, it will takes last 32 images into 1 HDF5 file
Interpolation of upsample used for upsampling are INTER_CUBIC


## Folder:
1. Original_size --> annotation generator and hdf5 generator splitted(TIME CONSUMING), use PIL
2. Upsample_2x --> change the height and width of target into 1024x1024px, annotation generator embedded with HDF5 generator (nodule >32px only), use OpenCV
3. Upsample_4x --> change the height and width of target into 2048x2048px, annotation generator embedded with HDF5 generator (nodule >32px only), use OpenCV

## File size
Generated file size ratio  
original_size : upsample_2x : upsample_4x = 1:4:16
Archive image use zip from CLI (80% space compression)


```zip -r <zip_file_name> <folder_dir> Compression result will reduce >80% of file size```


## Check out other repo:
1. [I3DR-Net Original without weight, and original anchors](https://github.com/ivanwilliammd/i3d-retina-rollover-noweight-orianchors)
2. [I3DR-Net Upsampled with P2 pyramid](https://github.com/ivanwilliammd/i3d-retina-upsample-P2-OOM-)
3. [I3DR-Net Original with smaller anchors](https://github.com/ivanwilliammd/i3d-retina-rollover-editanchors)
4. [JPG to HDF5 Converter](https://github.com/ivanwilliammd/BatchImagesToHDF5_Converter)


------------------------------------------------------------------------------
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

```http://www.apache.org/licenses/LICENSE-2.0```

------------------------------------------------------------------------------
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
******************************************************************************
