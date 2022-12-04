import arcpy.mapping
arcpy.env.workspace = r"C:\Data\inclass12_data"
mapdoc = arcpy.mapping.MapDocument(r"C:\Data\inclass12_data\Austin_TX.mxd")
listdf = arcpy.mapping.ListDataFrames(mapdoc)
outspace = r"C:\Data\inclass12_data"
for df in listdf:
    print(df.name)
    out = os.path.join(outspace + df.name + ".jpg")
    jpeg = r"C:\Data\inclass12_data\Austin.jpg"
    ExportToJPEG(mapdoc,jpeg,resolution=300)
mapdoc.save
del mapdoc


