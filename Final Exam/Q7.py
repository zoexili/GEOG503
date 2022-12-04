import arcpy
arcpy.env.workspace = r"C:\Data\FinalExam\data\rastTester.gdb"
tifflist = arcpy.ListRasters("*cover*")
for tiff in tifflist:
    print(tiff)
    fieldlist = arcpy.ListFields(tiff)
    for field in fieldlist:
        print('\t' + field.name)
