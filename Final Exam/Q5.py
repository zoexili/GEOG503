import arcpy
arcpy.env.workspace = r"C:\Data\FinalExam\data"
fclist = arcpy.ListFeatureClasses("*out*.shp")
for fc in fclist:
    result = arcpy.GetCount_management(fc)
    count = int(result.getOutput(0))
    print(fc + " has {} entries".format(count))