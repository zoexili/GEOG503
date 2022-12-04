import arcpy,os

fc = arcpy.GetParameterAsText(0)
fields = arcpy.GetParameterAsText(1)
outfc = arcpy.GetParameterAsText(2)

arcpy.Copy_management(fc,outfc)
fields = arcpy.ListFields(outfc)
for field in fields:
    if field.type == "String":
        print(field.name)

cursor = arcpy.da.UpdateCursor(outfc,["COVER"])
for row in cursor:
    row[0] = row[0].upper()
    cursor.updateRow(row)

del cursor
del row
