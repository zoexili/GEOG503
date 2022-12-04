import arcpy

def clipraster(workspace):
    inp = workspace
    clipfc = workspace
    out = workspace
    return out

if arcpy.CheckExtension("spatial") == "Available":
    arcpy.CheckOutExtension("spatial")

if __name__ == "__main__":
cursor = arcpy.da.SearchCursor(clipfc,["SHAPE@"])
for row in cursor:
    extent = row[0].extent
    xmin = extent.XMin
    ymin = extent.YMin
    xmax = extent.XMax
    ymax = extent.YMax
tifflist = arcpy.ListRasters(inp)
cnt = len(tifflist)
arcpy.SetProgressor("step","Clip Rasters to geodatabase...", 0, cnt, 1)
for tiff in tifflist:
    arcpy.SetProgressorLabel("Cliping " + tiff + "...")
    out_tiff = outspace + desc.basename + ".tif"
    cr == "False"
    if cr == "True":
        arcpy.CompositeBands_management(tiff,out_tiff)
    desc = arcpy.Describe(tiff)
    arcpy.Clip_management(tiff,"xmin ymin xmax ymax",out_tiff)
    rasterclip.save(out_tiff)
    arcpy.SetProgressorPosition()
arcpy.ResetProgressor()
arcpy.CheckInExtension("spatial")
del cursor
del row