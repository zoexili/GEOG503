import arcpy
arcpy.env.workspace = r"C:\Data\FinalExam\data"
mapdoc = arcpy.mapping.MapDocument(r"C:\Data\FinalExam\data\states.mxd")
print("Map: {}".format(mapdoc.filePath))
dflist = arcpy.mapping.ListDataFrames(mapdoc)
df1 = arcpy.mapping.ListDataFrames(mapdoc,"Northeast")[0]
print("Frame 0: {}".format(df1.name))
lyrlist1 = arcpy.mapping.ListLayers(mapdoc,data_frame=df1)
i = 0
for lyr in lyrlist1:
    print("         Layer {}: {}  {}".format(i,lyr.name,lyr.workspacePath))
    i += 1
df2 = arcpy.mapping.ListDataFrames(mapdoc,"Southeast")[0]
print("Frame 1: {}".format(df2.name))
lyrlist2 = arcpy.mapping.ListLayers(mapdoc,data_frame=df2)
i = 0
for lyr in lyrlist2:
    print("         Layer {}: {}  {}".format(i, lyr.name, lyr.workspacePath))
    i += 1
