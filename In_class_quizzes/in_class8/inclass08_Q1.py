import arcpy
inp = arcpy.GetParameterAsText(0)
clipfc = arcpy.GetParameterAsText(1)
outspace = arcpy.GetParameterAsText(2)
fclist = arcpy.ListFeatureClasses(inp)
for fc in fclist:
    desc = arcpy.Describe(fc)
    name = desc.basename
    outfc = outspace + name + ".shp"
    arcpy.Clip_analysis(fc,clipfc,outfc)