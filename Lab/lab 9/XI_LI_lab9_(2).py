import arcpy

#get user provided inputs
fc = arcpy.GetParameterAsText(0)
fields = arcpy.GetParameterAsText(1)
fieldlist = fields.split(";")
delimiter = arcpy.GetParameterAsText(2)
export_file = arcpy.GetParameterAsText(3)

#process field values
f = open(export_file,"w")

cursor = arcpy.da.UpdateCursor(fc,fieldlist)
for row in cursor:
    line = "{}: {}".format(fieldlist,delimiter.join(str(i) for i in row))
    f.write(line + "\n")
    
del cursor
f.close()

