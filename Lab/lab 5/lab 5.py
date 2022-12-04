# lab 5
## Question 1
import arcpy
from arcpy import env
env.workspace = r"C:\Geog 503\lab5"
env.overwriteOutput = True
arcpy.CreateFileGDB_management("Results/", "new.gdb")
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    desc = arcpy.Describe(fc)
    basename = desc.basename
    type = desc.shapetype
    if type == "point" or "polygon":
        arcpy.CopyFeatures_management(fc, "Results/new.gdb/", basename)

## Question 2
import arcpy
arcpy.env.workspace = r"C:\Geog 503\lab5\testdata.gdb"
fclist = arcpy.ListFeatureClasses()
tifflist = arcpy.ListRasters()
for fc in fclist:
    desc = arcpy.Describe(fc)
    Type1 = desc.shapetype
    if Type1 == "polygon":
        arcpy.CopyFeatures_management(fc, "Results/" + fc)
for tiff in tifflist:
    desc = arcpy.Describe(tiff)
    Type2 = desc.datatype
    if Type2 == "float":
        arcpy.CopyFeatures_management(tiff, "Results/" + tiff)

## Question 3
import arcpy
arcpy.env.workspace = r"C:\Geog 503\lab5\Results"
for tiff in tifflist:
    desc = arcpy.Describe(tiff)
    sr = desc.spatialreference.name
    cell_y = desc.meanCellHeight
    cell_x = desc.meanCellWidth
    column = desc.width
    width = desc.height
    min = desc.minimum
    max = desc.maximum
    mean = desc.mean
print (sr, cell_y, cell_x, column, width, min, max, mean)

## Question 4
import arcpy
from arcpy import env
env.workspace = r"C:\Geog 503\lab5\Results"
fieldlist = arcpy.ListFields("*.shp")
for field in fieldlist:
    if field.length > 10:
        print field
