from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt
import os

ds = gdal.Open('NE1_50M_SR_W/NE1_50M_SR_W.tif')

gt = ds.GetGeoTransform()
#print (gt)

proj = ds.GetProjection()
print (proj)
num_of_bands = ds.RasterCount
#print (num_of_bands)

band_1 = ds.GetRasterBand(1)
array_1 = band_1.ReadAsArray()

band_2 = ds.GetRasterBand(2)
array_2 = band_2.ReadAsArray()

band_3 = ds.GetRasterBand(3)
array_3 = band_3.ReadAsArray()


binmask = np.where(array_1 >= np.mean(array_1), 1, 0)
#binmask = binmask.astype(np.uint8)

# plt.imshow(binmask)
# # #plt.imshow(array_1)
# plt.show()

#print (binmask)

# cv2.imwrite('binmask.tif', binmask)
driver = gdal.GetDriverByName('GTiff')
driver.Register()
outds = driver.Create('binmask.tif', xsize = binmask.shape[1],
                      ysize = binmask.shape[0], bands = 1,
                    eType = gdal.GDT_Byte)

outds.SetGeoTransform(gt)
outds.SetProjection(proj)
outband = outds.GetRasterBand(1)
outband.WriteArray(binmask)
outband.SetNoDataValue(np.nan)
outband.FlushCache()
outband = None
outds = None 

import matplotlib.pyplot as plt
im = plt.imread('binmask.tif', 0)
#im = cv2.imread('binmask.tif', 0)

plt.imshow(im)
plt.show()

