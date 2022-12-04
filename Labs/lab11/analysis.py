__author__ = 'Li'

import arcpy
import os

#define the ClipRaster function
def ClipRaster(workspace,clipfc,ouput_dir):
    arcpy.env.workspace = workspace
    arcpy.env.overwriteOutput = True
    tifflist = arcpy.ListRasters()

    desc = arcpy.Describe(clipfc)
    if desc.path = workspace:
        tifflist.remove(desc.file)

    if arcpy.Exists(output_dir) == False:
        arcpy.CreateFolder_management(os.path.split(output_dir)[0],os.path.split(output_dir)[1])

    for tiff in tifflist:
        out_tiff = os.path.join(output_dir,tiff)
        arcpy.Clip_management(tiff,"xmin ymin xmax ymax",out_tiff)