__author__ = 'Li Xi'

import arcpy
import os

arcpy.CheckOutExtension("spatial")
arcpy.CheckOutExtension("3D")

#Set parameters
workspace = arcpy.GetParameterAsText(0)
clipfc = arcpy.GetParameterAsText(1)
outspace = arcpy.GetParameterAsText(2)
outtable = arcpy.GetParameterAsText(3)
surface_tiff = arcpy.GetParameterAsText(4)

arcpy.env.workspace = workspace
arcpy.env.overwriteOutput = True
tifflist = arcpy.ListRasters()
cnt = len(tifflist)
arcpy.env.mask = clipfc

#Clip multiple rasters
arcpy.SetProgressor("step","Clipping Rasters to Geodatabase...", 0, cnt, 1)
i = 1
for tiff in tifflist:
    arcpy.SetProgressorLabel("Clipping " + str(i) + "/" + str(cnt) + ": " + tiff + "...")
    desc = arcpy.Describe(tiff)
    out_tiff = os.path.join(outspace, desc.name)
    arcpy.env.snapraster = tiff
    out_ras = arcpy.sa.ExtractByMask(tiff,clipfc)
    out_ras = arcpy.sa.ApplyEnvironment(out_ras)
    out_ras.save(out_tiff)

#Calculate raster properties and get output
elev_min = arcpy.GetRasterProperties_management(out_tiff,"MINIMUM")
elev_max = arcpy.GetRasterProperties_management(out_tiff,"MAXIMUM")
elev_mean = arcpy.GetRasterProperties_management(out_tiff,"MEAN")
elev_sd = arcpy.GetRasterProperties_management(out_tiff,"STD")
elevmin = elev_min.getOutput(0)
elevmax = elev_max.getOutput(0)
elevmean = elev_mean.getOutput(0)
elevsd = elev_sd.getOutput(0)

#insert values into statistic table
fields = ["Minimum","Maximum","Mean","SD"]
cursor = arcpy.da.InsertCursor(outtable,fields)
cursor.insertRow((elevmin,elevmax,elevmean,elevsd))

del cursor

#quantify landform terrain with aspect, contour, hillshades, and slope.
ras_aspect = "aspect" + ".tif"
ras_contour = "contour" + ".tif"
ras_shades = "shades" + ".tif"
ras_slope = "slope" + ".tif"
if surface_tiff.lower() == "true":
    arcpy.SetProgressorLabel("Creating aspect & contour & hillshades & slope...")
    arcpy.env.workspace = outspace
    raslist = arcpy.ListRasters()
    for ras in raslist:
        arcpy.Aspect_3d(ras,ras_aspect)
        arcpy.Contour_3d(ras,ras_contour,200)
        arcpy.HillShade_3d(ras,ras_shades)
        arcpy.Slope_3d(ras,ras_slope)
    arcpy.SetProgressorPosition()

arcpy.CheckInExtension("spatial")
arcpy.CheckInExtension("3D")